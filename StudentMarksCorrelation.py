import csv
import numpy as np

def getDataSource(dataPath):
    marks=[]
    attendance=[]
    
    with open(dataPath) as f:
        df = csv.DictReader(f)
        
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))
    return{
        "x": marks,
        "y": attendance
    }
    
def findCorrelation(dataSource):
    correlation= np.corrcoef(dataSource["x"], dataSource["y"])
    print("The correlation between the marks and number of days present is" , correlation[0,1])
    
def setup():
    dataPath = "StudentMarks.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    
setup()