import allure
from allure_commons.types import Severity
from selene import browser, have, be, by


def test_github_find_repo_issue_by_number_with_allure_decorator_steps():
    allure.dynamic.tag("homework")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.epic("QA.GURU course")
    allure.dynamic.feature("Allure reports")
    allure.dynamic.story("Allure decorator steps with dynamic labels")
    allure.dynamic.link("https://github.com", name="Testing")
    open_main_page()
    search_for_repository('webremake/wrm_selene_python_hw_7')
    go_to_repository('webremake/wrm_selene_python_hw_7')
    open_tab_issues()
    should_see_issue_with_number('#2')


@allure.step("открываем https://github.com/")
def open_main_page():
    browser.open('/')


@allure.step("ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element('[name=q]').should(be.clickable).type(repo).press_enter()


@allure.step("переходим в репозиторий по ссылке {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).should(be.clickable).click()


@allure.step("переходим в таб Issue")
def open_tab_issues():
    browser.element('#issues-tab').should(be.clickable).click()


@allure.step("проверяем наличие issue с номером {number}")
def should_see_issue_with_number(number):
    assert browser.element('.opened-by').should(have.text(number))
