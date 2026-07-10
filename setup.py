# from setuptools import find_packages,setup
# from typing import List
# HYPEN_E_DOT = "-e ."

# def get_requirements(file_path:str)-> List[str]:
#   '''
# this function returns the list of requirements
#   '''
#   requirements=[]
#   with open(file_path) as file_obj :
#     requirements = file_obj.readlines()
#     requirements=[req.replace("\n","")for req in requirements]

#     if HYPEN_E_DOT in requirements :
#       requirements.remove(HYPEN_E_DOT)
#   return requirements

    
# setup(
#     name= "ML_project",
#     version="0.0.1",
#     author = "sahil",
#     author_email= "jangrasahil2024@gmail.com",
#     packages= find_packages(),
#     install_requires=get_requirements("requirements.txt")

# )
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    print(requirements)

    return requirements

setup(
    name="ML_project",
    version="0.0.1",
    author="sahil",
    author_email="jangrasahil2024@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
