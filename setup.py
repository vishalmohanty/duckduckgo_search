from setuptools import setup
from vm_ddgsearch import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vm_ddgsearch",
    version=__version__,
    author="Vishal Mohanty",
    author_email="vishalmohanty97@gmail.com",
    description="Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishalmohanty/vm_ddgsearch",
    license="MIT",
    py_modules=["vm_ddgsearch"],
    install_requires=["requests>=2.27.1", "lxml>=4.7.1", "brotli>=1.0.9"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",  
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
