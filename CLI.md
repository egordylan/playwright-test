**CLI - Command Line Interface**
pytest CLI commands documentation
https://docs.pytest.org/ -> 
click on Contents -> click on Usage and Invocations
https://docs.pytest.org/en/6.2.x/usage.html

**Reporter**
https://github.com/christiansandberg/pytest-reporter-html1

**Parellel run with pytest xdist**
pytest -n <NCPU>
exmpl: pytest -n 3

Stop at first failure:
 pytest -x

Allow max failures before stopping:
 pytest --maxfail=2

Run single test:
 pytest -k test_func_name

Run a single file:
 pytest test_file.py

Re-run last failed tests only:
 pytest --lf

Re-run all tests, starting with last failed:
 pytest --ff

You can combine CLI options together:
 pytest --ff -x -v

Reporting with pytest-reporter-html1:
 pytest --template=html1/index.html --report=report.html

pytest --maxfail=2 -m sanity --template=html1/index.html --report=sanity_report.html -n 3