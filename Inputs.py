# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:45:35 2024

@author: louise.grenier
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dm4bem

start_date = '02-01 12:00:00'
end_date = '02-07 18:00:00'

start_date = '2000-' + start_date
end_date = '2000-' + end_date
print(f'{start_date} \tstart date')
print(f'{end_date} \tend date')