import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="연도별 기온 변화", layout="wide")
st.title("🌡️ 연도별 기온 변화 추이 (1월 ~ 12월)")

try:
    # CSV 읽기 - 자동 구분자 감지 + 한글 인코딩 대응
    df = pd.read_csv("월별 기온.csv", encoding="cp949", engine="python")

    # 컬럼 공백 제거
    df.columns = df.columns.str.strip()

    # 연도 컬럼 있는지 확인
    if '연도' not in df.columns:
        st.error("❗ '연도'라는 열이 없습니다. CSV의 첫 열 이름을 확인해주세요.")
        st.stop()

    # 연도 숫자형 변환
    df['연도'] = df['연도'].astype(int)

    # 연도 선택
    selected_year = st.slider("연도를 선택하세요", min_value=df['연도'].min(), max_value=2100)

    # 해당 연도 데이터 추출
    if selected_year in df['연도'].values:
        row = df[df['연도'] == selected_year].iloc[0, 1:]  # '1월'부터 '12월'
        months = list(row.index)
        temps = list(row.values)

        # 그래프 출력
        fig, ax = plt.subplots()
        ax.plot(months, temps, marker='o', linestyle='-', color='tomato')
        ax.set_title(f"{selected_year}년 월별 평균 기온")
        ax.set_xlabel("월")
        ax.set_ylabel("기온 (℃)")
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.warning(f"{selected_year}년 데이터가 없습니다.")

except Exception as e:
    st.error(f"⚠️ 오류 발생: {e}")
