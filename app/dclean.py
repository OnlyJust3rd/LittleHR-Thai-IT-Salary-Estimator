import pandas as pd
import numpy as np


def edu(x):
  if 'Bachelor' in x or 'Certificate' in x:
    return 1
  if 'Master' in x:
    return 2
  if 'Doctoral' in x:
    return 2
  return 0

def employ(x):
  if 'Full-time' in x or 'Freelance' in x:
    return 1
  if 'Part-time' in x:
    return 0
  return 1

def orgsize(x):
  if 'Just me' in x or '10 to 19' in x or '2 to 9' in x:
    return 0
  if '20 to 99' in x:
    return 1
  if '100 to 999' in x:
    return 2
  if '1,000 to 9,999' in x:
    return 3
  if '10,000 or more':
    return 4
  return x

def get_in(x):
  jobs = []
  substring = ''
  iscollecting = False
  for s in x:
    if iscollecting:
      if s == ')':
        jobs.append(substring)
        substring = ''
        iscollecting = False
      else: substring += s

    if s == '(':
      iscollecting = True
  return jobs[0]

def wplace(x):
  xstr = get_in(x)
  if xstr == 'Bangkok' or xstr == 'Nonthaburi' or xstr == 'Samut Prakan' or xstr == 'Pathum Thani' or xstr == 'Nakhon Pathom' or xstr == 'Samut Sakhon':
    return 1
  else:
    return 0