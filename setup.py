from setuptools import setup,find_packages
from typing import List

#declaring variables for setup function

PROJECT_NAME="insurance-premium-predictor"
VERSION="0.0.3"
AUTHOR="Ankith Patil"
DESCRIPTION="This is a first FSDS Nov batch Internship Machine Learning Project"
PACKAGES=find_packages() #this finds all the folders where there is __init__ file and returns those folders name 
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """Description: This function is going to return list of requirement mentioned in
    requirements.txt file
    
    return This function is going to return a list which contains 
    the name of the libraries mentioned in requirements.txt file"""

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
