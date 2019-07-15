"""
pytest hooks
"""


def pytest_addoption(parser):
    """
    addoption - test url
    """
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")
    parser.addoption("--address", action="store", default="http://192.168.110.60/",
                     help="Enter opencart url")
