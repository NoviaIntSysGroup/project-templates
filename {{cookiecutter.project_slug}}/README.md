# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug}}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![Coookiecutter - Novia Intelligent Systems Group](https://img.shields.io/badge/cookiecutter-Novia Intelligent Systems Group-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/NoviaIntSysGroup/project-templates)](https://github.com/NoviaIntSysGroup/project-templates)


---

**Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}})

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

**PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)

---

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.8+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
poetry run pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/main/docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github Pages page](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatting (`ruff format`), linters (e.g. `ruff` and `mypy`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
poetry run pre-commit install
```

Or if you want them to run only for each push:

```sh
poetry run pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
poetry run pre-commit run --all-files
```

---

## Using Poetry

To add a pythond package, for instance `requests`, run:

```sh
poetry add requests
```

To add a dev depencency, use the --dev flag:

```sh
poetry add gradio --dev
```

## Cruft
If you created this project with Cruft and want to update to the newest settings in the original template, run:

```sh
cruft update
```


This project was generated using the [project-templates](https://github.com/NoviaIntSysGroup/project-templates) template.


## Run demo

```sh
poetry run gradio demo.py
```