import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csp-scan",
    version="1.0.0",
    packages=["csp_scan"],
    author="Marcin Szleszynski",
    author_email="mszlesz@gmail.com",
    description="Constructs strict Content-Security-Policy header after scanning all HTML files in a directory",
    entry_points = {
        'console_scripts':
        ['csp-scan=csp_scan.__main__:main']
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martinezpl/csp-scan",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.0",
)