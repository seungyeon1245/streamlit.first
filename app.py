import streamlit as st

st.title('세션 상태 이해하기 🧠')


# 세션 상태 초기화 및 활용
st.header('1. 세션 상태 초기화 및 활용')

# 세션 상태에 값이 없으면 초기화
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# 카운터 버튼
if st.button('카운터 증가'):
    st.session_state.counter += 1

# 카운터 값 표시
st.write(f"현재 카운터 값: {st.session_state.counter}")

# 세션 상태 초기화 버튼
if st.button('카운터 리셋'):
    st.session_state.counter = 0

# 세션 상태 내용 보기
st.header('2. 세션 상태 내용 확인')
st.write("현재 세션 상태:")
st.write(st.session_state)

# 다양한 초기화 방법
st.header('3. 다양한 초기화 방법')

code = """
# 방법 1: 딕셔너리 스타일
st.session_state['name'] = 'Alice'

# 방법 2: 속성 스타일
st.session_state.age = 25

# 방법 3: 한 번에 여러 값 설정
if 'user_info' not in st.session_state:
    st.session_state['user_info'] = {
        'name': 'Bob',
        'age': 30,
        'is_member': True
    }
"""

st.code(code, language='python')

# 실제 초기화 예제
st.header('4. 실제 초기화 예제')
if 'name' not in st.session_state:
    st.session_state['name'] = '홍길동'

st.text_input('이름', key='name') # key 와 연동되어 관리
st.write(f"저장된 이름: {st.session_state['name']}")