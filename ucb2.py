#required libreries 
import pandas as pd 
import numpy as np

#extraction 
wine_url = '/workspaces/DICD408-TELLERIA/dailyCalories_merged.csv'
wine_data = pd.read_csv(wine_url, header=None)

wine_quality_url = "/workspaces/DICD408-TELLERIA/dailyCalories_merged.csv"
wine_quality_data = pd. read_csv(wine_quality_url, sep=";")


print(wine_data.head())
print(wine_quality_data.head())

#trasformacion 

##

#loading 
##saving the transformed data as a cvs file (guardar los datos )
wine_data.to_csv('wine_dataset.csv', index = False)
wine_quality_data.to_csv('wine_quality_dataset.csv', index = False)
















