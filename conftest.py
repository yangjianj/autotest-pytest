import pytest
from _pytest.runner import runtestprotocol
#测试夹具：函数名可作为测试函数参数传入，测试函数内部通过引用函数名来获得fixture对象
@pytest.fixture  #夹具函数注册标记
def my_demo():
    return [1,2,3,4]

def pytest_runtest_protocol(item,nextitem):
    reports = runtestprotocol(item,nextitem=nextitem)
    for re in reports:
        if re.when == 'call':
            print('\n%s------%s'%(item.name,re.outcome))