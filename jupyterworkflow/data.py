import os
from urllib.request import urlretrieve

import pandas as pd
 
Fremont_URL = 'https://data.seattle.gov/api/views/mdbt-9ykn/rows.csv?accessType=DOWNLOAD'

def get_data(filename ='Fremont.csv', url = Fremont_URL, force_download= False):
    """Download and cache the fremont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
         web location of the data
     force_download : bool (optional)
         if True, force redownload of data
   Returns
   =======
   data : pandas.DataFrame
        The Fremont bridge data 
   """
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    data= pd.read_csv('Fremont.csv',index_col='Date', parse_dates =True)
    data.columns = ['West' , 'East']
    data['Total'] = data['West'] + data['East']
    return data