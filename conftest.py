import pytest
from playwright.sync_api import Browser, Page, sync_playwright
from pytest import Config

def pytest_addoption(parser):
    parser.addini("base_url", "base url for the application under test")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")

@pytest.fixture(scope="session")
def browser(pytestconfig):
    headless = pytestconfig.getoption("--headless", default=False)
    print("1")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
   
        
@pytest.fixture(scope="function")
def page(browser, base_url) -> Page:
    # 브라우저 컨텍스트 생성! 독립적인 환경을 만들어줘!
    context = browser.new_context()

    # 새로운 페이지(탭) 열기! 이제 이 페이지로 테스트를 시작할 수 있어!
    page = context.new_page()
    
    page.base_url = base_url
    
    print("conftest - base_url : ", base_url)

    # 여기 'yield'가 중요해! 이 'page' 객체를 테스트 함수한테 넘겨주는 거야!
    # yield 아래 코드는 테스트 함수 실행이 끝난 후에 실행돼!
    yield page # 테스트 함수가 여기서 page 객체를 받아서 테스트를 진행함!

    # 테스트 함수 실행이 모두 끝나면 정리 진행
    # 페이지, 컨텍스트 순서로 닫아주기
    page.close()
    context.close()