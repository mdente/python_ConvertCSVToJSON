import urllib.request  
from datetime import datetime
import pandas as pd
from pandas._libs.tslibs import timestamps

class ConvertCSVToJSON:
    def __init__(self,url,saveTo,separatorType):
        self.url = url
        self.saveTo = saveTo
        self.separatorType = separatorType
    def convert(self):
        cCSV = urllib.request.urlopen(self.url)
        csv_data = pd.read_csv(cCSV,sep = self.separatorType)
        csv_data.to_json(self.saveTo,orient= "records")


# Test 
now = datetime.now()
timestamp = str(datetime.timestamp(now))
convertNow = ConvertCSVToJSON("http://sistema.cenipa.aer.mil.br/cenipa/media/opendata/aeronave.csv",timestamp+".json",";")
convertNow.convert()
