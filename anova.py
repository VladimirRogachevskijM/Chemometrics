import numpy as np
from scipy.stats import f

class ANOVA:
    """Class ANOVA (Analysator of variance).
    
    Parameters:

    data : np.array - two-rang tensor, rows - experiments, culumns - replics
    """

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    def impact(self, confidence_level = 0.95):
        """Return integetr 1 if observed dependence and 0 if not"""
        data = self.data
        n_exp = len(data)
        n_rep = len(data[0])
        mean = np.mean(data)
        ss_exp = 0
        ss_rep = 0
        for experiment in data:
            exp_mean = np.mean(experiment)
            for rep in experiment:
                ss_exp += (rep-mean)**2
                ss_rep += (rep - exp_mean)**2
        ss_exp *= n_rep
        F_n1 = n_exp - 1
        F_n2 = n_exp*(n_rep-1)
        ss_exp /= (F_n1)
        ss_rep /= (F_n2)
        F_exp_data = ss_exp/ss_rep
        F_calc = f.ppf(confidence_level, F_n1, F_n2)
        if F_calc > F_exp_data:
            res =  0
        else:
            res = 1
        return res