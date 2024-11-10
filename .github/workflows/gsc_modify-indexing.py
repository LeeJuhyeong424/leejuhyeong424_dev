import json
import os
import sys
import requests
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
import re
from datetime import datetime

CREDENTIALS_PATH = '.github/workflows/credentials.json'
SCOPES = ["https://www.googleapis.com/auth/indexing"]
API_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
STATUS_FILE_PATH = 'gsc-index-status.md'

# Google 서비스 계정 인증
def get_credentials():
    credentials = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    request = Request()
    credentials.refresh(request)
    return credentials

# 오류 코드와 설명 매핑
def get_error_message(status_code, error_code=None):
    error_messages = {
        200: ("성공", "요청이 정상적으로 처리되었습니다."),
        301: ("영구 이동", "응답의 Location 헤더에 지정된 URL로 보내야 합니다."),
        303: ("다른 곳 참조", "Location 헤더의 URL로 GET 요청을 보내야 합니다."),
        304: ("수정되지 않음", "캐시된 응답을 사용해야 합니다."),
        307: ("임시 리디렉션", "Location 헤더에 지정된 URL로 요청을 다시 보냅니다."),
        400: ("잘못된 요청", "요청이 잘못되었거나 형식이 부적절합니다."),
        401: ("인증 오류", "인증 정보가 잘못되었거나 제공되지 않았습니다."),
        403: ("권한 없음", "URL 소유권 확인 실패로 요청이 거부되었습니다."),
        404: ("찾을 수 없음", "요청한 리소스를 찾을 수 없습니다."),
        429: ("요청 한도 초과", "API 호출 한도를 초과했습니다."),
        500: ("서버 오류", "서버 내부 오류로 인해 요청이 실패했습니다."),
        503: ("서비스 이용 불가", "백엔드 오류가 발생했습니다."),
    }

    if status_code in error_messages:
        result, description = error_messages[status_code]
        tooltip = f"{error_code or 'N/A'} - {description} (반환코드: {status_code})"
        return result, tooltip

    return "알 수 없는 오류", f"알 수 없는 오류 (반환코드: {status_code})"

# 입력 값 검증 및 파싱 (split 사용)
def validate_and_parse_input():
    modified_files_str = os.getenv("JSON_FILES", "")
    try:
        print(f"받은 추가된 파일 목록: {modified_files_str}")

        # 쉼표로 구분된 문자열을 리스트로 변환
        modified_files = [file.strip() for file in modified_files_str.split(',') if file.strip()]

        if not modified_files:
            print("오류: 추가된 파일 목록이 비어 있습니다.")
            sys.exit(1)

        return modified_files
    except Exception as e:
        print(f"입력 값 처리 오류: {str(e)}")
        sys.exit(1)

# 인덱싱 요청 전송
def send_indexing_request(url):
    credentials = get_credentials()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {credentials.token}'
    }
    data = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    status_code = response.status_code
    error_code = response.json().get("error", {}).get("status")
    result, tooltip = get_error_message(status_code, error_code)
    return result, tooltip

# gsc-index-status.md 파일 업데이트
def update_status_file(date, time, result, tooltip, url):
    with open(STATUS_FILE_PATH, 'r') as file:
        lines = file.readlines()

    formatted_date = f"{date.year}년 {date.month}월 {date.day}일"
    formatted_time = f"{time.hour}시 {time.minute}분 {time.second}초"
    date_with_tooltip = f'<span title="{formatted_time}">{formatted_date}</span>'
    result_with_tooltip = f'<span title="{tooltip}">{result}</span>'
    new_record = f"| {date_with_tooltip} | 수정 | {result_with_tooltip} | {url} |\n"

    header = lines[:8]
    existing_records = lines[8:]
    updated_content = header + [new_record] + existing_records

    with open(STATUS_FILE_PATH, 'w') as file:
        file.writelines(updated_content)

# 수정된 파일 리스트 처리
def process_modified_files(modified_files):
    now = datetime.now()

    for file_path in modified_files:
        match = re.search(r'_posts/\d{4}-\d{2}-\d{2}-(.+)\.md$', file_path)
        if match:
            title = match.group(1)
            post_url = f"https://leejuhyeong424dev.github.io/{title}"
            print(f"인덱싱 요청 전송 중: {post_url}")
            result, tooltip = send_indexing_request(post_url)
            print(f"응답 결과: {result}, 툴팁: {tooltip}")
            update_status_file(now, now, result, tooltip, post_url)
        else:
            print(f"파일 경로에서 title 추출 실패: {file_path}")

if __name__ == "__main__":
    modified_files = validate_and_parse_input()
    process_modified_files(modified_files)
