import  pytest
import time
class Test1():
    @pytest.mark.webtest
    def test_web(self):
        print(time.localtime())
        time.sleep(5)

        print(11111)

    @pytest.mark.webtest1
    def test_web1(self):
        print(time.localtime())
        time.sleep(6)

        print(2222)

    def test_webtmp2(self,my_demo):
        mylist=my_demo
        print(mylist)
        print(time.localtime())
        print(22333)

if __name__ == '__main__':
    #pytest.main(['-v','-n 3','-m webtest or webtest1','--html=./output/report_v_test.html','--junit-xml=./output/report_v_test.xml','--result-log=./output/testlog.log'])
    pytest.main(['-v','-k web or http','-n 3','--cov-report=html','--cov=D:/yangjian/project/pytest_pro', '--tb=long', '--html=./output/report_v_test.html',
                  '--junit-xml=./output/report_v_test.xml', '--result-log=./output/testlog.log'])