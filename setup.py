from setuptools import find_packages,setup

setup(
    name="DimondPricePrediction",
    version="0.0.1",
    author="vinayraj",
    author_email="vinay.raj@gmail.com",
    install_requires=["scikit-learn","pandas","numpy","seaborn","scipy"]
    packages=find_packages()
)