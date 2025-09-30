import random

from vector import Vector

def generate_forel(coords):
    """Generate random forel coords and return list"""
    min_el_val = coords[0][0]
    max_el_val = coords[0][0]

    for i in coords:
        if min(i) < min_el_val:
            min_el_val = min(i)
        if max(i) > max_el_val:
            max_el_val = max(i)

    forel_coords = []
    for i in range(len(coords[0])):
        forel_coords.append(random.random()*(max_el_val-min_el_val)+min_el_val)

    forel = Vector(forel_coords)
    return forel

def get_cluster_vectors(vectors, forel, metric, R):
    """Get cluster of vector when r(vector, forel) < R and return list of vectors"""
    cluster_vectors = []
    for i in vectors:
        if metric == 'evklid':
            if forel.evklid_dist(i) < R:
                cluster_vectors.append(i)
        if metric == 'manhetten':
            if forel.manhetten_dist(i) < R:
                cluster_vectors.append(i)
        if metric == 'max':
            if forel.max_metric_dist(i) < R:
                cluster_vectors.append(i)
    return cluster_vectors

def center_mass_calc(vectors):
    """Calculate center mass of vectors and return list of center mass coords"""
    if not vectors:
        return []
    
    center_mass_coords = []
    for i in range(len(vectors[0].get_coords())):
        coord_sum = 0
        for j in vectors:
            coord_sum += j.get_coords()[i]
        center_mass_coords.append(coord_sum/len(vectors))
    return center_mass_coords

def forel_alg(vectors, R):
    """Apply FOREL algorithm and return list of vectors"""
    coords = []
    for i in vectors:
        coords.append(i.get_coords())
    clusters = []
    vectors_copy = vectors.copy()
    coords_copy = coords.copy()
    while len(vectors_copy) != 0:
        print(f'Num of vectors = {len(vectors_copy)}')
        forel = generate_forel(coords_copy)
        cluster_vectors = get_cluster_vectors(vectors_copy, forel, R)
        center_mass_start = center_mass_calc(cluster_vectors, forel, R)
        forel = Vector(center_mass_start)
        cluster_vectors = get_cluster_vectors(vectors_copy, forel)
        center_mass_new = center_mass_calc(cluster_vectors, forel, R)
        iter = 1
        while center_mass_new != center_mass_start:
            center_mass_start = center_mass_new
            forel = Vector(center_mass_start)
            cluster_vectors = get_cluster_vectors(vectors_copy, forel)
            center_mass_new = center_mass_calc(cluster_vectors, forel, R)
        for i in cluster_vectors:
            vectors_copy.remove(i)
            coords_copy.remove(i.get_coords())
        clusters.append(cluster_vectors)
    return clusters