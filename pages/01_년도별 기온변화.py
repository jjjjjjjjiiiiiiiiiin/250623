import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="연도별 기온 변화", layout="wide")

# 제목
st.title("🌡️ 연도별 기온 변화 추이 (1월 ~ 12월)")

# CSV 파일 로드 (같은 폴더에 있는 파일)
try:
    df = pd.read_csv("월별 기온.csv", encoding="cp949")
    
    # 연도 컬럼이 문자열일 수 있으므로 정수로 변환
    df['연도'] = df['연도'].astype(int)

    # 연도 슬라이더 선택
    year_selected = st.slider("연도를 선택하세요", min_value=df['연도'].min(), max_value=2100, step=1)

    if year_selected in df['연도'].values:
        # 해당 연도의 기온 데이터 추출
        monthly_data = df[df['연도'] == year_selected].iloc[0, 1:]  # '1월'부터 '12월'까지
        months = list(monthly_data.index)
        temps = monthly_data.values

        # 선 그래프 그리기
        fig, ax = plt.subplots()
        ax.plot(months, temps, marker='o', linestyle='-', color='tomato')
        ax.set_title(f"{year_selected}년 월별 평균 기온", fontsize=16)
        ax.set_xlabel("월")
        ax.set_ylabel("기온 (℃)")
        ax.grid(True)

        st.pyplot(fig)
    else:
        st.warning(f"{year_selected}년 데이터가 없습니다.")

except FileNotFoundError:
    st.error("⚠️ '월별 기온.csv' 파일이 현재 폴더에 없습니다.")
except Exception as e:
    st.error(f"⚠️ 오류 발생: {e}")
