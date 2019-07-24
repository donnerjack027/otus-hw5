"""
pytest hooks
"""
import pytest


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    if report.when == 'call':
        report.test_metadata = 'whatever'
        report.stage_metadata = {
            'Test status': 'start of run'
        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'Test status': 'in progress'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'Test status': 'test finished'
        }
