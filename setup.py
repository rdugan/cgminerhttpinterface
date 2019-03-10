from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cgminerhttpinterface',
      version='0.1.3',
      description='HTTP endpoint for CGMiner RPC conforming interfaces',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Systems Administration',
      ],
      keywords='cgminer sgminer mining api http monitor',
      url='http://github.com/rdugan/cgminerhttpinterface',
      author='rdugan',
      author_email='cgmhi-dev@mailnicks.org',
      license='Apache',
      packages=find_packages(),
      python_requires='>=3',
      entry_points={
          'console_scripts': ['chi-server=cgminerhttpinterface.command_line:start_server'],
      },
      include_package_data=True,
      zip_safe=False)
