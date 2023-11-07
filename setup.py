from setuptools import find_packages,setup
from typing import List

HYPEN_E_DONT="-E ."
def get_requirements(file_path:str)->List[str]:
    '''  
    this function will return the list of requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_path.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DONT in requirements:
            requirements.remove(HYPEN_E_DONT)
            
        return requirements        

setup(
name="Studentperformanceprediction",
version="0.0.1",
author="Dennis",
author_email="denz.aviator@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)  