# `bumphub` version 1.0.3
The project contains tools to automate package distribution and publishing.

## `sphinxhub`
The first utility, `sphinxhub`, generates documentation for a python package using sphinx and uploads it to github `gh_pages` branch of the repository.

You can use it from the shell like this:

    $ sphinxhub demo

## `pybump`
The second utility, `pybump`,  contains a script to automatically bump the version number of a python module, add a git tag, commit it, and finally upload the project to PyPI.

You can use it from the shell like this:

    $ pybump demo

## Uploading a package to PyPI

Before using this script your package needs to already be registered in PyPI. Follow these steps starting with your project repository. Let's say your project is named `demo`.

    cd ~/repos/demo
    git init
    git add *
    git add .gitignore
    git commit -m "First commit"

Now create a new empty repository on github, let's say your username is `bob`. Then push to it:

    git remote add origin git@github.com:bob/demo.git
    git push -u origin master

Upgrade the setuptools and the wheel packages:

    pip install --user --upgrade setuptools wheel

Build a wheel:

    python setup.py sdist bdist_wheel

Test installation locally:

    virtualenv test_env
    source ./test_env/bin/activate
    pip install dist/demo-1.0.0-py2-none-any.whl
    python -c "import demo"

Clean up:

    deactivate
    rm -rf test_env

Upload it:

    twine upload dist/*.whl

Clean up:

    rm -rf *.egg-info
    rm -rf build
    rm -rf dist
