# from distutils.core import setup
from setuptools import setup, Extension

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'flaskinator',         
  packages = ['flaskinator'],   
  version = '0.1.3',      
  license='MIT',        
  description = 'Quick library to generate ready to use APIs for Flask environment',
  author = 'Divs',
  url = 'https://github.com/Divsatwork/flaskinator',
  download_url = 'https://github.com/Divsatwork/flaskinator/archive/v_0.1.2.tar.gz',
  keywords = ['Flask', 'Ready to use', 'API'],
  install_requires=[ ], #no dependencies
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'
)