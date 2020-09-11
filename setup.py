import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riskrate-data",
    version="0.0.1",
    author="Andrei Gorbulin",
    author_email="andrei@riskrate.io",
    description="Riskrate Data client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riskrate/riskrate-data-python",
    package_dir={'': 'riskrate_data'},
    packages=setuptools.find_packages(
        where='src', exclude=['generate_schema.py']
    ),
    install_requires=['websocket-client>=0.57.0', 'sgqlc>=11.0'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
