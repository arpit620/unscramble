
# gz compresses file by replacing the original one
gzip filename
gunzip filename


# zip file
zip file.zip file.txt
unzip file.zip

# To run pytest inside test folder
py.test                # To run all
py.test file.py        # To run specific file

# To run make files
make check
make test
make docs

#----------------------------------------------------------------#

### Upload a package to PyPI

# Step 1: Compile your package
python setup.py bdist_wheel

# Step 2: Make sure following is setup
pip install twine

# create a .pypirc file at HOME location
[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username = arpit625

# Step 3: Upload on pip
python -m twine upload dist/*


