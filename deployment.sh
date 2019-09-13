echo Upgrading Build Tools
pip3 install --upgrade setuptools wheel

echo Upgrading publish Tools
pip3 install --upgrade twine

echo Builing package
rm -rf *.egg-info build dist
python3 setup.py sdist bdist_wheel

echo Uploading Package to PyPI
python3 -m twine upload dist/*
