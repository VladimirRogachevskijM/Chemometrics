import numpy as np

class Experimental_Data:
    """Class Experimental_Data.
    
    Parameters:

    data : 2-dim np.array, where rows - experiments, columns - params (e.g. T, p etc.)
    """

    def __init__(self, data):
        self.__data = data
    
    @property
    def data(self):
        return self.__data