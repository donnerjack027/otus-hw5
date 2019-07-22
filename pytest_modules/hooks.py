"""
pytest hooks
"""


def pytest_addoption(parser):
    """
    addoption
    """
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")
    parser.addoption("--address", action="store",
                     default="http://192.168.110.60/opencart/admin/index.php?route=common/login",
                     help="Enter opencart url")
    parser.addoption("--timeout", action="store", default="3",
                     help="Enter page load timeout")
