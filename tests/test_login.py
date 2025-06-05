import pytest
import subprocess
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_Login(page: Page, base_url):
    print("\n 로그인 성공 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    login_page.login()
    print("로그인 성공 테스트 완료!")
'''
def test_Login_fail(page: Page, base_url):
    print("\n 로그인 실패 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # 로그인 시도 (실패를 위해 잘못된 ID와 PW 사용)
    page.fill("#id", "wrong_user")
    page.fill("#pw", "wrong_password")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "로그인 실패 메시지가 표시되지 않았습니다."
    
    print("로그인 실패 테스트 완료!")
    
def test_Login_with_empty_credentials(page: Page, base_url):
    print("\n 빈 자격 증명으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # 빈 ID와 PW로 로그인 시도
    page.fill("#id", "")
    page.fill("#pw", "")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "빈 자격 증명으로 로그인 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("빈 자격 증명으로 로그인 테스트 완료!")   
    
def test_Login_with_invalid_credentials(page: Page, base_url):
    print("\n 잘못된 자격 증명으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # 잘못된 ID와 PW로 로그인 시도
    page.fill("#id", "invalid_user")
    page.fill("#pw", "invalid_password")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "잘못된 자격 증명으로 로그인 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("잘못된 자격 증명으로 로그인 테스트 완료!")       
    
def test_Login_with_special_characters(page: Page, base_url):
    print("\n 특수 문자 포함 자격 증명으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # 특수 문자가 포함된 ID와 PW로 로그인 시도
    page.fill("#id", "user!@#")
    page.fill("#pw", "pass$%^")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "특수 문자가 포함된 자격 증명으로 로그인 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("특수 문자 포함 자격 증명으로 로그인 테스트 완료!")   
    
def test_Login_with_long_credentials(page: Page, base_url):
    print("\n 긴 자격 증명으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # 너무 긴 ID와 PW로 로그인 시도
    long_id = "a" * 256  # 예: 256자 길이의 ID
    long_pw = "b" * 256  # 예: 256자 길이의 PW
    page.fill("#id", long_id)
    page.fill("#pw", long_pw)
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "긴 자격 증명으로 로그인 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("긴 자격 증명으로 로그인 테스트 완료!")       

def test_Login_with_sql_injection(page: Page, base_url):
    print("\n SQL 인젝션 시도 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # SQL 인젝션 시도
    page.fill("#id", "' OR '1'='1")
    page.fill("#pw", "' OR '1'='1")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "SQL 인젝션 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("SQL 인젝션 시도 테스트 완료!")   
    
def test_Login_with_xss_attack(page: Page, base_url):
    print("\n XSS 공격 시도 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    login_page.goto_login_page()
    
    # XSS 공격 시도
    page.fill("#id", "<script>alert('XSS')</script>")
    page.fill("#pw", "<script>alert('XSS')</script>")
    page.click("#log\\.login")
    
    # 로그인 실패 메시지 확인
    error_message = page.locator(".error-message")  # 실제 에러 메시지의 CSS 선택자에 맞게 수정 필요
    assert error_message.is_visible(), "XSS 공격 시도 시 에러 메시지가 표시되지 않았습니다."
    
    print("XSS 공격 시도 테스트 완료!") 
    
    
def test_Login_with_empty_page(page: Page, base_url):       
    print("\n 빈 페이지에서 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 빈 페이지로 이동
    page.goto(base_url)
    
    # 로그인 시도 (빈 페이지에서 로그인 버튼 클릭)
    try:
        page.click("#log\\.login")
        assert False, "빈 페이지에서 로그인 버튼을 클릭했지만 에러가 발생하지 않았습니다."
    except Exception as e:
        print(f"빈 페이지에서 로그인 시도 시 에러 발생: {e}")
    
    print("빈 페이지에서 로그인 테스트 완료!")      
    
def test_Login_with_invalid_url(page: Page, base_url):
    print("\n 잘못된 URL에서 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 잘못된 URL로 이동
    invalid_url = f"{base_url}/invalid"
    page.goto(invalid_url)
    
    # 로그인 시도 (잘못된 URL에서 로그인 버튼 클릭)
    try:
        page.click("#log\\.login")
        assert False, "잘못된 URL에서 로그인 버튼을 클릭했지만 에러가 발생하지 않았습니다."
    except Exception as e:
        print(f"잘못된 URL에서 로그인 시도 시 에러 발생: {e}")
    
    print("잘못된 URL에서 로그인 테스트 완료!") 
    
    
def test_Login_with_network_issue(page: Page, base_url):
    print("\n 네트워크 문제로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 네트워크 문제를 시뮬레이션하기 위해 페이지를 로드하지 않음
    try:
        page.goto(base_url, wait_until="domcontentloaded", timeout=5000)  # 5초 후 타임아웃
        assert False, "네트워크 문제로 페이지를 로드하지 못했지만 에러가 발생하지 않았습니다."
    except Exception as e:
        print(f"네트워크 문제로 로그인 시도 시 에러 발생: {e}")
    
    print("네트워크 문제로 로그인 테스트 완료!")
    
    
def test_Login_with_browser_error(page: Page, base_url):
    print("\n 브라우저 오류로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 브라우저 오류를 시뮬레이션하기 위해 페이지를 강제로 닫음
    try:
        page.close()
        page.goto(base_url)  # 페이지를 다시 열려고 시도
        assert False, "브라우저 오류로 페이지를 로드하지 못했지만 에러가 발생하지 않았습니다."
    except Exception as e:
        print(f"브라우저 오류로 로그인 시도 시 에러 발생: {e}")
    
    print("브라우저 오류로 로그인 테스트 완료!")
    
def test_Login_with_page_timeout(page: Page, base_url):
    print("\n 페이지 타임아웃으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 페이지 로드 타임아웃을 설정하고 페이지를 로드하지 않음
    try:
        page.goto(base_url, timeout=1000)  # 1초 후 타임아웃
        assert False, "페이지 타임아웃이 발생했지만 에러가 발생하지 않았습니다."
    except Exception as e:
        print(f"페이지 타임아웃으로 로그인 시도 시 에러 발생: {e}")
    
    print("페이지 타임아웃으로 로그인 테스트 완료!")
    
def test_Login_with_page_reload(page: Page, base_url):
    print("\n 페이지 리로드로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 페이지를 로드하고 리로드 시도
    login_page.goto_login_page()
    
    try:
        page.reload()  # 페이지를 리로드
        print("페이지가 성공적으로 리로드되었습니다.")
    except Exception as e:
        assert False, f"페이지 리로드 중 에러 발생: {e}"
    
    print("페이지 리로드로 로그인 테스트 완료!")
    
def test_Login_with_page_navigation(page: Page, base_url):
    print("\n 페이지 탐색으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 다른 페이지로 탐색
    try:
        page.goto(f"{base_url}/another-page")  # 다른 페이지로 이동
        print("다른 페이지로 성공적으로 탐색되었습니다.")
    except Exception as e:
        assert False, f"페이지 탐색 중 에러 발생: {e}"
    
    print("페이지 탐색으로 로그인 테스트 완료!")
    
    
def test_Login_with_page_screenshot(page: Page, base_url):
    print("\n 페이지 스크린샷으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 페이지 스크린샷 찍기
    try:
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"페이지 스크린샷이 {screenshot_path}에 저장되었습니다.")
    except Exception as e:
        assert False, f"페이지 스크린샷 중 에러 발생: {e}"
    
    print("페이지 스크린샷으로 로그인 테스트 완료!")
    
def test_Login_with_page_console_log(page: Page, base_url):
    print("\n 페이지 콘솔 로그로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 페이지 콘솔 로그 출력
    try:
        page.on("console", lambda msg: print(f"콘솔 메시지: {msg.type} - {msg.text}"))
        page.evaluate("console.log('테스트용 콘솔 메시지')")
    except Exception as e:
        assert False, f"페이지 콘솔 로그 중 에러 발생: {e}"
    
    print("페이지 콘솔 로그로 로그인 테스트 완료!")
    
def test_Login_with_page_error_handling(page: Page, base_url):
    print("\n 페이지 오류 처리로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 페이지 오류 처리
    try:
        page.on("pageerror", lambda error: print(f"페이지 오류: {error}"))
        page.evaluate("throw new Error('테스트용 페이지 오류')")
    except Exception as e:
        print(f"페이지 오류 처리 중 에러 발생: {e}")
    
    print("페이지 오류 처리로 로그인 테스트 완료!")
    
    
def test_Login_with_page_navigation_back(page: Page, base_url): 
    print("\n 페이지 뒤로 탐색으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 다른 페이지로 탐색 후 뒤로 가기
    try:
        page.goto(f"{base_url}/another-page")  # 다른 페이지로 이동
        page.go_back()  # 이전 페이지로 돌아가기
        print("이전 페이지로 성공적으로 돌아갔습니다.")
    except Exception as e:
        assert False, f"페이지 뒤로 탐색 중 에러 발생: {e}"
    
    print("페이지 뒤로 탐색으로 로그인 테스트 완료!")
    
    
def test_Login_with_page_navigation_forward(page: Page, base_url):
    print("\n 페이지 앞으로 탐색으로 로그인 테스트 시작!")
    
    login_page = LoginPage(page, base_url)
    
    # 로그인 페이지로 이동
    login_page.goto_login_page()
    
    # 다른 페이지로 탐색 후 앞으로 가기
    try:
        page.goto(f"{base_url}/another-page")  # 다른 페이지로 이동
        page.go_back()  # 이전 페이지로 돌아가기
        page.go_forward()  # 다음 페이지로 이동
        print("다음 페이지로 성공적으로 탐색되었습니다.")
    except Exception as e:
        assert False, f"페이지 앞으로 탐색 중 에러 발생: {e}"
    
    print("페이지 앞으로 탐색으로 로그인 테스트 완료!") 
'''
    