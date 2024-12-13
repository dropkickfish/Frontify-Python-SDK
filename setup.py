from setuptools import setup, find_packages

setup(
    name='frontify',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pydantic',
        'httpx',
    ],
)