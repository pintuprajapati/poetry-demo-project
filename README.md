# Poetry Guidance:

## Installation

- Install poetry: `pip install poetry`
- create project using poetry: `poetry new <projecct-name>`

## venv
- In-project Virtual Environment (Optional):
    - To create venv in the same project directory:
    - one time process: `poetry config virtualenvs.in-project true`
    - create venv: `poetry shell`

## Dependencies
- Add dependencies (general): `poetry add <package_name>` (ex: `poetry add requests`)
    - This will be added under `[tool.poetry.dependencies]` in `toml` file
- Add dependencies (for development env only): `poetry add -D <<package_name>` (ex: `poetry add -D mypy`)
    - This will be added under `[tool.poetry.group.dev.dependencies]` in `toml` file

## PyPi Package
- To build a pypi package: `poetry build`
    - It will create a `dist` directory (you can either publish from terminal or manually. you can google it)

## Dependencies Tree
- To see what package is dependent on what packages (n tree like structure): `poetry show --tree`