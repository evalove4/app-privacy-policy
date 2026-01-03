
import streamlit as st
import os

# 1. 페이지 설정
st.set_page_config(page_title="광천 Hills 주차위치 Scanner 다운로드", page_icon="🏢", layout="wide")

# 2. 헤더 및 앱 소개
st.title("🏢 광천 Hills 주차위치 Scanner 앱 다운로드")
st.info("이 앱은 명품 광천힐스테이트 입주민들의 주차장 위치 확인을 위해 제작되었습니다.")

st.markdown("---")

# 3. [핵심] APK 다운로드 섹션
st.header("📥 앱 다운로드 및 설치")
st.info("Version 260104 - 2026년 1월 4일 배포")

apk_file_path = "app-release_2601042.apk"

# 파일이 있는지 확인 후 버튼 표시
if os.path.exists(apk_file_path):
    with open(apk_file_path, "rb") as file:
        btn = st.download_button(
            label="👉 안드로이드 앱 다운로드 (클릭)",
            data=file,
            file_name=apk_file_path
            mime="application/vnd.android.package-archive",
            use_container_width=True,
            type="primary"
        )
    
    st.markdown("""
    ### ⚠️ 설치 안내 (필독)
    1. 위 **다운로드 버튼**을 눌러 파일을 받으세요.
    2. 다운로드가 완료되면 **'파일 열기'**를 누르세요.
    3. **"보안상의 이유로..."** 라는 경고가 뜨더라도 진행해야합니다.
         **[설정]**을 누르고 **[이 소스 허용]**을 켜주세요.
    4. 뒤로가기를 눌러 **[설치]** 버튼을 누르면 완료됩니다.
    5. 설치 후 앱을 실행하세요!
    6. 블루투스 신호 수신을 위해 위치 장치(GPS)의 권한을 요청할 수 있으나, 
        실제 위치 정보는 수집하지 않습니다.
    
    """)
else:
    st.error("현재 배포 파일이 준비되지 않았습니다. 관리자에게 문의하세요.")

st.markdown("---")

# 4. 개인정보 처리방침 (이전에 요청하신 내용 통합)
st.subheader("📋 개인정보 처리방침")

# 본문 내용 (여기에 10줄 이내의 내용을 넣으세요)
content = """
**광천Hills 주차위치 표시기 개인정보 처리방침**

* 1. 수집하는 개인정보 항목

    본 광천Hills 주차위치 표시기 앱은 회원가입기능이 없으며 따라서 이메일, 이름, 전화번호 등

    개인을 식별 할 수있는 어떤 개인정보도 수집하지 않습니다.

* 2. App에서 저장하는 항목

    (1) 사전에 지정된 ESP32-u 고유정보(4글자 / 예시 "0000")

    (2) Scan 된 주차위치 기록(최대 10개)

    (3) 기타 앱 설정 정보

    해당 자료는 외부로 전송되거나 공유되지 않습니다. 

    해당 정보는 스마트폰 내부 SharedPreferences 에만 저장되며, 앱 삭제 시 함께 삭제됩니다. 또한 다른 앱에서 접근할 수 없도록 보호됩니다.

* 3. App에서 요구하는 권한 **

    사용자가 앱을 이용하는 동안 위치 정보나 기타 개인 식별 정보를 저장하거나 추적하지 않습니다.

    블루투스 신호 수신을 위해 위치 장치(GPS)의 권한을 요청할 수 있으나, 실제 위치 정보는 수집하지 않습니다.


* 4. 개인정보의 보유 및 이용기간

    수집하는 정보가 없으므로 보유 기간 또한 없습니다.

* 5. 문의처

    앱 관련 문의사항은 입주민 단톡방에서 말씀해주세요.
"""

st.markdown(content)

# 5. 하단 푸터
st.caption("© 2026 광천힐스 입주민. All rights reserved.")

