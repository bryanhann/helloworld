venv=./.venv
rm -rf ./build
rm -rf ./dist
rm -rf ./MANIFEST.in
rm -rf $venv
ls -a1
echo

venv=./.venv
[ -d $venv ] || python3 -m venv $venv
source $venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install check-manifest
check-manifest --create
python setup.py sdist bdist_wheel
pip install -e . .\[dev\]
#url: gitignore.io   choosealicence.com
pytest
