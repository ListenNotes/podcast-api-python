import os
from codecs import open
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fp:
    long_description = fp.read()

version_contents = {}

with open(
    os.path.join(here, "listennotes", "version.py"), encoding="utf-8"
) as f:
    exec(f.read(), version_contents)

setup(
    name="podcast-api",
    version=version_contents.get("VERSION", "1.0.0"),
    description="Python bindings for the Listen Notes Podcast API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Listen Notes, Inc.",
    author_email="hello@listennotes.com",
    url="https://github.com/listennotes/podcast-api-python",
    license="MIT",
    keywords="listen notes podcast api",
    packages=["listennotes", "examples"],
    zip_safe=False,
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        "setuptools>=41.0.1",
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Tracker": (
            "https://github.com/listennotes/" "podcast-api-python/issues"
        ),
        "Documentation": "https://www.listennotes.com/api/docs/",
        "Source Code": "https://github.com/listennotes/podcast-api-python/",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
