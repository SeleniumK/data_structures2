from setuptools import setup


setup(
    name="data-structures2",
    description="Collection of Classic Data Structures",
    version=0.1,
    author=["Selena Flannery", "Norton Pengra"],
    license="MIT",
    py_modules=["bst"],
    install_requires=["future"],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
