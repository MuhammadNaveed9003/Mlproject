from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements.
    """

    requirements = []

    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()

    requirements = [
        req.strip()
        for req in requirements
        if req.strip() and req.strip() != HYPEN_E_DOT
    ]

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="MuhammadNaveed",
    author_email="l259003@lhr.nu.edu.pk",
    packages=find_packages(),
    install_requires=get_requirements("Requirements.text")
)