import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert


@pytest.mark.usefixtures('setup')
class TestMain:
    @allure.feature('Интернет магазин')
    @allure.story('Тест главной страницы')
    @allure.title('Тест 1')
    def test1(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Переходит по ссылке Whats New'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/nav/ul/li[1]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[3]/div[1]/div[1]/strong').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == 'Compare Products', 'Ошибка!'


    @allure.feature('Интернет магазин')
    @allure.story('Тест выбора мужской одежды')
    @allure.title('Тест 2')
    def test2(self):
        with allure.step('Открывает ссылку MEN'):
            self.browser.get('https://magento.softwaretestingboard.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Переходит по ссылке'):
            self.browser.find_element(By.XPATH,'//*[@id="ui-id-5"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбор цвета'):
            self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-53"]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Тест сортировки')
    @allure.title('Тест 3')
    def test3(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает тип'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/select').send_keys('Product Name')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Тест выбора одежды')
    @allure.title('Тест 4')
    def test4(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/men/tops-men.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирается Cassius Sparking Tank'):
            element = self.browser.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        element = self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text
        assert element == 'Cassius Sparring Tank', 'Ошибка!'
    @allure.feature('Интернет магазин')
    @allure.story('Тест товаров для йоги')
    @allure.title('Тест 5')
    def test5(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/a/span/span[2]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Переход в категорию Tops мужской одежды')
    @allure.title('Тест 6')
    def test6(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/men.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH,'//*[@id="narrow-by-list2"]/dd/ol/li[1]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Переход в категорию Bottoms мужской одежды')
    @allure.title('Тест 7')
    def test7(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/men.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[2]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Переход в категорию Gear')
    @allure.title('Тест 8')
    def test8(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/men.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-6"]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Выбор рюкзака')
    @allure.title('Тест 9')
    def test9(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/gear.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[3]/div/div/ol/li[1]/div/a/span/span/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            element=self.browser.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text
        assert element == 'Fusion Backpack','Ошибка!'

    @allure.feature('Интернет магазин')
    @allure.story('Переход по ссылке Fitess Equipment')
    @allure.title('Тест 10')
    def test10(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/gear.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH,'//*[@id="narrow-by-list2"]/dd/ol/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[3]/div/a/span/span/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            element = self.browser.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text
        assert element == 'Harmony Lumaflex™ Strength Band Kit', 'Ошибка!'

    @allure.feature('Интернет магазин')
    @allure.story('Тест сортировки')
    @allure.title('Тест 11')
    def test11(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/gear/fitness-equipment.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="sorter"]').send_keys('Price')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Тест изменения списка товаров')
    @allure.title('Тест 12')
    def test12(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/gear/fitness-equipment.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="mode-list"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Тест выбора товара')
    @allure.title('Тест 13')
    def test13(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/gear/fitness-equipment.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/a/span/span/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Тест выбора женской одежды')
    @allure.title('Тест 14')
    def test14(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Переходит по ссылке Women'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-4"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбор цвета'):
            self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-50"]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Интернет магазин')
    @allure.story('Переход на ссылку контакты')
    @allure.title('Тест 15')
    def test15(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/women.html')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Переходит по ссылке Contact US'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[5]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        element = self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/span').text
        assert element == '1-800-403-8838', 'Ошибка!'