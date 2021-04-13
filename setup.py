from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    install_requires = requirements.read().split("\n")

setup(
    name='ais_service_discovery',
    version='0.2.0',
    author='Peak AI',
    author_email='infra-notifications@peak.ai',
    description='AIS service discovery package for python3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/peak-ai/ais-service-discovery-python',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    keywords='aws service-discovery ais lambda',
    install_requires=install_requires,
)
