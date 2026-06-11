from data_loader import load_osm_nodes
from preprocessing import build_distance_matrix
from solver import solve_vrp
from visualization import plot_routes

def main():

    print("Loading OSM data...")
    nodes = load_osm_nodes()

    print("Building distance matrix...")
    distance_matrix, demands = build_distance_matrix(nodes)

    print("Solving VRP...")
    routes = solve_vrp(distance_matrix, demands)

    print("\nRESULT ROUTES:")
    for i, r in enumerate(routes):
        print(f"Vehicle {i}: {r}")

    plot_routes(nodes, routes)


if __name__ == "__main__":
    main()