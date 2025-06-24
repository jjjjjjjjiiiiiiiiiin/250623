import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌡️ 연도별 기온 변화 추이")

try:
    # 구분자 자동 감지 + cp949 인코딩
    df = pd.read_csv("월별 기온.csv", encoding="cp949", engine='python')

    # 연도 열 정리
    df.columns = df.columns.str.strip()  # 열 이름 공백 제거
    df['연도'] = df['연도'].astype(int)

    # 연도 선택 슬라이더
    year_selected = st.slider("연도를 선택하세요", min_value=df['연도'].min(), max_value=2100, step=1)

    if year_selected in df['연도'].values:
        row = df[df['연도'] == year_selected].iloc[0, 1:]  # 월별 데이터
        months = row.index
        temps = row.values

        # 선 그래프
        fig, ax = plt.subplots()
        ax.plot(months, temps, marker='o', linestyle='-', color='tomato')
        ax.set_title(f"{year_selected}년 월별 평균 기온")
        ax.set_xlabel("월")
        ax.set_ylabel("기온 (℃)")
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.warning(f"{year_selected}년 데이터가 없습니다.")

except Exception as e:
    st.error(f"⚠️ 오류 발생: {e}")
