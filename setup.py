from setuptools import find_packages,setup

from typing import List

hyphenr="-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()  # removes spaces, \n, \t, etc.
            if req and req != "-e .":
                requirements.append(req)
    return requirements

setup(
    name="mlproject1",
    version='0.0.1',
    author='Chhandos',
    author_email="chhandosxyz@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

