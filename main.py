from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from data_loader import load_osm_nodes
from preprocessing import build_distance_matrix
from solver import solve_vrp

app = FastAPI()  # Uvicorn sekarang akan menemukan variabel 'app' ini

class VRPRequest(BaseModel):
    # Sesuaikan dengan format input yang dibutuhkan sistem Anda
    data_nodes: List[dict] 

@app.post("/solve")
async def solve(request: VRPRequest):
    # Pindahkan logika dari fungsi main() Anda ke sini
    nodes = request.data_nodes 
    distance_matrix, demands = build_distance_matrix(nodes)
    routes = solve_vrp(distance_matrix, demands)
    return {"routes": routes}

@app.get("/")
async def root():
    return {"message": "VRP Optimization API is running"}