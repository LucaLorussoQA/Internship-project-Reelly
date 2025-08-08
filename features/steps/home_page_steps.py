from time import sleep

from behave import given, when, then


@when('Click on Off plan at the left side menu')
def off_plan_tab(context):
    context.app.home_page.off_plan_tab()


@when('Click on off plan at bottom left menu')
def off_plan_mobile_tab(context):
    context.app.home_page.off_plan_mobile_tab()