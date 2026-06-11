import json
import random

def generate_data(num_nodes):
    # Depot di titik pusat
    nodes = [["Depot", -2.99, 103.67, 0]] 
    for i in range(num_nodes - 1):
        # Koordinat acak di sekitar depot (variasi 0.1 derajat ~11km)
        nodes.append([
            f"Node_{i}", 
            -2.99 + random.uniform(-0.1, 0.1), 
            103.67 + random.uniform(-0.1, 0.1), 
            random.randint(1, 5) # Demand random 1-5
        ])
    
    # Kapasitas disesuaikan agar selalu feasibel (total demand / 2)
    total_demand = sum([n[3] for n in nodes])
    return {
        "nodes": nodes, 
        "num_vehicles": 3, 
        "capacity": max(10, int(total_demand / 2))
    }

if __name__ == "__main__":
    for size in [5, 25, 50, 100]:
        filename = f"test_data_{size}.json"
        with open(filename, 'w') as f:
            json.dump(generate_data(size), f)
        print(f"Berhasil membuat: {filename}")