from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger('BASE_PAGE')


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект pages атрибуту класса

    # Метод для открытия ссылок
    def visit(self, url: str):
        step = f'Opening the URL "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    # Метод для перезагрузки страницы
    def reload(self):
        step = f'Reloading page with URL "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='networkidle')

    # Метод для проверки url
    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)