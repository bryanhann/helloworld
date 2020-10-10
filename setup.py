from setuptools import setup

def slurp(path):
    with open(path, 'r') as fd:
        return fd.read()

# versioning should be as relaxed as possible for install_requires
install_requires = [
    "blessings ~= 1.7",
]

# versioning should be as strict as possible for extras_requir
extras_require = {
    "dev" : [
        "pytest>=3.7",
    ],
}

classifiers=[
    "Programming Language :: Python :: 3"       ,
    "Programming Language :: Python :: 3.6"     ,
    "Programming Language :: Python :: 3.7"     ,
    "License :: OSI Approved :: ..."            ,
    "Operating System :: OS Independent"        ,
]

setup(
    name='helloworld'
    , version='0.1.1'
    , description='Say hello!'
    , long_description=slurp('README.md')
    , long_description_content_type='text/markdown'
    , py_modules=["helloworld"]
    , package_dir={'': 'src'}
    , classifiers=classifiers
    , install_requires=install_requires
    , extras_require=extras_require
    # sdist would like the following:
    , url="https:/github.com/bryanhann/helloworld"
    , author="Bryan Hann"
    , author_email="bhann@pobox.com"
)
