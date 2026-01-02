import numpy as np
from sklearn.linear_model import LinearRegression

class Experiment_Predictor:
    """Class Experiment_Predictor.
    
    Parameters:

    exp_data : obj Experimental_Data
    individual_params : list of floats
    coefs : list of floats predict coefficients
    """

    def __init__(self, exp_data, target_param_name, params_names = "all", iteraction_account = 0):
        exp_data = exp_data.data
        params_names_list = exp_data.columns
        params = exp_data.drop(target_param_name, axis = 1)
        params.insert(0, "Free member", 1).to_numpy()
        target_param = exp_data.iloc[params_names_list.index(target_param_name)].to_numpy()

        coefs = np.linalg.inv(params.T@params)@params.T@target_param
        coefs = [coef for coef in coefs[0]]

        self.__params_names = params_names
        self.__target_param_name = target_param_name
        self.__coefs = coefs

    @property
    def params_names(self):
        return self.__params_names
    
    @property
    def target_param_name(self):
        return self.__target_param_name

    @property
    def coefs(self):
        return self.__coefs
    
    def predict(self, params):
        """Input list of floats params, return float predict value."""
        coefs = self.coefs

    def save_model(self, path = "model.txt"):
        params_names = self.params_names
        coefs = self.coefs
        with open(path, "w") as model_file:
            lines = [f"Parameters of model to predict {self.target_param_name}:\n\n"]
            for param_ind, param in enumerate(params_names):
                lines.append(f'{param}    {coefs[param_ind]}\n')
            model_file.writelines(lines)
        return len(lines)