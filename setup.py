from distutils.core import setup

setup(
      name             = 'bumphub',
      version          = '1.2.0',
      description      = 'Tools for building doc and incrementing python package version numbers',
      long_description = open('README.md').read(),
      long_description_content_type = 'text/markdown',
      license          = 'MIT',
      url              = 'https://github.com/xapple/bumphub/',
      author           = 'Lucas Sinclair',
      author_email     = 'lucas.sinclair@me.com',
      install_requires = ['plumbing>=2.8.0', 'autopaths>=1.4.1',
                          'sh', 'rich', 'twine', 'pdoc', 'grayskull',
                          'conda-build'],
      scripts          = ['bumphub/pybump'],
    )