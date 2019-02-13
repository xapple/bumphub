# `bumphub`
The project contains tools to automate package distribution and publishing.

#### `sphinxhub`
The first utility, `sphinxhub`, generates documentation for a python package using sphinx and uploads it to github pages

You can use it from the shell like this:

    $ sphinxhub seqenv

#### `pybump`
The second utility, `pybump`,  contains a script to automatically bump the version number of a module, add a tag, commit it, and finally upload the project to PyPI.

You can use it from the shell like this:

    $ pybump seqenv

## Uploading a package to PyPI

Before using this script your pacakge needs to be registered in PyPI. Follow these steps starting with your project repository. Let's say your project is named `demo`.

    cd ~/repos/demo
    git init
    git add *
    git add .gitignore
    git commit -m "First commit"

Now create a new empty repository on github, let's say your username is `user`. Then push to it:

    git remote add origin git@github.com:user/demo.git
    git push -u origin master

Upgrade the packages:

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