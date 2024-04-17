from setuptools import setup

setup(
    name="tljh-pangeo",
    version="0.1",
    entry_points={"tljh": ["pangeo = tljh_pangeo"]},
    py_modules=["tljh_pangeo"],
)

