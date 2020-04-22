#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:09:57 2020

@author: vigneshshenbagarajan
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = '~/Users/vigneshshenbagarajan/Documents/Work/projects/ds_salary_pred/chromedriver'

df = gs.get_jobs('data scientist',10, False, path, 15)

#df.to_csv('glassdoor_jobs.csv', index = False)


