from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    # Function that returns a list of requirements from requirements.txt
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        



setup(
    name='facify',
    version='0.1.0',
    description='Facify: A Real-time face detection and recognition system',
    author='Rabel Mervin',
    author_email='rabelmervin@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    )