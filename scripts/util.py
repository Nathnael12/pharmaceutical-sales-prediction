import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dvc.api as dvc

class Util:
    
    def read_from_file(self,path):
        """
            Load data from a csv file
        """
        try:
            df = pd.read_csv(path)
            return df
        except FileNotFoundError:
            print("File not found.")
    def read_from_dvc(self,path,repo,rev):
        
        """
            Load data from a dvc storage
        """
        try:
            data_url = dvc.get_url(path=path,repo=repo,rev=rev)
            df =pd.read_csv(data_url)
            return df
        except Exception as e:
            print("Something went wrong!",e)