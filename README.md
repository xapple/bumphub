# `bumphub` version 1.2.0

The project contains scripts to automate distribution and packaging of python modules on PyPI and conda.

## `pybump`

The first utility, `pybump`, contains a script to automatically publish a package on PyPI.
More specifically the following steps are carried out:

* Bump the version number of a python module (in `__init__.py`, in `setup.py` and `README.md`).
* Regenerate the documentation with `pdoc3`.
* Commit these changes with git.
* Add a git tag with the new version number to the latest commit.
* Push these changes upstream.
* Build the package.
* Upload the package to PyPI.
* Bump the version number again.
* Commit these changes with git.

These other python packages are dependencies:

* `plumbing`
* `autopaths`
* `sh`

These executables are required on the `$PATH`:

* `gsed`
* `twine`
* `pdoc`

You can use it from the shell like this:

    $ pybump myproject

Command line options are:

* `--test` to upload to `testpypi` instead of the real PyPI.
* `--infinite` to keep incrementing the minor version number and never increment the major version number.

See https://packaging.python.org/guides/using-testpypi/ for the test option.


## `anacondabump`

The second utility, `anacondabump`, contains a script to automatically retrieve a package that was previously uploaded to PyPI, and upload an exact copy on a personal anaconda channel.

You can use it from the shell like this:

    $ anacondabump myproject

To use this script you first need to install `conda` and some utilities (see next section).


## Setup `conda` on macOS

To set up `conda` on macOS do the following:

    $ brew install miniconda
    $ conda init "$(basename "${SHELL}")"
    $ mv ~/.bash_profile ~/.conda/conda_init.sh
    $ source ~/.conda/conda_init.sh
    $ conda install conda-build
    $ conda install anaconda-client

You also need your anaconda credentials to be recorded by running the command:

    $ anaconda login

Interesting blog article containing possible improvements to this script:

https://blog.gishub.org/how-to-publish-a-python-package-on-conda-forge


## Uploading a package to PyPI manually

If you want to do the steps manually instead, follow this guide. Let's say your project is named `myproject`.

    cd ~/repos/myproject
    git init
    git add *
    git add .gitignore
    git commit -m "First commit"

Now create a new empty repository on GitHub, let's say your username is `bob`. Then push to it:

    git remote add origin git@github.com:bob/myproject.git
    git push -u origin master

Upgrade the setuptools, and the wheel packages:

    pip install --user --upgrade setuptools wheel

Build a wheel:

    python setup.py sdist bdist_wheel

Test installation locally:

    virtualenv test_env
    source ./test_env/bin/activate
    pip install dist/myproject-1.0.0-py2-none-any.whl
    python -c "import myproject"

Clean up:

    deactivate
    rm -rf test_env

Upload the universal tar:

    twine upload dist/*.tar.gz

Or if you prefer the version specific wheel:

    twine upload dist/*.whl

Clean up:

    rm -rf *.egg-info
    rm -rf build
    rm -rf dist

Additional resources can [be found here](https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi).


## Uploading a package to anaconda manually

Resources on this topic can [be found here](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html).