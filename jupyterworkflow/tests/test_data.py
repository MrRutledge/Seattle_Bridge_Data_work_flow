from jupyterworkflow.data import get_data
import pandas as pd

def test_f_data():
     data = get_data()
     assert all(data.columns == ['West', 'East', 'Total'])
     assert isinstance(data.index, pd.DatetimeIndex)
