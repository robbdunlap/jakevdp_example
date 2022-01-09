import os
import pandas as pd

fremont_data_url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# function to load the Fremont bike data - will download if it isn't already in the 
# data folder will also create the data folder if it doesn't already exist
def get_fremont_data(url=fremont_data_url, 
                    filename='data/Fremont.csv', 
                    force_download=False):
    """Download and cache the Fremont bike route traffic data. Pull data from the cache on rerun unless the "force_download"
       is True or the data doesn't exist in the specificied location.

    Parameters
    ----------
    url : string (optional)
        web location of the source data
    filename : string (optional)
        location to save the data after downloading
    force_download : bool (optional)
        if True, force downloading of the data 

    Returns
    -------
    data : pandas.DataFrame
        The Fremont bike route traffic data
    """
    
    if force_download or not os.path.exists(filename):
        data = pd.read_csv(URL, index_col='Date', parse_dates=True)
        data.columns = ['Total','East','West']
        if not os.path.exists('data'):
            os.mkdir('data')
        data.to_csv('data/Fremont.csv')
    else:
        data = pd.read_csv('data/Fremont.csv', index_col='Date', parse_dates=True)
    
    return data