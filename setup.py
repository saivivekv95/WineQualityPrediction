import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
__version__="0.0.0"

REPO_NAME = "WineQualityPrediction"
AUTHOR_USER_NAME = "VIVEK"
SRC_REPO= "WinQualityPrediction"
AUTHOR_EMAIL = "saivivekv95@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="python package for mlapp",
    url=f"https://github.com/saivivekv95/WineQualityPrediction",
    project_url = {"Bug Tracker":f"https://github.com/saivivekv95/WineQualityPrediction/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)