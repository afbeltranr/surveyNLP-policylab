from setuptools import setup, find_packages

setup(
    name="surveyNLP-policylab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "bertopic",
        "sentence-transformers"
    ],
    author="afbeltranr",
    description="NLP analysis for survey data",
    python_requires=">=3.8",
)
