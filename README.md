![Tests](https://github.com/TristynKahrs/TestsBase/actions/workflows/tests.yml/badge.svg)

# TestBase
A base project for testing with pytest

---

## Testing
### Usage
- mypy src
- flake8 src
- pytest
- tox

### pyproject.toml
investigate this config
*addopts* infers package name from src, change to match

### setup.cfg
investigate this config 
*install_requires* infers requirements from requirements.txt  
*packages* infers package name from src, change to match
*[options.package_data]* uses package name, change to match

### ./tests/
test_*.py contains the tests themselves  
/conftests.py contains fixtures for the tests *fixtures may be removed if not needed*  

---

## Packages
### requirements.txt
include numpy and pandas for example, but can be removed if not needed.

### requirements_dev.txt
includes flake8, tox, pytest, pytest-cov, mypy for testing and linting

---

*Be sure to alter header link above to refer to the correct project repository*