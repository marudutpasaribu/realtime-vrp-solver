from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Hapus import dari config jika tidak diperlukan lagi
# from config import NUM_VEHICLES, VEHICLE_CAPACITY 

def solve_vrp(distance_matrix, demands, num_vehicles, capacity): # Terima 4 argumen

    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix),
        num_vehicles, # Gunakan argumen dinamis
        0
    )

    routing = pywrapcp.RoutingModel(manager)

    # distance callback
    def distance_callback(i, j):
        return int(distance_matrix[
            manager.IndexToNode(i)
        ][manager.IndexToNode(j)] * 1000)

    transit_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_index)

    # demand callback
    def demand_callback(i):
        return demands[manager.IndexToNode(i)]

    demand_index = routing.RegisterUnaryTransitCallback(demand_callback)

    routing.AddDimensionWithVehicleCapacity(
        demand_index,
        0,
        [capacity] * num_vehicles, # Gunakan argumen dinamis
        True,
        "Capacity"
    )

    # solver config
    params = pywrapcp.DefaultRoutingSearchParameters()
    params.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    params.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    params.time_limit.FromSeconds(2)

    solution = routing.SolveWithParameters(params)

    routes = []

    if solution:
        for v in range(num_vehicles): # Gunakan argumen dinamis
            index = routing.Start(v)
            route = []

            while not routing.IsEnd(index):
                node = manager.IndexToNode(index)
                route.append(node)
                index = solution.Value(routing.NextVar(index))

            route.append(manager.IndexToNode(index))
            routes.append(route)

    return routes