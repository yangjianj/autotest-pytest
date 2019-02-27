import pytest
def pytest_collection_modifyitems(items):
    for item in items:
        print(item)
        if "interface" in item.nodeid:
            item.add_marker(pytest.mark.interface)
        elif "event" in item.nodeid:
            item.add_marker(pytest.mark.event)