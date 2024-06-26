# setup.py

from setuptools import setup, find_packages

setup(
    name="Breamer Tasks",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "celery>=5.4.0",
        "redis>=5.0.7",
    ],
    author="Neel",
    author_email="neel@local.host",
    description="Celery tasks for dreamer.",
    url="https://github.com/neelkamal0310/breamer_tasks.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
