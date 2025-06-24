import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 예시 데이터 (실제로는 CSV나 DB 연동 필요)
data = [
    {"대학교": "서울대학교", "학과": "컴퓨터공학과", "입학전형": "수시, 정시", "위도": 37.4602, "경도": 126.9527},
    {"대학교": "고려대학교", "학과": "컴퓨터학과", "입학전형": "수시, 정시", "위도": 37.5865, "경도": 127.0296},
    {"대학교": "한양대학교", "학과": "소프트웨어학부", "입학전형": "정시", "위도": 37.5570, "경도": 127.0459},
    {"대학교": "부산대학교", "학과": "컴퓨터공학부", "입학전형": "수시", "위도": 35.2323, "경도": 129.0846},
    {"대학교": "경북대학교", "학과": "전산전자공학부", "입학전형": "정시", "위도": 35.8886, "경도": 128.6097},
    # 필요한 만큼 추가
]

df = pd.DataFrame(data)

st.title("🎓 희망학과 기반 대학교 찾기")

# 사용자 입력
major_input = st.text_input("희망 학과를 입력하세요 (예: 컴퓨터공학과, 기계공학과 등)")

if major_input:
    filtered = df[df["학과"].str.contains(major_input, case=False)]

    if filtered.empty:
        st.warning("해당 학과가 있는 대학교를 찾을 수 없습니다.")
    else:
        st.success(f"{len(filtered)}개의 대학교가 검색되었습니다.")
        st.dataframe(filtered[["대학교", "학과", "입학전형"]])

        # 지도 생성
        m = folium.Map(location=[36.5, 127.5], zoom_start=7)
        for _, row in filtered.iterrows():
            folium.Marker(
                location=[row["위도"], row["경도"]],
                popup=f"{row['대학교']} - {row['학과']}<br>{row['입학전형']}",
                tooltip=row["대학교"],
            ).add_to(m)

        st.subheader("🗺️ 지도에서 학교 위치 보기")
        st_folium(m, width=700, height=500)
else:
    st.info("위의 입력창에 학과 이름을 입력해 주세요.")
