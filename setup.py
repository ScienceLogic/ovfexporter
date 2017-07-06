#!/usr/bin/env python
from distutils.core import setup
import setuptools
setup(name='ovfexporter',
      version='1.0.0',
      description="Export a vCenter VM's vmdks and ovf descriptor to local file system",
      author='Douglas Rohde',
      author_email='drohde@sciencelogic.com',
      packages=['ovfexporter'],
      keywords='export vmdk vCenter vm, ami',
      url='https://github.com/ScienceLogic/ovfexporter/archive/1.0.0.zip',
      license="MIT",
      install_requires=[
          'pyvmomi',
          'pysphere',
      ],
      scripts=['bin/ovfexport'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          # Indicate who your project is intended for
          'Intended Audience :: Developers, Sys Admins',
          'Topic :: Other/Nonlisted Topic :: Export Tools',

          # Pick your license as you wish (should match "license" above)
          "License :: MIT License",

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.7',

      ]

      )
