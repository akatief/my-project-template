# ukp_project_template
[![Arxiv](https://img.shields.io/badge/Arxiv-YYMM.NNNNN-red?style=flat-square&logo=arxiv&logoColor=white)](https://put-here-your-paper.com)
[![Python Versions](https://img.shields.io/badge/Python-3.11-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/akatief/my-project-template)](https://opensource.org/licenses/Apache-2.0)
[![CI](https://github.com/akatief/my-project-template/actions/workflows/main.yml/badge.svg)](https://github.com/akatief/my-project-template/actions/workflows/main.yml)

RANDOM STUFFFFF

> **Abstract:** This is a copy of my beautiful abstract. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Contact person: John Smith, XXXX@ukp.informatik.tu-darmstadt.de

https://www.ukp.tu-darmstadt.de/

https://www.tu-darmstadt.de/


Don't hesitate to send us an e-mail or report an issue, if something is broken (and it shouldn't be) or if you have further questions.


## Getting Started

> **DO NOT CLONE OR FORK**

If you want to set up this template:

1. Request a repository on UKP Lab's GitHub by following the standard procedure on the wiki. It will install the template directly. Alternatively, set it up in your personal GitHub account by clicking **[Use this template](https://github.com/rochacbruno/python-project-template/generate)**.
2. Wait until the first run of CI finishes. Github Actions will commit to your new repo with a "✅ Ready to clone and code" message.
3. Delete optional files: 
    - If you don't need automatic documentation generation, you can delete folder `docs` and file `.github\workflows\docs.yml`
    - If you don't want automatic testing, you can delete folder `tests` and file `.github\workflows\tests.yml`
4. Adapt anything else (for example this file) to your project. 
5. Prepare a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install .
```
5. Read the file [CONTRIBUTING.md](CONTRIBUTING.md) for more information about development

## Usage

### Using the classes
**(change this as needed!)**

This is how you can use classes inside `my_project_template`: 

```py
from my_project_template import BaseClass
from my_project_template import base_function

BaseClass().base_method()
base_function()
```
### Using scripts

This is how you can use `my_project_template` from command line:

```bash
$ python -m my_project_template
```

### Expected results

After running the experiments, you should expect the following results:

(Feel free to describe your expected results here...)

### Parameter description

* `x, --xxxx`
  * This parameter does something nice
...
* `z, --zzzz`
  * This parameter does something even nicer
  


## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Cite
Please use the following citation:

```
@InProceedings{smith:20xx:CONFERENCE_TITLE,
  author    = {Smith, John},
  title     = {My Paper Title},
  booktitle = {Proceedings of the 20XX Conference on XXXX},
  month     = mmm,
  year      = {20xx},
  address   = {Gotham City, USA},
  publisher = {Association for XXX},
  pages     = {XXXX--XXXX},
  url       = {http://xxxx.xxx}
}
```
> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 

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
