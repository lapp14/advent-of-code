# advent-of-code

https://adventofcode.com/2023

## Setup
Set up the venv with `python3 -m venv venv` Activate venv with `source venv/bin/activate` Verify python version after activation with `python --version`

List packages with `pip list` Install packages with `python -m pip install -U <package>`

Write required dependencies to `requirements.txt` using `pip freeze > requirements.txt` Install dependencies from `requirements.txt` using `pip install -r requirements.txt`

## Creating tests
- Install pytest with `pip install pytest`
- Create tests folder and create `__init__.py`
- Create a `test_unit.py` file to store the tests
- Tests and test files must be functions prefixed with `test_`
- The `assert` keyword is available without imports
- Create a `test_assertions` function to check the length of an empty list, or something trivial just for now to verify that everythings working
- Run `pytest` to see our single test pass