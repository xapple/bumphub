from distutils.core import setup

setup(
      name             = 'bumphub',
      version          = '0.0.1',
      description      = 'Assign environment ontology (EnvO) terms to short DNA sequences',
      license          = 'MIT',
      url              = 'https://github.com/xapple/bumphub',
      download_url     = 'https://github.com/xapple/bumphub/tarball/0.0.1',
      author           = 'Lucas Sinclair',
      author_email     = 'lucas.sinclair@me.com',
      scripts          = ['bumphub/pybump', 'bumphub/sphinxhub'],
      install_requires = ['sh'],
      long_description = open('README.md').read(),
    )
