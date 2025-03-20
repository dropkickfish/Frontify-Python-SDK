from setuptools import setup, find_packages

setup(
    name='frontify',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pydantic',
        'httpx',
    ],
)