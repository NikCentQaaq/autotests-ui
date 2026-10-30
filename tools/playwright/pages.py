import allure
from playwright.sync_api import Page, Playwright
from config import settings, Browser
from tools.playwright.mock import mock_static_resources


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None

) -> Page:
    # Динамически получаем нужный браузер
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(), #все ссылки будут начинаться с базовой url
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)  #МОК отключение загрузки статических ресурсов

    yield page

    trace_path = settings.tracing_dir.joinpath(
        f'{test_name}_{browser_type.value}.zip'
    )
    context.tracing.stop(path=trace_path)

    video_path = page.video.path()
    context.close()

    allure.attach.file(trace_path, name='trace', extension='zip')
    allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)

    browser.close()




