from fabric.api import local

def test(module, pattern="*_test.py"):
    """Running all tests inside a module 

    This task not to run all tests inside `tests` folder,
    but we need to spesify which of test's module need to 
    run.
    """
    module_path = "tests/{}".format(module)
    local('python -m unittest discover {} {}'.format(module_path, pattern))
