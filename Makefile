install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 hexlet_code

check:
	poetry run flake8
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml
