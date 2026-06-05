
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirement.txt','r')as file:
            lines=file.readlines()
        for line in lines:
            requirement=line.split()
            if requirement and requirement!= '-e .':
                requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")

setup(
name="Network Security",
version="0.0.1",
author="wania aijaz",
author_email="waniaaijaz896@gmail.com",
packages=find_packages(),
install_requires=get_requirements()

)