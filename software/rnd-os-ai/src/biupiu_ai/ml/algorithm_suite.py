"""Dependency-light AI/ML algorithm primitives for Biupiu verification and simulation.

The implementations are deterministic reference algorithms, not claims of production
model quality. They provide a local baseline before optional specialist libraries.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping, Sequence

def _dot(a,b): return sum(float(x)*float(y) for x,y in zip(a,b))

def linear_regression_gd(X, y, *, learning_rate=0.01, epochs=500):
    if not X or len(X)!=len(y): raise ValueError("X and y must be aligned and non-empty")
    w=[0.0]*len(X[0]); b=0.0; n=len(X)
    for _ in range(epochs):
        errors=[_dot(w,x)+b-float(t) for x,t in zip(X,y)]
        for j in range(len(w)): w[j]-=learning_rate*2.0/n*sum(e*x[j] for e,x in zip(errors,X))
        b-=learning_rate*2.0/n*sum(errors)
    return tuple(w), b

def logistic_predict(weights, bias, x):
    z=_dot(weights,x)+float(bias)
    z=max(-60.0,min(60.0,z))
    return 1.0/(1.0+math.exp(-z))

def logistic_regression_gd(X,y,*,learning_rate=0.1,epochs=500):
    if not X or len(X)!=len(y): raise ValueError("X and y must be aligned and non-empty")
    w=[0.0]*len(X[0]); b=0.0; n=len(X)
    for _ in range(epochs):
        p=[logistic_predict(w,b,x) for x in X]
        for j in range(len(w)): w[j]-=learning_rate/n*sum((pi-yi)*x[j] for pi,yi,x in zip(p,y,X))
        b-=learning_rate/n*sum(pi-yi for pi,yi in zip(p,y))
    return tuple(w), b

def kmeans(points, k, *, iterations=50):
    if not points or k<1 or k>len(points): raise ValueError("invalid points or k")
    centroids=[tuple(map(float,p)) for p in points[:k]]
    labels=[0]*len(points)
    for _ in range(iterations):
        new_labels=[]
        for p in points:
            new_labels.append(min(range(k), key=lambda c: sum((float(a)-b)**2 for a,b in zip(p,centroids[c]))))
        new_centroids=[]
        for c in range(k):
            members=[points[i] for i,l in enumerate(new_labels) if l==c]
            new_centroids.append(tuple(sum(float(p[j]) for p in members)/len(members) for j in range(len(points[0]))) if members else centroids[c])
        if new_labels==labels and new_centroids==centroids: break
        labels,centroids=new_labels,new_centroids
    return tuple(labels),tuple(centroids)

def zscore_anomalies(values, *, threshold=3.0):
    if not values: raise ValueError("values required")
    mean=sum(values)/len(values); variance=sum((v-mean)**2 for v in values)/len(values)
    sd=math.sqrt(variance)
    if sd==0: return tuple(False for _ in values)
    return tuple(abs((v-mean)/sd)>threshold for v in values)

def ewma(values, *, alpha=0.2):
    if not values or not 0<alpha<=1: raise ValueError("invalid EWMA input")
    out=[]; state=float(values[0]); out.append(state)
    for v in values[1:]: state=alpha*float(v)+(1-alpha)*state; out.append(state)
    return tuple(out)

def psi(expected, actual, *, epsilon=1e-6):
    if len(expected)!=len(actual) or not expected: raise ValueError("aligned distributions required")
    return sum((a-e)*math.log((a+epsilon)/(e+epsilon)) for e,a in zip(expected,actual))

def fedavg(client_weights, client_sizes):
    if not client_weights or len(client_weights)!=len(client_sizes): raise ValueError("clients required")
    if any(len(w)!=len(client_weights[0]) for w in client_weights): raise ValueError("weight shapes differ")
    total=sum(client_sizes)
    if total<=0: raise ValueError("client sizes must be positive")
    return tuple(sum(w[j]*n for w,n in zip(client_weights,client_sizes))/total for j in range(len(client_weights[0])))

def async_weighted_update(global_weights, client_weights, *, staleness=0, base_weight=0.5):
    if len(global_weights)!=len(client_weights) or not 0<=base_weight<=1: raise ValueError("invalid update")
    weight=base_weight/(1.0+max(0,staleness))
    return tuple((1-weight)*g+weight*c for g,c in zip(global_weights,client_weights))

@dataclass(frozen=True)
class QLearningTable:
    q: Mapping[tuple[str,str], float]

def q_learning_update(q, state, action, reward, next_actions, *, alpha=0.1, gamma=0.95):
    if not 0<=alpha<=1 or not 0<=gamma<=1: raise ValueError("alpha/gamma out of range")
    current=float(q.get((state,action),0.0))
    future=max((float(q.get((state,a),0.0)) for a in next_actions), default=0.0)
    updated=current+alpha*(float(reward)+gamma*future-current)
    out=dict(q); out[(state,action)]=updated; return out