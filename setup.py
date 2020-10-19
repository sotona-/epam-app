from setuptools import setup, find_packages
import app


def parse_requirements_file(requirements_path):
    with open(requirements_path) as req_file:
        return req_file.read().strip().split('\n')


setup(
    name="epam-app",
    version=app.__version__,
    packages=find_packages(exclude=('tests', 'tests.*', 'build', 'dist', 'env')),
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'epam-app=app.server:main'
        ],
    },
    install_requires=parse_requirements_file('requirements.txt'),
)
