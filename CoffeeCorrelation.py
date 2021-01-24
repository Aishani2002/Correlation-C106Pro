import csv
import numpy as np

def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    
    with open(dataPath) as f:
        df = csv.DictReader(f)
        
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{
        "x": coffee,
        "y": sleep
    }
    
def findCorrelation(dataSource):
    correlation= np.corrcoef(dataSource["x"], dataSource["y"])
    print("The correlation between amount of coffee and amount of sleep is" , correlation[0,1])
    
def setup():
    dataPath = "Coffee.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    
setup()