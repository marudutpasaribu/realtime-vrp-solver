from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def solve_vrp(distance_matrix, demands, num_vehicles, capacity):
    # 1. Validasi Dasar: Apakah total demand muat di seluruh kendaraan?
    if sum(demands) > (num_vehicles * capacity):
        raise ValueError(f"Infeasible: Total demand ({sum(demands)}) melebihi total kapasitas armada ({num_vehicles * capacity}).")

    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, 0)
    routing = pywrapcp.RoutingModel(manager)

    # distance callback
    def distance_callback(i, j):
        return int(distance_matrix[manager.IndexToNode(i)][manager.IndexToNode(j)] * 1000)

    transit_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_index)

    # demand callback
    def demand_callback(i):
        return demands[manager.IndexToNode(i)]

    demand_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_index, 0, [capacity] * num_vehicles, True, "Capacity"
    )

    # solver config
    params = pywrapcp.DefaultRoutingSearchParameters()
    params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    params.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    params.time_limit.seconds = 2 # Cara yang lebih standar untuk set time limit

    solution = routing.SolveWithParameters(params)

    if not solution:
        raise ValueError("Solver tidak menemukan solusi feasible dalam batasan waktu/kapasitas yang diberikan.")

    routes = []
    for v in range(num_vehicles):
        index = routing.Start(v)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        routes.append(route)

    return routes