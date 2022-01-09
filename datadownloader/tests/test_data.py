from datadownloader.data import get_fremont_data
import pandas as pd

def test_fremont_data():
    
    data = get_fremont_data()
    
    # without the "all" command, the "data.columns ==" will return an array
    # of boolean values. "all" sums the booleans.
    assert all(data.columns == ['Total', 'East', 'West'])
    assert(isinstance(data.index, pd.DatetimeIndex))