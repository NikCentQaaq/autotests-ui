# from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки
#
# ## Запуск Playwright в синхронном режиме
# with sync_playwright() as playwright:
#     # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
#     browser = playwright.chromium.launch(headless=False)
#     pages = browser.new_page()  # Создаем новую страницу
#
#     # Переходим на страницу авторизации
#     pages.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#     # Находим поле "Email" и заполняем его
#     email_input = pages.locator('//div[@data-testid="login-form-email-input"]//div//input')
#     email_input.fill("user.name@gmail.com")
#
#     # Находим поле "Password" и заполняем его
#     password_input = pages.locator('//div[@data-testid="login-form-password-input"]//div//input')
#     password_input.fill("password")
#
#     # Находим кнопку "Login" и кликаем на нее
#     login_button = pages.locator('//button[@data-testid="login-pages-login-button"]')
#     login_button.click()
#
#     # Проверяем, что появилось сообщение об ошибке
#     wrong_email_or_password_alert = pages.locator('//div[@data-testid="login-pages-wrong-email-or-password-alert"]')
#     expect(wrong_email_or_password_alert).to_be_visible()  # Проверяем видимость элемента
#     expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")  # Проверяем текст
# 
#     # Пауза на 5 секунд, чтобы увидеть результат
#     pages.wait_for_timeout(5000)


from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Login
    login_button = page.get_by_test_id('login-pages-login-button')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = page.get_by_test_id('login-pages-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)