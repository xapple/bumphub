# `bumphub` version 1.3.1

Scripts to automate the distribution and packaging of Python modules on **PyPI** and **conda**.

This repo provides two CLI tools:

- **`pybump`**: bump versions + regenerate docs + git tag/push + build + upload to PyPI.
- **`anacondabump`**: generate a conda recipe + build + upload to anaconda channel.

> Note: these tools assume a fairly opinionated workflow (git repo, importable package, specific file layouts).

## `pybump`

The first utility, `pybump`, contains a script to automatically publish a
package on PyPI. More specifically, the following steps are carried out:

* Bump the version number of a python module (in `__init__.py`, in `setup.py` or `pyproject.toml`, and in `README.md`).
* Regenerate the documentation with `pdoc`.
* Commit these changes with git.
* Add a git tag with the new version number to the latest commit.
* Push these changes upstream.
* Build the package.
* Upload the package to PyPI.
* Bump the version number again.
* Commit these changes with git.


### Dependencies

Python packages used by the scripts include:

* `plumbing`
* `autopaths`
* `sh`
* `build`
* `twine`
* `pdoc`

### Required executables on `$PATH`

* `gsed`
* `twine`
* `pdoc`
* `git`

On macOS, `gsed` is provided by GNU sed:

    $ brew install gnu-sed

You can use it from the shell like this:

    $ pybump myproject

You can also pass a filesystem path, or omit the argument to use the current working directory:

    $ pybump /path/to/myproject
    $ cd /path/to/myproject && pybump

Command line options are:

* `--test` to upload to `testpypi` instead of the real PyPI.
* `--infinite` to keep incrementing the minor version number and never increment the major version number.

See https://packaging.python.org/guides/using-testpypi/ for the test option.

To get the dependencies, you can use:

    $ conda env create -f environment.yml

### Behavior and assumptions

- **Version source**: `pybump` imports your module and reads `module.__version__`. Your package must be importable from the repo root.
- **File edits**: it updates `yourpkg/__init__.py`, plus `setup.py` and/or `pyproject.toml` if present, plus the `README.md` line matching ` version X.Y.Z`.
- **Docs**: it runs `pdoc --output-dir docs/ yourpkg/` and stages `docs/`.
- **Release artifact**: it uploads **only** `dist/*.tar.gz` (sdist) via `twine` (not wheels).
- **Dev bump**: after uploading, it bumps again to a “dev” version, but the final “back to dev” commit/push is currently commented out in the script.
- **Safety**: it does not do much validation (clean working tree, missing credentials, etc.). Run on a clean repo and ensure PyPI credentials are configured for `twine`.


## `anacondabump`

The second utility, `anacondabump`, contains a script to do the same thing by uploading to an anaconda channel.

You can use it from the shell like this:

    $ anacondabump myproject

To use this script you first need to install `conda` and some utilities (see next section).

These executables are required on the `$PATH`:

* `rattler-build`
* `pyrattler-recipe-autogen`

> Note: the current script is hard-coded to upload to owner/channel `xapple`. If you want to publish to a different owner/channel you’ll need to edit `anacondabump` (or send a PR to make it configurable).

To get the dependencies, you can use:

    $ conda env create -f environment.yml



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

    python -m build

Test installation locally:

    uv venv test_env
    source ./test_env/bin/activate
    uv pip install dist/*.whl
    python -c "import myproject"

Clean up:

    deactivate
    rm -rf test_env

Upload the universal tar:

    twine upload dist/*.tar.gz

Or if you prefer the more version specific wheel:

    twine upload dist/*.whl

Or you can upload both of course.

    twine upload dist/*

Clean up:

    rm -rf *.egg-info
    rm -rf build
    rm -rf dist

Additional resources can [be found here](https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi).


## Uploading a package to anaconda manually

Resources on this topic can [be found here](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html).

### Setup `conda` on macOS

To set up `conda` on macOS do the following:

    $ brew install miniconda
    $ conda init "$(basename "${SHELL}")"
    # Restart your shell after `conda init` (or source your shell rc file).
    $ conda env create -f environment.yml
    $ conda activate bump

You also need your anaconda credentials to be recorded by running the command:

    $ anaconda login

Don't forget that you have to log into anaconda.org and not anaconda.com

In the future, we might improve the script by publishing the packages to conda forge.

Interesting blog article about this:

https://blog.gishub.org/how-to-publish-a-python-package-on-conda-forge
