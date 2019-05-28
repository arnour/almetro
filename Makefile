clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	rm -fr cover
	rm .coverage

setup:
	pip install -r requirements.txt
	pip install -r requirements_test.txt
	tox -r

tests:
	tox

install: clean
	pip install -e .

release:
	@rm -fr dist/*
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
