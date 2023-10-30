#works only of linux or git bash terminal

echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activating the environment"

source activate ./venv

echo [$(date)]: "installing the dev requirements"

pip install -r requirements.txt

echo [$(date)]: "END"