import os
from setuptools import setup

def get_data_files():

  data_files = []
  for pardir, subdirs, dirfiles in os.walk('data'):
    data_files.append((os.path.join('share/lace', pardir),
        [os.path.join(pardir, f) for f in dirfiles]))

  return data_files  
  


setup(
  data_files = get_data_files() 
)
