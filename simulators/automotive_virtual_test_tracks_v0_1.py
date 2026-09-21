"""Biupiu Automotive Virtual Test Tracks v0.1.
Dependency-light scenario generator. Screening only; not a certified solver.
"""
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass(frozen=True)
class Segment:
    id: str
    kind: str
    length_m: float
    radius_m: Optional[float] = None
    grade_pct: float = 0.0
    friction_mu: float = 1.0
    target_speed_kph: Optional[float] = None
    def validate(self):
        if self.length_m <= 0: raise ValueError(f"{self.id}: length_m must be positive")
        if self.radius_m is not None and self.radius_m <= 0: raise ValueError(f"{self.id}: radius_m must be positive")
        if self.friction_mu <= 0: raise ValueError(f"{self.id}: friction_mu must be positive")

@dataclass(frozen=True)
class Track:
    id: str
    purpose: str
    segments: tuple[Segment, ...]
    def validate(self):
        if not self.segments: raise ValueError(f"{self.id}: no segments")
        for s in self.segments: s.validate()
    @property
    def length_m(self): return sum(s.length_m for s in self.segments)
    @property
    def corner_count(self): return sum(s.radius_m is not None for s in self.segments)
    def manifest(self):
        self.validate()
        return {"track_id":self.id,"purpose":self.purpose,"length_m":round(self.length_m,2),"corner_count":self.corner_count,"segments":[asdict(s) for s in self.segments]}

def create_default_tracks():
    return (
      Track("AUTO-TEST-01-DYNAMIC-LOOP","acceleration, braking, lane change, cornering and endurance",
            (Segment("start","straight",900,target_speed_kph=220),Segment("brake-01","braking",180,target_speed_kph=80),Segment("turn-01","corner",160,65,target_speed_kph=90),Segment("slalom-01","slalom",300,45,target_speed_kph=100),Segment("back-straight","straight",700,target_speed_kph=220))),
      Track("AUTO-TEST-02-HANDLING-CIRCUIT","constant-radius, transient steer and slalom",
            (Segment("approach","straight",500,target_speed_kph=120),Segment("constant-radius","corner",250,100,target_speed_kph=110),Segment("transition","slalom",300,50,target_speed_kph=90),Segment("exit","straight",500,target_speed_kph=160))),
      Track("AUTO-TEST-03-BRAKE-STABILITY-PAD","straight braking and split-mu screening",
            (Segment("launch","straight",500,target_speed_kph=160),Segment("high-mu","braking",120,friction_mu=1.05),Segment("reset","straight",100,target_speed_kph=30),Segment("low-mu","braking",120,friction_mu=.55),Segment("runoff","straight",250,friction_mu=.55))),
      Track("AUTO-TEST-04-ROUGH-ROAD","ride, suspension and durability",
            (Segment("approach","straight",250,target_speed_kph=80),Segment("corrugation","rough",500,.0,0,.95,70),Segment("pothole-proxy","rough",100,.0,0,.9,35),Segment("grade","grade",400,.0,8, .95,60))),
      Track("AUTO-TEST-05-WET-LOW-MU","wet/low-friction handling",
            (Segment("wet-entry","wet",250,friction_mu=.65,target_speed_kph=80),Segment("wet-corner","corner",140,70,friction_mu=.60,target_speed_kph=60),Segment("wet-slalom","slalom",280,50,friction_mu=.62,target_speed_kph=70))),
      Track("AUTO-TEST-06-AERO-HIGH-SPEED","high-speed stability and aero screening",
            (Segment("aero-straight","straight",1800,target_speed_kph=280),Segment("fast-corner","corner",260,300,target_speed_kph=220),Segment("return","straight",1200,target_speed_kph=280))),
      Track("AUTO-TEST-07-EV-ENERGY","EV/hybrid energy and thermal cycle",
            (Segment("urban","cycle",900,target_speed_kph=60),Segment("accelerate","cycle",500,target_speed_kph=120),Segment("regen","regeneration",300,target_speed_kph=40),Segment("grade-up","grade",600,grade_pct=6,target_speed_kph=80),Segment("grade-down","regeneration",600,grade_pct=-6,target_speed_kph=60))),
      Track("AUTO-TEST-08-AUTONOMOUS-SENSOR","lane following, obstacles, intersections and sensor fusion",
            (Segment("lane-follow","autonomy",600,target_speed_kph=50),Segment("obstacle-zone","autonomy",300,target_speed_kph=35),Segment("intersection","autonomy",220,target_speed_kph=30),Segment("merge","autonomy",400,target_speed_kph=60)))
    )

def curvature_speed_kph(radius_m, friction_mu):
    return (max(0.0, friction_mu*9.80665*radius_m)**0.5)*3.6

def run_screen(track):
    track.validate()
    return {"track_id":track.id,"length_m":round(track.length_m,2),"corner_count":track.corner_count,
            "corner_limits":[{"segment":s.id,"screen_speed_kph":round(curvature_speed_kph(s.radius_m,s.friction_mu),2)} for s in track.segments if s.radius_m is not None],
            "validation":"screened"}
