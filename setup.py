from setuptools import setup, find_packages

setup(
    name="yolo_tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'ultralytics',
        'opencv-python-headless'
    ],
)