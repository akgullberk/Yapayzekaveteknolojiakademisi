# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:03:34 2025

@author: berka
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veri = pd.read_csv('veriler.csv')
boy = veri[['boy']]
print(boy)
boykilo = veri[['boy','kilo']]
print(boykilo)
