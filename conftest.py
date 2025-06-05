import pytest
import shutil
import os
import datetime
import time

from datetime import datetime
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
    headless = pytestconfig.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # GUI 모드로 실행하려면 headless=False로 설정해줘야 함
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

# def is_report_complete(file_path):
#     """
#     파일 크기나 내용에 특정 문자열이 포함되어 있는지 체크하여
#     리포트가 완전히 작성되었는지 확인하는 함수입니다.
#     """
#     # 파일이 존재하고 크기가 일정 이상일 때 완료된 것으로 간주
#     if os.path.exists(file_path):
#         # 파일 크기가 1KB 이상인지 체크 (일반적으로 HTML 리포트 파일은 최소 1KB 이상)
#         file_size = os.path.getsize(file_path)
#         if file_size > 1024:  # 1KB 이상이면 리포트 내용이 있다고 판단
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 content = f.read()
#                 # 결과 내용에 "Tests run" 문구가 포함되면 리포트가 완료되었음
#                 if "Tests run" in content:
#                     return True
#     return False
  
# def pytest_sessionfinish(session, exitstatus):
#     # 테스트가 성공적으로 완료된 경우
#     if exitstatus == 0:
#         # 기본 리포트 경로 (pytest가 생성하는 기본 report.html)
#         default_report = "reports/report.html"
        
#         current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
#         report_name = f"reports/report_{current_date}.html"
        
#         # 리포트가 생성되었는지 확인하고, 내용이 완료될 때까지 기다림
#         wait_time = 0
#         while not is_report_complete(default_report) and wait_time < 5:
#             print(f"\n Waiting for report to complete... Attempt {wait_time+1}/5")
#             time.sleep(1)  # 1초 대기
#             wait_time += 1

#         # 리포트가 완료되었으면, 현재 날짜와 시간으로 리포트 파일 이름 생성
#         if is_report_complete(default_report):            
#             # `report.html`을 원하는 이름으로 복사
#             shutil.copy(default_report, report_name)
#             print(f"Custom report generated: {report_name}")
#         else:
#             print("Report was not completed in time.")       
        
        # # 현재 날짜와 시간으로 리포트 파일 이름 생성
        # current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        # report_name = f"reports/report_{current_date}.html"
        
        # # 리포트 파일이 이미 있으면 삭제
        # if os.path.exists(report_name):
        #     os.remove(report_name)
        
        # # 기본 리포트 경로
        # default_report = "reports/report.html"
        
        # # 기본 리포트를 날짜와 시간 포함된 이름으로 변경
        # if os.path.exists(default_report):
        #     time.sleep(3)
        #     shutil.move(default_report, report_name)
        #     print(f"Custom report generated: {report_name}")
        # else:
        #     print("No report.html generated.")
        
        # print(f"\n Report generated: {report_name}")   
