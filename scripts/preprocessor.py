from data_cleaner import DataCleaner
from util import Util
from logger import Logger
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
import numpy as np

class Preprocessor:
    def __init__(self) -> None:
        self.cleaner=DataCleaner()
        self.util=Util()
        self.logger = Logger("preprocessing.log").get_app_logger()
        self.logger.info("Initialized preprocessor object")

    def prepare(self,df):
        """
        Prepare the data for modeling by preprocessing
        """
        
        pipeline= Pipeline(steps=[
            ('format_dtype',FunctionTransformer(self.format_dtype,validate=False)),
            ('feature_encodder',FunctionTransformer(self.cleaner.feature_encodder,validate=False)),
            ('feature_engineering',FunctionTransformer(self.feature_engineering,validate=False)),
            ('standard_scaller',FunctionTransformer(self.cleaner.standard_scaler,validate=False)),
        ])

        return pipeline.fit_transform(df)
    
    def feature_engineering(self,df):
        
        df["Weekday"]=np.where(df["DayOfWeek"]<6, 1, 0)
        df["Weekend"]=np.where(df["DayOfWeek"]>5, 1, 0)

        return df
    
    def format_dtype(self,df):
        try:
            
            df = self.cleaner.convert_to_datetime(df,['Date'])

            df = self.cleaner.convert_to_int(df,['CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2SinceWeek','Promo2SinceYear','Store','DayOfWeek','Customers','Open','Promo','SchoolHoliday','Promo2'])

            df = self.cleaner.convert_to_float(df,['CompetitionDistance'])

            df = self.cleaner.convert_to_object(df,['StateHoliday','StoreType','Assortment','PromoInterval'])

            self.logger.info("Complete formating data types")

        except:
            self.logger.error("Unable to set data type")
        return df