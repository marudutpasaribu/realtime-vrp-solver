import matplotlib.pyplot as plt

def plot_routes(nodes, routes):
    # nodes: [[nama, lat, lon, demand], ...]
    # routes: [[0, 1, 0], [0, 2, 3, 0]]
    
    plt.figure(figsize=(10, 6))
    colors = ["red", "blue", "green", "orange", "purple"]

    for idx, route in enumerate(routes):
        lats = [nodes[node_idx][1] for node_idx in route]
        lons = [nodes[node_idx][2] for node_idx in route]
        
        plt.plot(lons, lats, marker="o", color=colors[idx % len(colors)], label=f"Vehicle {idx+1}")

    # Plot Depot (biasanya node 0)
    plt.scatter(nodes[0][2], nodes[0][1], color='black', marker='s', s=100, label='Depot')
    
    plt.title("VRP Optimized Routes")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.grid(True)
    plt.show()