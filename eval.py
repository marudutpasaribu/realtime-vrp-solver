import time
import json
import pandas as pd
from solver import solve_vrp
from preprocessing import build_distance_matrix

def calculate_total_distance(routes, matrix):
    total_dist = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_dist += matrix[route[i]][route[i+1]]
    return total_dist

def run_evaluation(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    num_vehicles = data.get('num_vehicles', data.get('vehicles'))
    capacity = data.get('capacity')
    
    start_time = time.time()
    matrix, demands = build_distance_matrix(data['nodes'])
    routes = solve_vrp(matrix, demands, num_vehicles, capacity)
    end_time = time.time()
    
    duration = end_time - start_time
    total_distance = calculate_total_distance(routes, matrix)
    
    return {
        "file": data_file,
        "nodes": len(data['nodes']),
        "time": round(duration, 4),
        "distance": round(total_distance, 2),
        "status": "PASS" if duration < 2.0 else "FAIL"
    }

if __name__ == "__main__":
    import os
    # Mendeteksi semua file test_data
    test_files = [f for f in os.listdir('.') if f.startswith('test_data') and f.endswith('.json')]
    
    results = []
    for file in sorted(test_files):
        try:
            results.append(run_evaluation(file))
        except Exception as e:
            print(f"Error pada {file}: {e}")

    # Menampilkan tabel perbandingan
    df = pd.DataFrame(results)
    print("\n--- BENCHMARK REPORT ---")
    print(df.to_string(index=False))