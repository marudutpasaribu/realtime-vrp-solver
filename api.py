from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
from typing import List, Any
import webbrowser
import threading
import time

from solver import solve_vrp
from preprocessing import build_distance_matrix
from eval import calculate_total_distance  # Pastikan diimpor di sini

app = FastAPI(
    title="VRP Optimization System",
    version="1.0.0"
)

# =========================
# INPUT MODEL
# =========================
class VRPRequest(BaseModel):
    nodes: List[List[Any]] = Field(
        ..., 
        description="Format: [[nama, latitude, longitude, demand], ...]"
    )
    num_vehicles: int = Field(..., gt=0)
    capacity: int = Field(..., gt=0)


# =========================
# GET ROOT
# =========================
@app.get("/", tags=["General"])
async def read_root():
    return RedirectResponse(url="/docs")


# =========================
# POST SOLVE
# =========================
@app.post("/solve", tags=["Optimization"])
async def solve(request: VRPRequest):
    try:
        matrix, demands = build_distance_matrix(request.nodes)
        routes = solve_vrp(matrix, demands, request.num_vehicles, request.capacity)
        
        # Hitung total jarak sebelum return
        total_dist = calculate_total_distance(routes, matrix)
        
        return {
            "status": "success",
            "total_distance": round(total_dist, 2),
            "num_vehicles": request.num_vehicles,
            "capacity": request.capacity,
            "routes": routes
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def buka_chrome():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:8000")

threading.Thread(target=buka_chrome, daemon=True).start()


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)