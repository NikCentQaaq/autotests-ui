import re

from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from dataclasses import dataclass


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        self.course_view = CourseViewComponent(page)
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')
        self.empty_view = EmptyViewComponent(page, 'courses-list')


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

        # БЫЛО ДО КОМПОНЕНТА
        # expect(self.empty_view_icon).to_be_visible()
        # expect(self.empty_view_title).to_be_visible()
        # expect(self.empty_view_title).to_have_text('There is no results')
        #
        # expect(self.empty_view_description).to_be_visible()
        # expect(self.empty_view_description).to_have_text(
        #     'Results from the load test pipeline will be displayed here'
        # )

    # def check_visible_create_course_button(self):
    #     expect(self.create_course_button).to_be_visible()
    #
    # def click_create_course_button(self):
    #     self.create_course_button.click()

    """
               ВСЕ ЭТО ЗАМЕНЕНО PageComponent !!!!   
                      методы Компонента будут использоваться напрямую в Тестах!!!
    """
    # # параметры через ДатаКласс
    # def check_visible_course_card(self, params: CheckVisibleCourseCardParams):
    #     expect(self.course_image.nth(params.index)).to_be_visible()
    #
    #     expect(self.course_title.nth(params.index)).to_be_visible()
    #     expect(self.course_title.nth(params.index)).to_have_text(params.title)
    #
    #     expect(self.course_max_score_text.nth(params.index)).to_be_visible()
    #     expect(self.course_max_score_text.nth(params.index)).to_have_text(f"Max score: {params.max_score}")
    #
    #     expect(self.course_min_score_text.nth(params.index)).to_be_visible()
    #     expect(self.course_min_score_text.nth(params.index)).to_have_text(f"Min score: {params.min_score}")
    #
    #     expect(self.course_estimated_time_text.nth(params.index)).to_be_visible()
    #     expect(self.course_estimated_time_text.nth(params.index)).to_have_text(
    #         f"Estimated time: {params.estimated_time}"
    #     )
    #
    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_item.nth(index).click()


    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()
    #
    #     expect(self.course_delete_menu_item.nth(index)).to_be_visible()
    #     self.course_delete_menu_item.nth(index).click()
    #     self.check_current_url(re.compile('.*/#/courses/.*'))