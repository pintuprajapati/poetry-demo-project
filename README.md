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
-    ### Add Dependencies
        - Add dependencies (general): `poetry add <package_name>` (ex: `poetry add requests`)
            - This will be added under `[tool.poetry.dependencies]` in `toml` file
        - Add dependencies (for development env only): `poetry add -D <<package_name>` (ex: `poetry add -D mypy`)
            - This will be added under `[tool.poetry.group.dev.dependencies]` in `toml` file

-    ### Remove Dependencies
        - Remove single dependency: `poetry remove <package_name>` (ex: `poetry remove requests`)
        - Remove multiple dependencies: `poetry remove <package1> <package2> …` (ex: `poetry remove requests numpy pandas`)
        - If you want to remove a development dependency (one installed with the `--dev` flag), use the same command: `poetry remove <dev_package_name>`
            - Poetry will detect whether the package is listed under `[tool.poetry.dependencies]` or `[tool.poetry.dev-dependencies]` in `pyproject.toml` and remove it accordingly.
        - Check Dependencies After Removal: `poetry show --tree`
        - Update the Lock File
            - Poetry automatically updates the `poetry.lock` file whenever you add or remove dependencies. You don’t need to manually update the lock file unless you want to refresh it with all current versions:
                - `poetry lock`



## PyPi Package
- To build a pypi package: `poetry build`
    - It will create a `dist` directory (you can either publish from terminal or manually. you can google it)

## Dependencies Tree
- To see what package is dependent on what packages (n tree like structure): `poetry show --tree`