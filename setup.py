from setuptools import find_packages
from setuptools import setup

setup(
      name='EmployeeApp',
      version='1.0',
      description='App for managing employees',
      author='Jan Hernas',
      author_email='hernasj@wp.pl',
      url='https://github.com/jasiex01/employeeApp',
      packages=find_packages(include=['app', 'app.*']),
      package_data={'': ['Employee.db']},
      include_package_data=True,
      entry_points={
            'console_scripts': [
                  'app-cli=app.main:main',
            ],
      },
)