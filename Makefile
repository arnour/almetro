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

dist:
	python setup.py sdist
	cp -f dist/almetro-0.1.0.tar.gz /Users/arnour.sabino/DockerVolumes/jupyter/almetro-0.1.1.tar.gz