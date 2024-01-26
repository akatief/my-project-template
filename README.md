
# UKP Project Template
[![Arxiv](https://img.shields.io/badge/Arxiv-YYMM.NNNNN-red?style=flat-square&logo=arxiv&logoColor=white)](https://put-here-your-paper.com)
[![Python Versions](https://img.shields.io/badge/Python-3.11-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/akatief/my-project-template)](https://opensource.org/licenses/Apache-2.0)
[![Build](https://github.com/akatief/my-project-template/actions/workflows/main.yml/badge.svg)](https://github.com/akatief/my-project-template/blob/main/.github/workflows/main.yml)

A low dependency and really simple to start project template for Python Projects.

### Getting Started

> **DO NOT CLONE OR FORK**

first, create a repository on the page by following the standard procedure, then
this template is to be pushed , or automatically 

1. Follow the standard procedure to create a repository on UKP Lab's GitHub and clone that one.
2. Download this template as a .zip by clicking on `Code > Download ZIP`.
3. Extract the zip and push it to the UKP Lab repository.
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. If you don't want automatic documentation generation, you can delete folder `docs` and file `.github\workflows\docs.yml`
5. If you don't want automatic testing, you can delete folder `tests` and file `.github\workflows\tests.yml`
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)

Click on **[Use this template](https://github.com/rochacbruno/python-project-template/generate)**

> **NOTE**: **WAIT** until first CI run on github actions before cloning your new project.

### What is included on this template?

- 🖼️ Templates for starting multiple application types:
  * **Basic low dependency** Python program (default) [use this template](https://github.com/rochacbruno/python-project-template/generate)
  * **Flask** with database, admin interface, restapi and authentication [use this template](https://github.com/rochacbruno/flask-project-template/generate).
  **or Run `make init` after cloning to generate a new project based on a template.**
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <my_project_template>` or `$ my_project_template` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  
> If you want to contribute to this template please open an [issue](https://github.com/rochacbruno/python-project-template/issues) or fork and send a PULL REQUEST.

[❤️ Sponsor this project](https://github.com/sponsors/rochacbruno/)

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# my_project_template

[![codecov](https://codecov.io/gh/akatief/my-project-template/branch/main/graph/badge.svg?token=my-project-template_token_here)](https://codecov.io/gh/akatief/my-project-template)
[![CI](https://github.com/akatief/my-project-template/actions/workflows/main.yml/badge.svg)](https://github.com/akatief/my-project-template/actions/workflows/main.yml)

Awesome my_project_template created by akatief

## Install it from PyPI

```bash
pip install my_project_template
```

## Usage

```py
from my_project_template import BaseClass
from my_project_template import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m my_project_template
#or
$ my_project_template
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
