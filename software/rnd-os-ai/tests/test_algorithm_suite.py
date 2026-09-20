from biupiu_ai.ml.algorithm_suite import *

def test_linear_regression_baseline():
    w,b=linear_regression_gd([[0],[1],[2]],[0,2,4],learning_rate=0.05,epochs=1000)
    assert abs(w[0]-2)<0.1

def test_logistic_regression_baseline():
    w,b=logistic_regression_gd([[0],[1],[2],[3]],[0,0,1,1],epochs=1000)
    assert logistic_predict(w,b,[3])>0.8

def test_kmeans_separates_clusters():
    labels,_=kmeans([[0],[0.1],[10],[10.1]],2)
    assert labels[0]==labels[1] and labels[2]==labels[3] and labels[0]!=labels[2]

def test_anomaly_and_drift_primitives():
    assert zscore_anomalies([1,1,1,1,20])[-1] is True
    assert len(ewma([1,2,3]))==3
    assert psi([.5,.5],[.9,.1])>0

def test_federated_aggregation_and_staleness():
    assert fedavg([(1,2),(3,4)],[1,3])==(2.5,3.5)
    assert async_weighted_update((0,0),(2,2),staleness=1)==(0.5,0.5)

def test_q_learning_update():
    q=q_learning_update({}, "s","a",1,["b"] ,alpha=1,gamma=0.5)
    assert q[("s","a")]==1