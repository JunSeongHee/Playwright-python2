import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_Login(page: Page, base_url):
    print("\n 로그인 성공 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    login_page.login()
    print("로그인 성공 테스트 완료!")