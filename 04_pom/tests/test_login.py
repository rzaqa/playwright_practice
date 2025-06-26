import pytest
import allure

@allure.feature('Authorisation')
@allure.story('Login Feature')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Authorisation with correct credentials')
@allure.description("Check that user is able to authenticate using a valid username and valid password")
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Open authorisation page'):
        login_page.navigate()
    with allure.step('Fill in the form with a correct credentials'):
        login_page.login(username, password)
    with allure.step('Check the Welcome message is displayed'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")

@allure.feature('Authorisation')
@allure.story('Login Feature')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Authorisation with a wrong credentials')
@allure.description("Check that user is NOT able to authenticate using a invalid username and invalid password")
def test_login_failure(login_page):
    with allure.step('Open authorisation page'):
        login_page.navigate()
    with allure.step('Fill in the form with a wrong credentials'):
        login_page.login('invalid_user', 'invalid_password')
    # with allure.step('Url has"t changed'):
    #     assert login_page.url == 'https://zimaev.github.io/pom/'
    with allure.step('The errors is displayed - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'



