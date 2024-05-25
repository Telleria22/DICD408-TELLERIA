#required libreries 
import pandas as pd 
import numpy as np

#extraction 
wine_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
wine_data = pd.read_csv(wine_url, header=None)

wine_quality_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data = pd. read_csv(wine_quality_url, sep=";")


#print(wine_data.head())
#print(wine_quality_data.head())

#trasformacion 
wine_data.columns = ['class', 'alcohol', 'malic acid', 'ash', 
                     'alcalinity of ash', 'magnesium', 'total phenols',
                     'flavonoids', 'nonflavonoid phenols', 'proanthocyanidins',
                     'color intensity', 'hue', 'OD280/OD315 of diluted wines',
                     'proline']
##converting class colum into categorical datatype
wine_data['class'] = wine_data['class'].astype('category')

## check  for any missing values in both datasets .
print(wine_data.isnull().sum())
print(wine_quality_data.isnull().sum())

##normalizing alcohol column in the wine_data using Min - Max normalization

wine_data['alcohol'] = (wine_data['alcohol'] - wine_data['alcohol'].min()/(wine_data['alcohol'].max() - wine_data['alcohol'].min()))


#loading 
##saving the transformed data as a cvs file (guardar los datos )
wine_data.to_csv('wine_dataset.csv', index = False)
wine_quality_data.to_csv('wine_quality_dataset.csv', index = False)
















