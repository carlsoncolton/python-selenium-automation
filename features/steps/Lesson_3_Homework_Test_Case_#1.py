import time
from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")


@when("Click on cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    time.sleep(3)


@then("Verify cart empty icon is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
    assert 'Your cart is empty' in actual_text
    print('Test case passed')
