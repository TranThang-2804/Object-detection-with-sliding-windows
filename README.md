### data set: https://universe.roboflow.com/hva/schoolllll/dataset/1#

# Project instruction:
## 1. install environment prequisites
### pipenv is python package dependency management
> run ```pip install pipenv```

### venv is python virtual environment
> run ```pip install virtualenv```

## 2. setup environment
### Create virtual environment
> run ```virtualenv venv```

### select the environment in VScode
<img src="./readme images/VScodeSetup.png" alt="Alt text" title="Setup VScode to use venv interpreter">

## 3. Get into the venv
> run ```source ./venv/bin/activate```

### to exit venv
> run ```deactivate```

<img src="./readme images/Successful.png" alt="Alt text" title="Successful get into the venv">

## 4. Install python package
> run ```pipenv install```

## 5. Run detection
> run ```python main.py --image [path/to/image]```

The result will be stored in folder "runs"