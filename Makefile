lint: clean
	@mypy sudoku_solver
	@flake8 sudoku_solver --append-config=flake8.solver.config.ini
	@flake8 tests --append-config=flake8.tests.config.ini

test: clean
	@poetry run pytest -s

clean:
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@find . -type d -name __pycache__ -prune -exec rm -rf {} \;
	@find . -type d -name .ipynb_checkpoints -prune -exec rm -rf {} \;

call:
	@poetry run python call.py