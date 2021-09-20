import pickle, os

final_model = pickle.load(open(os.path.join("models", "xgb_final.sav"), 'rb'))

from azureml.core import Workspace
ws = Workspace.from_config(path = os.path.join("..", "config", "config.json"))