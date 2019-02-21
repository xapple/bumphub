from distutils.core import setup

setup(
      name             = 'bumphub',
      version          = '1.0.2',
      description      = 'Tools for building doc and incrementing python package version numbers',
      long_description = open('README.md').read(),
      license          = 'MIT',
      url              = 'https://github.com/xapple/bumphub/',
      author           = 'Lucas Sinclair',
      author_email     = 'lucas.sinclair@me.com',
      install_requires = ['sh', 'pkgtools', 'python2-pythondialog'],
      scripts          = ['bumphub/pybump', 'bumphub/sphinxhub'],
      packages         = ['bumphub'],
    )