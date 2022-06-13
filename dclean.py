import pandas as pd
import numpy as np

dev_group = {
  'Data scientist or machine learning specialist':'Data',
  'Scientist':'Academic',
  'Academic researcher':'Academic',
  'Data engineer':'Data',
  'Front-end developer':'Web Dev',
  'QA or test developer':'Service',
  'Designer':'Art',
  'Full-stack developer':'Web Dev',
  'Data or business analyst':'Business',
  'Back-end developer':'Web Dev',
  'Database administrator':'Admin',
  'Product manager':'Manager',
  'Marketing or sales professional':'Business',
  'Engineering manager':'Manager',
  'System administrator':'Admin',
  'Embedded applications or devices developer':'Embled Dev',
  'Mobile developer':'Mobile Dev',
  'Game or graphics developer':'Game Dev',
  'Desktop or enterprise applications developer':'Desktop Dev',
  'Educator':'Academic',
  'DevOps specialist':'Engineer',
  'Site reliability engineer':'Engineer'	,
  'Senior Executive (C-Suite/VP/etc.)':'Executive',
  'Consultant':'Service',
  'Cloud Engineer':'Engineer',
  'UX/UI Developer':'Web Dev',
  'Web Developer':'Web Dev',
  'IT Security':'Security',
  'Penetration tester':'Security',
  'Manager':'Manager',
  'IT Support':'Service',
  'Network Engineer':'Engineer',
  'Security Engineer':'Security',
  'Business Intelligence':'Business',
  'UI/UX Designer':'Art',
  'Human Resource':'Manager',
  'Robotic Software Engineer':'Engineer',
  'CTO':'Executive',
  'Director':'Executive',
  'CEO':'Executive',
  'Software engineer':'Engineer',
  'System Analyst':'Admin'
}

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

def group_freq(x):
  batch = x.split(', ')
  group = []
  for i in batch:
    group.append(dev_group[i])
    
  temp = pd.DataFrame(columns=['original','group'])
  temp['original'] = batch
  temp['group'] = group

  return temp['group'].value_counts().index[0]

def what_should_this_guy_be(x):
  # ls = ['Data','Academic','Web Dev','Service','Art','Business','Admin','Manager','Device Dev','Mobile Dev','Desktop Dev','Game Dev','Engineer','Executive','Security','Network']
  if 'Executive' in x:
    return 'Executive'
  if 'Front-end developer' in x or 'Back-end developer' in x or 'Full-stack developer' in x:
    if 'Desktop' in x:
      return 'Desktop Dev'
    elif 'Mobile' in x:
      return 'Mobile Dev'
    elif 'Embled' in x:
      return 'Embled Dev'
    elif 'Game' in x:
      return 'Game Dev'
    elif 'Web' in x:
      return 'Web Dev'
    else:
      return group_freq(x)
  else:
    return group_freq(x)
    

def wpos(x):
  if x != '':
    return what_should_this_guy_be(x)
  else:
    return 'Engineer'