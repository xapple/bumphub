# -*- coding: utf8 -*-

"""
Shared helpers for bumphub scripts.
"""

# Built-in modules #
import os, argparse

# Internal modules #
from autopaths import Path

###############################################################################
def get_args(description):
    # Create a shell parser #
    parser = argparse.ArgumentParser(description=description)

    # Ask for the main argument #
    help_msg = "The name of the project to process."
    parser.add_argument("module", nargs='?', default=None, help=help_msg, type=str)

    # Optional testing mode
    parser.add_argument("--test", action='store_true')

    # Parse the shell arguments #
    args = parser.parse_args()
    path_or_name = args.module
    test_mode = args.test

    # We can accept module names, filesystem paths, or default to CWD #
    if path_or_name is None:
        base_dir = Path(os.getcwd())
        proj_name = base_dir.name
    elif '/' in path_or_name:
        base_dir = Path(path_or_name)
        proj_name = base_dir.name
    else:
        base_dir = Path("~/repos/%s/" % path_or_name)
        proj_name = path_or_name

    # The python code directory #
    code_dir = base_dir + proj_name + '/'

    # Packaging files #
    toml_path  = base_dir + 'pyproject.toml'

    # So let's confirm they exist #
    base_dir.must_exist()
    code_dir.must_exist()
    toml_path.must_exist()

    # Change directory #
    os.chdir(base_dir)

    return base_dir, proj_name, code_dir, toml_path, test_mode
