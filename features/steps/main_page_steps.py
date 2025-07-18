from behave import given, when, then

@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()




# @Given ("Open the main page")
# def open_main(context):
#     context.driver.get('https://soft.reelly.io')
#     sleep(2)