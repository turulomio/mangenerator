from setuptools import setup
from mangenerator import __version__

setup(name='mangenerator',
      version=__version__,
      description='Python module to generate man documentation',
      url='https://mangenerator.sourceforge.io/',
      author='Turulomio',
      author_email='turulomio@yahoo.es',
      license='GPL-3',
      packages=['mangenerator'],
      zip_safe=False)
