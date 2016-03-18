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
