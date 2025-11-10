'''
  The setup.py files is an essential part of packaging and distributing python projects. It is used by setuptolls (or distutils in 
  older python versions) to define the configuration of your 
  project, such as its metadata, dependencies, and more'''
  
from setuptools import find_packages, setup # used to find __init__ file for finding package (scan through entire folder and try to get this one out)
from typing import List

def get_requirements()-> List[str]:
  """
  this function will return list of requirements
  """
  requirements_lst:List[str] = []
  try:
    with open('requirements.txt', 'r') as file:
      #Read lines from the file
      lines = file.readlines()
      #Process each line
      for line in lines:
        requirements = line.strip()
        #ignore empty lines and -e.
        if requirements and requirements!= '-e .':
          requirements_lst.append(requirements)
          
  except FileNotFoundError:
    print("requirements.txt not find")
    
  return requirements_lst

setup(
  name = "Network_Security",
  version='0.0.1',
  author='Aviral Mittal',
  author_email='aviralmittal0012@gmail.com',
  packages=find_packages(),
  install_requires = get_requirements()
)
