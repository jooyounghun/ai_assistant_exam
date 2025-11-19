import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini AI 챗봇", layout="centered")

def gemini_chat():
    st.markdown("""
        <style>
        body, .stApp {
            background: #fff !important;
            color: #111 !important;
        }
        .section-title {
            color: #111 !important;
            font-size: 1.45em;
            margin-top: 0.7em;
            font-weight: 800;
            letter-spacing: -.4px;
        }
        .chat-user {
            font-weight:600;
            margin: 10px 0 3px 0;
            color:#111;
        }
        .chat-ai {
            color: #262626;
            background: #f3f2fd;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 3px 0 16px 24px;
            border: 1.1px solid #f0f0fa;
            font-size:1.01em;
        }
        </style>
    """, unsafe_allow_html=True)

    # API 키 입력 및 세션 저장
    if 'gemini_api_key' not in st.session_state:
        st.session_state.gemini_api_key = ''

    st.markdown('<div class="section-title">Gemini 3.0 기반 AI 대화 챗봇</div>', unsafe_allow_html=True)
    st.write("아래에 Gemini API 키를 입력해야 대화가 가능합니다. 키 값은 저장되지 않으며, 세션 내에서만 사용됩니다.")

    with st.form(key="apikey_form"):
        api_key_input = st.text_input("Gemini API Key를 입력하세요.", type="password")
        api_submitted = st.form_submit_button("API 키 등록/변경")
        if api_submitted and api_key_input:
            st.session_state.gemini_api_key = api_key_input
            st.success("API KEY가 저장되었습니다.")

    if not st.session_state.gemini_api_key:
        st.warning("API 키를 등록해야 Gemini 챗봇을 사용할 수 있습니다!")
        return

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.markdown('<div class="section-title">Gemini와 대화하기</div>', unsafe_allow_html=True)
    st.caption("※ API Key는 화면에 노출되지 않으며, 세션 내에서만 사용됩니다. 안전하게 입력하세요.")

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("질문을 입력하세요.", "")
        submitted = st.form_submit_button("Gemini에게 질문하기")

    if submitted and user_input:
        try:
            client = genai.Client(api_key=st.session_state.gemini_api_key)
            response = client.models.generate_content(
                model="gemini-3-pro-preview",
                contents=user_input,
            )
            ai_reply = response.text
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("ai", ai_reply))
        except Exception as e:
            msg = f"[에러] Gemini 응답 실패: {e}"
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("ai", msg))

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div class='chat-user'>🙋 나: {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-ai'>{msg}</div>", unsafe_allow_html=True)
