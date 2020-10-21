from setuptools import setup, find_packages
import app


def parse_requirements_file(requirements_path):
    with open(requirements_path) as req_file:
        return req_file.read().strip().split('\n')


setup(
    name="epam-app",
    version=app.__version__,
    packages=['app'],
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'epam-app=app.server:main'
        ],
    },
    include_package_data=True,
    install_requires=parse_requirements_file('requirements.txt'),
    data_files=[('css', ['app/static/css/main.css']),
                ('templates', ['app/templates/404.html', 'app/templates/base.html', 'app/templates/index.html'])],
)
