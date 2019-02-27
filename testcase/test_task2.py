import  pytest
import time
class Test1():
    @pytest.mark.webtest
    def test_tmp(self):
        print(time.localtime())
        time.sleep(5)
        print(11111)

    @pytest.mark.webtest1
    def test_http1(self):
        print(time.localtime())
        time.sleep(4)
        print(2222)

    def test_web2(self):
        print(time.localtime())
        print(22333)

if __name__ == '__main__':
    pytest.main(['-v','-m webtest or webtest1','--html=./output/report_v_test.html','--junit-xml=./output/report_v_test.xml','--result-log=./output/testlog.log'])