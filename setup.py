import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="TextAdventureGameApp"
    version="0.0.1",
    author="Alebachew Melaku",
    author_email="alebachewtegegne2017@yahoo.com",
    url="https://github.com/yourusername/yourproject",
    description="simple math game",
    long_description=The provides some math questions to test our knowledge,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
