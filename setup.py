from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use .strip() instead of replace

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)  # Remove editable install line

    return requirements

setup(
    name="FaultDetection",
    version="0.0.1",
    author="ernee",
    author_email="er.neeteshkumar236656@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)
