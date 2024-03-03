# html-note

A minimal python package for creating html notes with markdown

# Setup

```
python setup.py sdist bdist_wheel

# wheel should be located in dist/
python -m pip install path/to/your-package.whl
```

# Usage

This project uses the [Python-Markdown](https://pypi.org/project/Markdown/) parser which follows the [daringfireball](https://daringfireball.net/projects/markdown/basics) syntax.

```
html-note generate example.md
output: example.html
```