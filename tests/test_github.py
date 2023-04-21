from selene import browser, have, be


def test_github_find_repo_issue_by_number(browser_control):
    """
    открываем https://github.com/
    в строку поиска вводим `/webremake/wrm_selene_python_hw_7`
    нажимаем Enter
    на открывшейся странице клакаем на первую ссыдку c текстом `webremake/wrm_selene_python_hw_7`
    кликаем на таб `Issues`
    проверяем что в списке есть issue с номером `#2`
    """
    browser.open('/')
    browser.element('[name=q]').should(be.clickable).type('webremake/wrm_selene_python_hw_7').press_enter()
    browser.element('[href="/webremake/wrm_selene_python_hw_7"]').should(be.clickable).click()
    browser.element('#issues-tab').should(be.clickable).click()
    assert browser.element('.opened-by').should(have.text('#2'))
