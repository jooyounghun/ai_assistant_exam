import streamlit as st
from gemini_chat import gemini_chat

st.set_page_config(page_title="바이브코딩 AI 비서 가이드", layout="wide")

# ----- 완전 검정 폰트 스타일 -----
st.markdown("""
    <style>
    body, .stApp {
        background: #fff !important;
        color: #111 !important;
    }
    .banner {
        background: linear-gradient(90deg, #edeaff 0%, #f8e9fe 100%);
        color: #111 !important;
        padding: 2.2rem 1rem 1.5rem 1rem;
        border-radius: 1.2em;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 26px 0 rgba(170,150,250,0.11);
    }
    .banner span, .banner h1 {
        color: #111 !important;
    }
    .section-title {
        color: #111 !important;
        font-size: 1.45em;
        margin-top: 1.35em;
        font-weight: 800;
        letter-spacing: -.4px;
    }
    .sub-box {
        background: #fbfaff;
        border-radius: 13px;
        padding: 1.25em 1.22em .6em 1.22em;
        margin-bottom: 1.28em;
        box-shadow: 0 2px 12px 0 #ede7fc5d;
        color: #111 !important;
    }
    .tech-list {
        display: flex;
        gap: 17px;
        margin-top:16px;
        margin-bottom:30px;
        flex-wrap:wrap;
    }
    .tech-item {
        background: #f3f2fd;
        color: #111 !important;
        font-weight:600;
        padding: .52em 1.2em;
        border-radius: 1.8em;
        font-size: 1.00em;
        border: 1.7px solid #eee6fd;
        margin-bottom:5px;
        box-shadow: 0 1px 5px #e9e2f944;
        transition: background 0.2s;
    }
    .tech-item:hover {
        background:#e7e4fa;
        color:#111 !important;
    }
    a, a:visited, a:hover, a:focus {
        color: #111 !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# ----- 상단 배너 -----
st.markdown("""
<div class="banner">
  <h1 style="font-size:2.45em; margin-bottom:.12em; font-weight: 900; letter-spacing:-1.2px; color:#111;">바이브코딩을 활용한 AI 비서 만들기</h1>
  <span style="font-size:1.16em; font-weight:400; color:#111;">쉽고 빠르게 만드는, 당신만의 AI 개인비서 웹앱 가이드</span>
</div>
""", unsafe_allow_html=True)

# ----- 탭 -----
tabs = st.tabs(["🏠 홈", "🐍 Python 설정", "📗 Streamlit 가이드", "🤖 AI 비서"])

# ----- 홈 -----
with tabs[0]:
    st.markdown('<div class="section-title">프로젝트 요약</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-box">\n'
        '이 가이드는 <b style="color:#111;">실전형 Python 및 Streamlit</b> 활용법을 쉽게 따라하며, 직접 <b style="color:#111;">서비스 수준의 AI 비서</b> 앱을 구현할 수 있게 돕습니다.<br><br>'
        '- 단계별 환경설정 안내 및 구현 실습<br>'
        '- 나만의 일정, 메모, 추천, 챗봇 등 <b style="color:#111;">실제 업무·일상 활용 예시</b> 제공<br>'
        '<span style="color:#111; font-weight:700;">위의 탭 메뉴로 각 가이드를 확인해 주세요!</span>'
        '</div>', unsafe_allow_html=True)
    st.info("이곳에서 바이브코딩 기반 AI 비서 프로젝트의 준비와 컨셉을 한 눈에 볼 수 있습니다.")

    # ---- 필요 기술 목록 ----
    st.markdown('<div class="section-title">필요 기술 목록</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="tech-list">'
        '<span class="tech-item">🐍 Python</span>'
        '<span class="tech-item">📗 Streamlit</span>'
        '<span class="tech-item">🐳 Docker</span>'
        '<span class="tech-item">🟥 Redis</span>'
        '<span class="tech-item">✨ Gemini 2.5 Flash</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
# ----- Python 환경설정 -----
with tabs[1]:
    st.markdown('<div class="section-title">🐍 Python 환경설정</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-box">', unsafe_allow_html=True)
    st.header("1. 파이썬 설치")
    st.markdown("""
    - [Python 공식 사이트](https://www.python.org/downloads/)에서 최신 버전 설치
    - Mac: Homebrew 사용 가능(`brew install python3`)
    - Windows: 설치 후 환경변수 자동 등록
    """)
    st.header("2. 가상환경 만들기")
    st.code("""
python -m venv venv
source venv/bin/activate  # (Windows는 venv\\Scripts\\activate)
""", language="bash")
    st.header("3. 필수 라이브러리 설치")
    st.code("pip install streamlit pandas matplotlib numpy", language="bash")
    st.header("4. Jupyter 등 추가")
    st.code("pip install jupyterlab notebook", language="bash")
    st.info("conda 사용자라면 conda create -n myenv python=3.10 등도 추천합니다.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Streamlit 가이드 -----
with tabs[2]:
    st.markdown('<div class="section-title">📗 Streamlit 가이드 핵심정리</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-box">', unsafe_allow_html=True)
    st.header("1. Streamlit이란?")
    st.write(
        "Streamlit은 파이썬으로 쉽고 빠르게 데이터 분석, 머신러닝, AI 프로젝트의 대시보드 및 웹앱을 만들 수 있는 오픈소스 프레임워크입니다."
    )
    st.header("2. 설치 및 기본 명령어")
    st.subheader("설치")
    st.code("pip install streamlit", language="bash")
    st.code("streamlit --version", language="bash")
    st.write("권장: 가상환경(venv, conda 등)에서 설치")
    st.subheader("주요 명령어")
    st.code(
        """streamlit run your_script.py   # 앱 실행
streamlit hello                 # 데모 앱 실행
streamlit config show           # 환경설정 보기
streamlit cache clear           # 캐시 초기화
streamlit docs                  # 문서 바로가기
""",
        language="bash"
    )
    st.header("3. 기본 예제")
    st.write("아래 코드를 복사해서 실행 후, 터미널에서 'streamlit run 파일명.py'로 웹페이지를 확인할 수 있습니다.")
    st.code(
        """import streamlit as st

st.title('Hello Streamlit!')
st.write('데이터 사이언스 앱을 쉽게 만들 수 있습니다.')
""", language="python"
    )
    st.header("4. 주요 사용법 및 위젯")
    with st.expander("텍스트 및 데이터 표시"):
        st.code(
            """st.text('텍스트')
st.markdown('_마크다운_')
st.latex(r'e^{i\\pi} + 1 = 0')
st.write('모든 객체 출력')  # DataFrame, 에러, 함수 등
st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.code('코드블록')
""", language="python"
        )
    with st.expander("데이터 표시"):
        st.code(
            """st.dataframe(df)   # 스크롤 지원
st.table(df)       # 고정 테이블
st.json({'a':1})
st.metric('지표명', 42, 2)
""", language="python"
        )
    with st.expander("미디어 표시"):
        st.code(
            """st.image('file.png')
st.audio(audio_bytes)
st.video(video_bytes_or_file)
""", language="python"
        )
    with st.expander("그래프 · 차트"):
        st.code(
            """st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
st.scatter_chart(df)
st.map(df)
""", language="python"
        )
    with st.expander("인터랙티브 위젯"):
        st.code(
            """st.button('버튼')
st.slider('슬라이더', min_value=0, max_value=100, value=50)
st.text_input('텍스트 입력')
st.selectbox('드롭다운', ['A', 'B'])
st.checkbox('체크박스')
st.radio('라디오', ['A', 'B'])
st.file_uploader('파일 업로드')
st.date_input('날짜', value=None)
""", language="python"
        )
    with st.expander("레이아웃(컬럼, 탭, 사이드바, 폼)"):
        st.code(
            """# 컬럼
col1, col2 = st.columns(2)
col1.write('왼쪽 컬럼')
col2.write('오른쪽 컬럼')

# 탭(Tab)
tab1, tab2 = st.tabs(['탭 1', '탭 2'])
tab1.write('첫 번째 탭')
tab2.write('두 번째 탭')

# 사이드바
st.sidebar.title('사이드바')
value = st.sidebar.radio('선택', [1, 2])

# 폼(Form)
with st.form('my_form'):
    name = st.text_input('이름')
    submitted = st.form_submit_button('제출')
    if submitted:
        st.write(f'안녕하세요, {name}님!')
""", language="python"
        )
    st.header("5. 추가 기능 & 심화")
    st.markdown(
    """
- **캐싱**  
  - `@st.cache_data` (데이터/계산 결과 캐시)  
  - `@st.cache_resource` (리소스 캐시: 예, 모델, DB 등)
- **세션 상태 관리**: `st.session_state` 활용
- **멀티 페이지 앱**: `pages` 폴더에 파이썬 파일로 작성
- **앱 테마 및 커스터마이징**: `.streamlit/config.toml` 파일 작성
- **사이드바, 탭, 메뉴 지원**
"""
    )
    st.header("6. 자주 묻는 질문 (FAQ)")
    with st.expander("FAQ 열기"):
        st.markdown(
            """
- 업로드한 파일은 세션 중 임시저장, 자동 삭제  
- DataFrame을 CSV로 다운로드: `st.download_button()`  
- 앱 테마는 `.streamlit/config.toml`에 설정  
- 여러 파일 레이아웃은 `st.columns`, `st.tabs`, `st.sidebar`로 구현  
- 앱을 중지/재실행: `st.stop()`, `st.rerun()`
- 자세한 내용은 [공식문서](https://docs.streamlit.io/) 참고
""")
    st.info("궁금한 점이 있으면 공식 문서와 치트시트도 참고하세요! [공식문서 바로가기](https://docs.streamlit.io/)")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- AI 비서 -----
with tabs[3]:
    gemini_chat()
