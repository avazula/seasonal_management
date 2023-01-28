from setuptools import setup

setup(
    name="models",
    version="0.0.1",
    author="avazula",
    author_email="jain@hllseasonal.com",
    packages=["seasonal_models", "seasonal_models.test"],
    description="Data models",
    long_description=open("README.txt").read(),
    # TODO: change this
    install_requires=["psycopg2==2.9.5", "pytest", "django-environ"],
)
