import streamlit as st
import pandas as pd

# 파일 업로드 및 불러오기
st.title("2025년 5월 기준 연령별 인구 현황 분석")
st.caption("상위 5개 행정구역의 연령별 인구 분포를 선 그래프로 보여줍니다.")

# CSV 파일 불러오기
df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding="euc-kr")

# 전처리
age_columns = [col for col in df.columns if col.startswith("2025년05월_계_")]
rename_dict = {}
for col in age_columns:
    if "총인구수" in col:
        rename_dict[col] = "총인구수"
    elif "100세 이상" in col:
        rename_dict[col] = "100세 이상"
    else:
        rename_dict[col] = col.split("_")[-1].replace("세", "")

df = df.rename(columns=rename_dict)

# '총인구수' 숫자형 변환 후 상위 5개 추출
df["총인구수"] = df["총인구수"].str.replace(",", "").astype(int)
top5 = df.sort_values(by="총인구수", ascending=False).head(5)

# 연령 컬럼 추출 및 숫자형 변환
age_cols = [col for col in top5.columns if col.isdigit() or col == "100세 이상"]
for col in age_cols:
    top5[col] = top5[col].astype(str).str.replace(",", "").astype(int)

# 시각화를 위한 전처리
top5_age = top5[["행정구역"] + age_cols]
top5_age = top5_age.set_index("행정구역").T

# 선 그래프 시각화
st.subheader("상위 5개 행정구역의 연령별 인구 분포")
st.line_chart(top5_age)

# 원본 데이터 표시
st.subheader("원본 데이터 (상위 5개 행정구역)")
st.dataframe(top5.reset_index(drop=True))
