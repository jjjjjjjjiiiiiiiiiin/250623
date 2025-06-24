import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="연도별 기온 변화", layout="wide")
st.title("🌡️ 연도별 기온 변화 추이 (1월 ~ 12월)")

try:
    # 구분자 자동 감지 + 한국어 인코딩 처리
    df = pd.read_csv("월별 기온.csv", encoding="cp949", delimiter=None, engine="python")

    # 컬럼 이름 공백 제거
    df.columns = df.columns.str.strip()

    # 연도 열 처리
    if '연도' not in df.columns:
        raise ValueError("⚠️ '연도'라는 열 이름이 존재하지 않습니다. 첫 번째 열 이름을 확인해 주세요.")

    df['연도'] = df['연도'].astype(int)
