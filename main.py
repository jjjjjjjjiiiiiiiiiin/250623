import streamlit as st

# MBTI 별 여행지 추천 데이터
mbti_travel = {
    "INTJ": ["교토, 일본", "하이델베르크, 독일"],
    "INTP": ["헬싱키, 핀란드", "레벤워스, 미국"],
    "ENTJ": ["뉴욕, 미국", "두바이, UAE"],
    "ENTP": ["베를린, 독일", "암스테르담, 네덜란드"],
    "INFJ": ["부다페스트, 헝가리", "스톡홀름, 스웨덴"],
    "INFP": ["프라하, 체코", "산토리니, 그리스"],
    "ENFJ": ["바르셀로나, 스페인", "밴쿠버, 캐나다"],
    "ENFP": ["리우데자네이루, 브라질", "시드니, 호주"],
    "ISTJ": ["런던, 영국", "시카고, 미국"],
    "ISFJ": ["에든버러, 영국", "교토, 일본"],
    "ESTJ": ["워싱턴 D.C., 미국", "프랑크푸르트, 독일"],
    "ESFJ": ["로마, 이탈리아", "파리, 프랑스"],
    "ISTP": ["레위니옹섬, 프랑스령", "호놀룰루, 하와이"],
    "ISFP": ["코펜하겐, 덴마크", "삿포로, 일본"],
    "ESTP": ["라스베이거스, 미국", "방콕, 태국"],
    "ESFP": ["바르셀로나, 스페인", "괌, 미국령"]
}

# 페이지 제목
st.title("MBTI 여행지 추천기")

# MBTI 선택
mbti_list = list(mbti_travel.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 추천 여행지 출력
if selected_mbti:
    st.subheader(f"✈️ {selected_mbti}에게 어울리는 여행지 추천")
    recommendations = mbti_travel[selected_mbti]
    for place in recommendations:
        st.markdown(f"- {place}")
