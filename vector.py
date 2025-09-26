import math

from core import mean, sko

class Vector:

    """Object vector
    
    method lenght calculate lenght of vector; methods evklid_-,manhetten_-, max_metric_-dist -
    calculate distance between two vectors
    """

    def __init__(self, coords):
        self.coords = coords

    def lenght(self, coords):
        """Calculation of vector lenght and return float"""
        vector_lenght = 0
        for i in coords:
            vector_lenght += coords[i]**2
        return math.sqrt(vector_lenght)
    
    def evklid_dist(self, other):
        """Calculation of vector distans in Evklid metrics and return float"""
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors needs same lenght")
        dist = 0
        for i in range(len(self.coords)):
            dist += (self.coords[i] - other.coords[i])**2
        dist = math.sqrt(dist)
        return dist
    
    def manhetten_dist(self, other):
        """Calculation of vector distans in Manhetten metrics and return float"""
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors needs same lenght")
        dist = 0
        for i in range(len(self.coords)):
            if self.coords[i] >= other.coords[i]:
                dist += (self.coords[i] - other.coords[i])
            else:
                dist += (other.coords[i] - self.coords[i])
        return dist
    
    def max_metric_dist(self, other):
        """Calculation of vector distans in max-metrics and return float"""
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors needs same lenght")
        dists = []
        dist = 0
        for i in range(len(self.coords)):
            if self.coords[i] >= other.coords[i]:
                dist = (self.coords[i] - other.coords[i])
            else:
                dist = (other.coords[i] - self.coords[i])
            dists.append(dist)
        return max(dists)
    
    def normalize_min_max(self):
        """Return list of float normalized coords in accordance with formula Xnew = (X-Xmin)/(Xmax-Xmin)"""
        normalized_coords = []
        for i in self.coords:
            normalized_coords.append((i-min(self.coords))/(max(self.coords)-min(self.coords)))
        return normalized_coords
    
    def normalized_mean(self):
        """Return list of float normalized coords in accordance with formula Xnew = (X-Xmean)/RSD"""
        normalized_coords = []
        list_mean = mean(self.coords)
        list_sko = sko(self.coords)
        for i in self.coords:
            normalized_coords.append((i-list_mean)/list_sko)
        return normalized_coords