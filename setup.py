from setuptools import setup, find_namespace_packages

setup(name='noteworthy-botkit',
      url="https://noteworthy.tech",
      author_email="hi@decentralabs.io",
      version='0.0.3',
      license='AGPLv3',
      packages=find_namespace_packages(include=['noteworthy.*']),
      zip_safe=False,
      install_requires=[
        'matrix-nio==0.17.0',
        'requests==2.25.1',
        'Pillow==8.1.2'
      ]
     )
