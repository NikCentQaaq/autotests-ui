import pytest
import allure

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @allure.severity(Severity.NORMAL)
    @allure.title('Check displaying of empty courses list')
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

        allure.attach.file('index.html', attachment_type=allure.attachment_type.HTML)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Create course')
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
            estimated_time="2 weeks"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @allure.severity(Severity.CRITICAL)
    @allure.title('Edit course')
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage,
    ):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_form.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
            estimated_time="2 weeks"
        )
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.click_edit_course(index=0)

        create_course_page.create_course_form.fill(
            title="Playwright111",
            max_score="11100",
            min_score="110",
            description="Playwright111",
            estimated_time="2 weeks111"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright111",
            max_score="11100",
            min_score="110",
            estimated_time="2 weeks111"
        )







