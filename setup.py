import os
from setuptools import setup, find_packages

about = {}
dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(dir, 'html_note', '__version__.py')) as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=about["title"],
    description=about["description"],
    long_description=readme,
    long_description_content_type="text/markdown",
    version=about["version"],
    author=about["author"],
    author_email=about["author_email"],
    url=about["url"],
    packages=find_packages(exclude=["test"]),
    package_data={'': ['html/base.html']},
    include_package_data=True,
    python_requires=">=3.11.*",
    install_requires=["markdown"],
    license=about["license"],
    zip_safe=True,
    entry_points={
        "console_scripts": ["html=html_note.entry_points:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    keywords=["package" "notes" "html" "python"]
)
