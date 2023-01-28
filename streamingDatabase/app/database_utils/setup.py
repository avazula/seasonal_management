from setuptools import setup

setup(
    name="database_utils",
    version="0.0.1",
    author="avazula",
    author_email="jain@hllseasonal.com",
    packages=["database_utils", "database_utils.test"],
    description="Database utilities",
    long_description=open("README.txt").read(),
    install_requires=["psycopg2==2.9.5", "pytest", "django-environ"],
)
