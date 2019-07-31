from setuptools import setup

setup(name='gilbert-scss',
      version='0.0.1',
      description='A plugin for Gilbert to render content using libsass',
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
)