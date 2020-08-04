from setuptools import setup, find_packages

setup(name='matrixbz',
      url="https://decentralabs.io",
      author_email="hi@decentralabs.io",
      version='0.0.1',
      license='AGPLv3',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
        'matrix-nio==0.14.1',
        'requests==2.24.0',
        'Pillow==7.2.0'
      ]
     )
