# King Dee-Dee-I

![](./frontend/src/assets/dedede-big.png)

## Setup

### Set up DB

**TODO**

### Install Backend Dependencies

- create a new .venv with `python -m venv .venv`
- [activate](https://docs.python.org/3/library/venv.html#how-venvs-work) the venv
- install `pipenv` using `pip install pipenv`
- install all packages using `pipenv install`
- install pre-commit hooks by using `pre-commit install`

### Install Frontend Dependencies

- cd to `frontend/`
- `npm install`
- `npm run build`

### Run Application

From the root of the repo, run `flask run --host=0.0.0.0 --port=8000 --debug`.

This starts up flask, which is configured to serve the vue files.
