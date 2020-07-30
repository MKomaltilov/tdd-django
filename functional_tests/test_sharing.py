from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass


class SharingTest(FunctionalTest):
    def test_can_share_a_list_with_another_user(self):
        self.create_pre_authenticated_session('1mail@1example1.com')
        first_user_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(first_user_browser))

        second_user_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(second_user_browser))
        self.browser = second_user_browser
        self.create_pre_authenticated_session('2mail@2example2.com')

        self.browser = first_user_browser
        self.browser.get(self.live_server_url)
        self.add_list_item('Get help')

        share_box = self.browser.find_element_by_css_selector(
            'input[name="sharee"]'
        )
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
