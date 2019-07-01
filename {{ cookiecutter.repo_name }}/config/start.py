import os
import sys
import random
import warnings
import re
import string
import math
import numpy as np
import pandas as pd
from datetime import datetime
from IPython.display import HTML

# Hana
from pathlib import Path
from dotenv import load_dotenv
import sqlalchemy_hana
from sqlalchemy import create_engine
from dateutil.relativedelta import relativedelta

# My libraries
sys.path.insert(0, '/opt/play/rbb/src/')
import importlib
import useful_func as f

# Plotting Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import iplot, init_notebook_mode
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

# Initialisation
cf.go_offline(connected=True)
init_notebook_mode(connected=True)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
warnings.filterwarnings('ignore')
env_path = Path('/opt/play/config') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True);
engine = f.create_hana_engine('BDS')
init_vars = [n for n, v in globals().items()]

def delete_local_vars(exclude_vars, verbose=True):
    delete_vars = [n for n, v in globals().items()]
    default_vars = ['json', 'getsizeof', 'NamespaceMagics', '_jupyterlab_variableinspector_nms', '_jupyterlab_variableinspector_Jupyter', 'pyspark', 'tf', '_jupyterlab_variableinspector_getsizeof', '_jupyterlab_variableinspector_getshapeof', '_jupyterlab_variableinspector_getcontentof', '_jupyterlab_variableinspector_is_matrix', '_jupyterlab_variableinspector_dict_list', '_jupyterlab_variableinspector_getmatrixcontent', '_jupyterlab_variableinspector_default']
    exclude_vars = init_vars + exclude_vars + default_vars + ['exclude_vars', 'delete_vars', 'verbose', 'delete_local_vars', 'init_vars']
    delete_vars = [var for var in delete_vars if var not in exclude_vars]
    g = globals()
    for name in delete_vars:
        if name in g:
            del g[name]

    if verbose:
        print('deleted following: {}'.format(', '.join(delete_vars)))

