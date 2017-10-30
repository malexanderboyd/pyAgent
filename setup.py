from setuptools import setup

setup(name='RequestAgent',
      version='1.0',
      description='A sample python agent to monitor a rest request',
      url='https://github.com/malexanderboyd/pyAgent',
      author='Alex Boyd',
      author_email='malexanderboyd@gmail.com',
      license='MIT',
      packages=[],
      install_requires=[
          'Flask',
          'pympler',
          'objgraph',
          'requests'
      ],
      zip_safe=False)