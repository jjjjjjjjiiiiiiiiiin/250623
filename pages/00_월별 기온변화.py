import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목
st.title("📈 월별 기온 변화 추이")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file)
    
    # 월 정렬 (숫자 기준 정렬을 위한 전처리)
    df['월숫자'] = df['월'].str.extract(r'(\d+)').astype(int)
    df = df.sort_values('월숫자')
    
    # 그래프 그리기
    fig, ax = plt.subplots()
    ax.plot(df['월'], df['평균기온'], marker='o', linestyle='-', color='skyblue')
    ax.set_xlabel("월")
    ax.set_ylabel("평균 기온 (℃)")
    ax.set_title("월별 평균 기온 변화")
    ax.grid(True)

    # Streamlit에 그래프 출력
    st.pyplot(fig)
else:
    st.info("왼쪽 사이드바에서 CSV 파일을 업로드해 주세요.")

