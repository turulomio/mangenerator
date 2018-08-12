from mangenerator import __version__
from setuptools import setup, Command
from mangenerator import Man

import datetime
import gettext
import os
import site

class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
        os.chdir("doc")
        os.system("doxygen Doxyfile")
        os.system("rsync -avzP -e 'ssh -l turulomio' html/ frs.sourceforge.net:/home/users/t/tu/turulomio/userweb/htdocs/doxygen/mangenerator/ --delete-after")
        os.chdir("..")

class Uninstall(Command):
    description = "Uninstall installed files with install"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -Rf {}/mangenerator*".format(site.getsitepackages()[0]))
        os.system("rm /usr/share/locale/es/LC_MESSAGES/mangenerator.mo")

class Doc(Command):
    description = "Update man pages and translations"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        #es
        os.system("xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o locale/mangenerator.pot *.py mangenerator/*.py")
        os.system("msgmerge -N --no-wrap -U locale/es.po locale/mangenerator.pot")
        os.system("msgfmt -cv -o locale/es/LC_MESSAGES/mangenerator.mo locale/es.po")
    ########################################################################

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='mangenerator',
     version=__version__,
     description='Python module to generate man documentation',
     url='https://mangenerator.sourceforge.io/',
     long_description=long_description,
     long_description_content_type='text/markdown',
     classifiers=['Development Status :: 4 - Beta',
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Build Tools',
                  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                  'Programming Language :: Python :: 3',
                 ], 
     keywords='man generator',
     author='Turulomio',
     author_email='turulomio@yahoo.es',
     license='GPL-3',
     packages=['mangenerator'],
     data_files=[ ('/usr/share/locale/es/LC_MESSAGES/', ['locale/es/LC_MESSAGES/mangenerator.mo']),
                ], 
     cmdclass={'doxygen': Doxygen,
               'doc': Doc,
               'uninstall':Uninstall, 
              },
      zip_safe=False
)

