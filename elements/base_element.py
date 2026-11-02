import allure
from playwright.sync_api import Page, Locator, expect
from tools.logger import get_logger
from ui_coverage_tool import ActionType, SelectorType
from elements.ui_coverage import tracker


logger = get_logger('BASE_ELEMENT')



class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return 'base element'


    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)

        step = f'Getting locator with "data-test-id"="{locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)   # ЛОГИРОВАНИЕ
            # Возвращаем объект локатора
            return self.page.get_by_test_id(locator).nth(nth)  # Возможность выбрать элемент по индексу
                                     # по умолчанию =0, то есть, как обычно, выбирает первый



    # Локатор в виде XPATH строки для сбора покрытия
    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f'//*[@data-testid="{self.locator.format(**kwargs)}"][{nth + 1}]'


    def track_coverage(self, action_type: ActionType,  nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )





    def click(self, nth: int = 0, **kwargs):

        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            # "Лениво" инициализируем локатор
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            # Выполняем нажатие на элемент
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            # Инициализируем локатор "лениво"
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            # Проверяем, что элемент виден на странице
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)


    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking {self.type_of} "{self.name}" with text "{text}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)


