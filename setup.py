from distutils.core import setup

from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='z.entry',  # 包名
      version='1.0.1',  # 版本号
      description='A decorator for autorun main func',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='z.houbin',
      author_email='z.houbin@foxmail.com',
      install_requires=[],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
