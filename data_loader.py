import osmnx as ox
from config import PLACE_NAME, OSM_TAGS

def load_osm_nodes():
    gdf = ox.features_from_place(PLACE_NAME, OSM_TAGS)

    nodes = []

    for _, row in gdf.iterrows():
        if row.geometry.geom_type == "Point":
            name = row.get("name", "unknown")
            lat = row.geometry.y
            lon = row.geometry.x
            nodes.append((name, lat, lon))

    # tambahkan depot manual (pusat kota)
    G = ox.graph_from_place(PLACE_NAME, network_type="drive")
    center_node = list(G.nodes())[0]
    lat = G.nodes[center_node]["y"]
    lon = G.nodes[center_node]["x"]

    nodes.insert(0, ("DEPOT", lat, lon))

    return nodes