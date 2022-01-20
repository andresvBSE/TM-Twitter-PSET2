import datetime
from datetime import datetime
import dateutil
from dateutil import tz
import pytz

import numpy as np
import pandas as pd


def date_time(df, date_column, replace, place):
    df[date_column] = pd.to_datetime( df[date_column], format="%Y-%m-%dT%H:%M:%S.000Z")
    if replace == 'yes':
        df[date_column] = df[date_column].dt.tz_localize(pytz.utc) 
        df[date_column] = df[date_column].dt.tz_convert(place)
      # Tell the datetime object that it's in UTC time zone since # datetime objects are 'naive' by default
    elif replace=='no' :
        df['date_new'] = df[date_column].dt.tz_localize(pytz.utc) 
        df['date_new'] = df['date_new'].dt.tz_convert(place)