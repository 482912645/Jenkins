import time
import allure
import pytest


@allure.epic('食方Windows AI插件')
@allure.feature('激活')
class Test01:
    @allure.description('jenkins测试')
    def test_01(self):
        pass

    def test_02(self):
        pass

    def test_03(self):
        pass

if __name__ == '__main__':
    pytest.main(['-vs','test01.py'])