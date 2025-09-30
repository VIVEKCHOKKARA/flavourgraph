import networkx as nx

def build_graph(recipes):
    """
    Build an ingredient co-occurrence graph from recipes.
    """
    G = nx.Graph()
    for recipe in recipes:
        ingredients = recipe["ingredients"]
        for i in range(len(ingredients)):
            for j in range(i + 1, len(ingredients)):
                u, v = ingredients[i], ingredients[j]
                if G.has_edge(u, v):
                    G[u][v]["weight"] += 1
                else:
                    G.add_edge(u, v, weight=1)
    return G
