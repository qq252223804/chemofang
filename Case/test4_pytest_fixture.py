'''
此py文件简单使用pytest 模块
实现 用例之间依赖注入
'''
import requests, json
import pytest


# @pytest.fixture()
# def first():
# 	# print("\n获取用户名")
# 	a = "yoyo"
# 	return a

# 默认也为scope="function"
# @pytest.fixture(scope="function")
# def sencond():
# 	# print("\n获取密码")
# 	b = "123456"
# 	return b
#
#
# def test_1(first):
# 	'''用例传fixture'''
# 	print("测试账号：%s" % first)
# 	assert first == "yoyo"
#
#


class tets_login():

    @classmethod
    def setup_class(cls):
        """ 这是一个class级别的setup函数，它会在这个测试类TestSohu里
                所有test执行之前，被调用一次.
                注意它是一个@classmethod
        """
        pass

    @classmethod
    def teardown_class(cls):
        pass

    # 如果多个用例只需调用一次fixture，那就可以设置为scope = "session"，并且写到conftest.py文件里
    # @pytest.fixture(scope="session")
    @pytest.fixture(scope="module")
    def test_cms_login(cls):
        """后台登陆:密码
    
        :return:cookie
        """
        url = 'http://192.168.31.172:8082/cms/login'
        datas = {"username": 18657738815, "password": 111111}
        res = requests.post(url, datas)
        assert res.json()['code'] == 200
        return res.cookies

    def test_shenqing_details(cls, test_cms_login):
        '''
        采销后台打开申请详情
        :return:
        '''
        print(test_cms_login)
        url = 'http://192.168.31.172:8082/cms/dealerCarEnquiry/getList?page=1&limit=20&keyword=&status=&carBrandId=&carSeriesId=&carInfoId=&startDate=&endDate='
        res = requests.get(url, cookies=test_cms_login)  # 用例传fixture中登陆返回额cookies
        print(res.json()['code'])
        assert res.json()['code'] == 200
        # print(json.loads(res.text))


# # pytest 传参数必须用params
@pytest.fixture(params=[1, 5, 3])
def test_data(request):
    return request.param


def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 2


if __name__ == "__main__":
    pytest.main(["-s", "test4_pytest_fixture.py"])
