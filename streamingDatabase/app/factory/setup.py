from setuptools import setup

setup(
    name="factory",
    version="0.0.1",
    author="avazula",
    author_email="jain@hllseasonal.com",
    packages=["factory", "factory.test"],
    description="Object factory",
    long_description=open("README.txt").read(),
    # TODO: change this
    install_requires=["psycopg2==2.9.5", "pytest", "django-environ"],
)
