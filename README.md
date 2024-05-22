# King Dee-Dee-I

![](./frontend/src/assets/dedede-big.png)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/PM5XoJ?referralCode=9XJNhY)

## Setup

### Set up DB

You will need the following commands:

- `python`
- `sqlite3`
- `wget`
- `printf`
- `gzip`

... if you have a bash terminal open, it should hopefully work.

Then just run `python setup-database.py` and grab a coffee, it'll download the script,
install it into the sqlite database, and remove all the temporary downloaded files.

Your database will be available at `test.db`.

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

### Working on the frontend

- Run the flask server (see "Run Application")
- cd to `frontend/` and run `npm run serve`.
