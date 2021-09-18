from setuptools import setup, find_packages

tests_require = [
    'pytest >= 3.7.4',
    'pytest-cov',
]

requires = [
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(name='ioet_mj_test',
      version='1.0',
      description='ioet application test',
      author='Manuel Japón',
      author_email='efrain.japon@gmail.com',
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      url='https://github.com/mjapon/acme-test',
      packages=find_packages()
      )
