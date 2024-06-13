from setuptools import setup, find_packages

setup(
    name="forensic_imaging_tool",
    version="1.0.0",
    description="A forensic imaging tool with a GUI using PyQt5",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5",
    ],
    entry_points={
        "console_scripts": [
            "forensic_imaging_tool=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
