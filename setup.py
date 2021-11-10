from setuptools import setup, find_packages

name = "video_creator"
version = "0.0.1"

setup(
    name=name,
    version=version,
    author="mogeko kumarramesh454 cupofocha Morristt chesionyaya Mashhood555",
    description="Use Python to multiple videos in one and simple syncronization. ",
    url="https://github.com/SDM-2021-16-SpongeBob/video_creator",
    packages=find_packages(),

    install_requires=[
        "opencv-python>=4.5.4.58",
        "numpy>=1.21.4"
    ],

    tests_require=[],

    extras_require={
        "lint": [
            "pylint>=2.11.1"
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
