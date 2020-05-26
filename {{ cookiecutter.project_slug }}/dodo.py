# https://github.com/pydoit/doit

"""
Build Automation Tasks

1. Codecoverage
2. Run tests
3. Build and publish on pypi
4. Run pylint
5. Build docs / website
6. clean directories
7. Spell checker
8. Subtasks
9. dot dependency grapoh generation

init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
"""

DOIT_CONFIG = {
    'backend': 'json',
    'dep_file': 'doit-db.json',
    'verbosity': 2,
}


def task_freeze():
    """ pip freeze | tee requirements.txt """
    cmd = 'pip freeze | tee requirements.txt'
    return {
        'actions': [cmd],
    }

def task_develop():
    """ python setup.py develop """
    cmd = 'python setup.py develop'
    return {
        'actions': [cmd],
    }

def task_checker():
    """ Lint: pylint src """
    return {
        'actions': ["pylint src"],
        # 'file_dep': ["sample.py"],
    }

def task_python_hello():
    """ Python action task hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["hello.txt"],
        }