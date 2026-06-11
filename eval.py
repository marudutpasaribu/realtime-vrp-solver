import time
import json
import numpy as np
from solver import solve_vrp
from preprocessing import build_distance_matrix

def calculate_total_distance(routes, matrix):
    total_dist = 0
    for route in routes:
        # Menghitung jarak berdasarkan urutan node dalam rute
        for i in range(len(route) - 1):
            total_dist += matrix[route[i]][route[i+1]]
    return total_dist

def run_evaluation(data_file):
    print(f"--- Evaluasi: {data_file} ---")
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    # Ambil parameter dari data JSON yang sesuai dengan API request
    # Kita gunakan .get() agar lebih aman jika key tidak ada
    num_vehicles = data.get('num_vehicles', data.get('vehicles')) # Support format lama & baru
    capacity = data.get('capacity')
    
    # Start timer
    start_time = time.time()
    
    # 1. Preprocessing
    matrix, demands = build_distance_matrix(data['nodes'])
    
    # 2. Solver (VRP)
    routes = solve_vrp(matrix, demands, num_vehicles, capacity)
    
    # End timer
    end_time = time.time()
    
    # Calculate Results
    duration = end_time - start_time
    total_distance = calculate_total_distance(routes, matrix)
    
    print(f"Waktu Eksekusi : {duration:.4f} detik")
    print(f"Total Jarak    : {total_distance:.2f} unit")
    print(f"Jumlah Rute    : {len(routes)}")
    print(f"Status Latensi : {'PASS' if duration < 2.0 else 'FAIL'} (< 2s)")
    print("-----------------------------\n")
    
    return {"time": duration, "distance": total_distance}

if __name__ == "__main__":
    # Sekarang bisa digunakan untuk tes tunggal atau looping semua file test_data
    import os
    
    # Uji file tunggal
    test_files = ['test_data.json'] 
    
    # Opsional: Jika ingin otomatis mendeteksi semua file test_data_xxx.json
    # test_files = [f for f in os.listdir('.') if f.startswith('test_data') and f.endswith('.json')]
    
    for file in test_files:
        try:
            run_evaluation(file)
        except Exception as e:
            print(f"Error pada file {file}: {str(e)}")