from setuptools import find_packages,setup

setup(
    name = 'generator',
    version = '0.0.1',
    author = 'Dhruv Agarwal',
    author_email = 'agarwaldhruv221202@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPdf2"],
    packages = find_packages()
)