from playwright.sync_api import Page

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
    #
    # def check_visible_create_course_title(self):
    #     expect(self.create_course_title).to_be_visible()
    #     expect(self.create_course_title).to_have_text('Create course')
    #
    # def click_create_course_button(self):
    #     self.create_course_button.click()
    #
    # def check_visible_create_course_button(self):
    #     expect(self.create_course_button).to_be_visible()
    #
    # def check_disabled_create_course_button(self):
    #     expect(self.create_course_button).to_be_disabled()
    #
    # def check_visible_create_course_form(
    #         self,
    #         title: str,
    #         estimated_time: str,
    #         description: str,
    #         max_score: str,
    #         min_score: str
    # ):
    #     expect(self.create_course_title_input).to_be_visible()
    #     expect(self.create_course_title_input).to_have_value(title)
    #
    #     expect(self.create_course_estimated_time_input).to_be_visible()
    #     expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
    #
    #     expect(self.create_course_description_textarea).to_be_visible()
    #     expect(self.create_course_description_textarea).to_have_value(description)
    #
    #     expect(self.create_course_max_score_input).to_be_visible()
    #     expect(self.create_course_max_score_input).to_have_value(max_score)
    #
    #     expect(self.create_course_min_score_input).to_be_visible()
    #     expect(self.create_course_min_score_input).to_have_value(min_score)
    #
    # def fill_create_course_form(
    #         self,
    #         title: str,
    #         estimated_time: str,
    #         description: str,
    #         max_score: str,
    #         min_score: str
    # ):
    #     self.create_course_title_input.fill(title)
    #     expect(self.create_course_title_input).to_have_value(title)
    #
    #     self.create_course_estimated_time_input.fill(estimated_time)
    #     expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
    #
    #     self.create_course_description_textarea.fill(description)
    #     expect(self.create_course_description_textarea).to_have_value(description)
    #
    #     self.create_course_max_score_input.fill(max_score)
    #     expect(self.create_course_max_score_input).to_have_value(max_score)
    #
    #     self.create_course_min_score_input.fill(min_score)
    #     expect(self.create_course_min_score_input).to_have_value(min_score)
    #
    # def check_visible_exercises_title(self):
    #     expect(self.exercises_title).to_be_visible()
    #     expect(self.exercises_title).to_have_text('Exercises')
    #
    # def check_visible_create_exercise_button(self):
    #     expect(self.create_exercise_button).to_be_visible()
    #
    # def click_create_exercise_button(self):
    #     self.create_exercise_button.click()
    #
    # def check_visible_exercises_empty_view(self):
    #     self.exercises_empty_view.check_visible(
    #         title='There is no exercises',
    #         description='Click on "Create exercise" button to create new exercise'
    #     )