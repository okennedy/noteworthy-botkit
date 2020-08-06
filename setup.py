from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='matrixbz',
      url="https://decentralabs.io",
      author_email="hi@decentralabs.io",
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='0.0.2',
      license='AGPLv3',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
        'matrix-nio==0.14.1',
        'requests==2.24.0',
        'Pillow==7.2.0'
      ]
     )
