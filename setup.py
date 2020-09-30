import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riskrate-data",
    version="0.0.6",
    author="Arnor Nolen",
    author_email="andrei@riskrate.io",
    description="Riskrate Data client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riskrate/riskrate-data-python",
    license="MIT",
    packages=setuptools.find_packages(exclude=['generate_schema.py']),
    install_requires=['websocket-client>=0.57.0', 'sgqlc>=11.0'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
