import numpy as np
import pandas as pd
from scipy.stats import f

class Experimental_Data:
    """Class Experimental_Data.
    
    Parameters:

    data : pd.DataFrames, where rows - experiments, columns - params (e.g. T, p etc.)
    params_names : list of str names of parameters
    experiments_names : list of str names of experiments
    """

    def __init__(self, data):
        self.__data = data
    
    @property
    def data(self):
        return self.__data
    
    def anova(self, param_name, target_param_name, confidence_level = 0.95):
        """Inputs: param_name etc 'T', target_param_name etc reaction yeld, experiments_names - 
        list of names of experiments. Return integetr 1 if observed dependence and 0 if not."""
        data = self.data
        data = data.sort_values(by = param_name)
        param_values = data[param_name].array
        target_param_values = data[target_param_name].array
        unical_param_vals = set(param_values)
        new_data = []
        for unical_param_val_num, param_val in enumerate(unical_param_vals):
            new_target = []
            ind_values = [val for val in param_values if val == param_val]
            for val_ind in ind_values:
                new_target.append(target_param_values[val_ind])
            new_data.append(new_target)
        new_data = np.array(new_data)

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