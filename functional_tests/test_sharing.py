from selenium import webdriver
from .base import FunctionalTest
from .list_page import ListPage
from .my_lists_page import MyListsPage


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
        list_page = ListPage(self).add_list_item('Get help')

        share_box = list_page.get_share_box()
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
        list_page.share_list_with('2mail@2example2.com')

        self.browser = second_user_browser
        MyListsPage(self).go_to_my_lists_page()

        self.browser.find_element_by_link_text('Get help').click()
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            '1mail@1example1.com'
        ))

        list_page.add_list_item('Hi User The First!')

        self.browser = first_user_browser
        self.browser.refresh()

        list_page.wait_for_row_in_list_table('Hi User The First!', 2)
