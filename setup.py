from setuptools import setup

with open("README.md", "r") as f:
  long_description = f.read()

setup(name='gilbert-scss',
      version='0.0.1',
      description='A plugin for Gilbert to render content using libsass',
      long_description= long_description,
      url='https://github.com/Alysha-94/gilbert-scss',
      author='Alysha Iannetta',
      packages=['gilbert.plugins'],
      classifiers = [
          'Development Status :: 4 - Beta',
      ],
      keywords='gilbert',
      install_requires=[
          'libsass'
      ],
      include_package_data = True,
)