# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="PhysicaSim Backend")

@app.get("/health")
def health():
    return {"status": "ok"}

# example endpoint for a simple projectile simulation (single-step)
class ProjectileParams(BaseModel):
    angle_deg: float
    speed: float
    gravity: float = 9.81

@app.post("/simulate/projectile/simple")
def simulate_projectile(params: ProjectileParams):
    # single-step shallow example (we'll replace with real sim later)
    import math
    theta = math.radians(params.angle_deg)
    vx = params.speed * math.cos(theta)
    vy = params.speed * math.sin(theta)
    # return initial velocity components for the frontend to visualize
    return {"vx": vx, "vy": vy, "gravity": params.gravity}
