import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R = 6371

    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)

    a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))


def build_distance_matrix(nodes):
    n = len(nodes)
    matrix = np.zeros((n, n))
    demands = []

    for i in range(n):
        # Unpacking data berdasarkan urutan: [nama, lat, lon, demand]
        _, lat1, lon1, demand = nodes[i]
        demands.append(demand)
        
        for j in range(n):
            _, lat2, lon2, _ = nodes[j]
            # Menggunakan fungsi haversine yang sudah Anda buat
            matrix[i][j] = haversine(lat1, lon1, lat2, lon2)

    return matrix, demands