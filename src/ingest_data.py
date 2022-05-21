## we're going to start with location data, as that's the most interesting to me.
'''
1. ingest location json and convert into dataframe
2. determine list of metrics interested in tracking
    i. number of new locations by time series
    ii. distance traveled by time series
    iii. look into classifications - what metadata does dataset have? can we slice accordingly?
    iv. create a "DAG" (basically files for each manipulation, all ran on a final file in bash script)
    v. once DAG is built (maybe storing to local SQL database), dash can be created using those tables
    


'''

import pandas as pd
import json

import sys

