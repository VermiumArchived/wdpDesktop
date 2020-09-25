import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatsdispic-zyner",
    version="0.0.1",
    author="Vermium Sifell, Temerold",
    author_email="support@vermium.se, support@temerold.se",
    description="Looks for Dis Pics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/zyner/whatsdispic/src/dev/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)