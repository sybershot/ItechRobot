from robot.api.deco import keyword


@keyword(name='Save page screenshot')
def save_page_screenshot(page, file_name):
    page.save_screenshot(file_name)
