echo Upgrading pip
python3 -m ensurepip --upgrade

echo Upgrading Build Tools
python3 -m pip install --user --upgrade setuptools wheel twine

echo Builing package
python3 setup.py sdist bdist_wheel

echo Uploading Package to PyPI
python3 -m twine upload dist/*
