import streamlit as st

# MBTI별 직업 추천 데이터 (중학생 눈높이에 맞게 간단하고 흥미롭게 구성)
mbti_counseling = {
    "INTJ": {
        "strength": "계획을 잘 세우고 목표를 향해 나아가는 힘이 있어요. 🗂️",
        "jobs": ["과학자 🔬", "프로그래머 💻", "전략가 🎯"]
    },
    "INFP": {
        "strength": "상상력이 풍부하고 다른 사람의 마음을 잘 이해해요. 🌱",
        "jobs": ["작가 ✍️", "심리상담가 🧠", "디자이너 🎨"]
    },
    "ENFP": {
        "strength": "에너지가 넘치고 새로운 것을 시도하는 걸 좋아해요. ⚡",
        "jobs": ["크리에이터 📱", "배우 🎭", "여행 가이드 🌍"]
    },
    "ISTJ": {
        "strength": "책임감이 강하고 약속을 잘 지켜요. 🏛️",
        "jobs": ["공무원 📊", "회계사 📈", "군인 🎖️"]
    },
    "ESFP": {
        "strength": "활발하고 분위기를 즐겁게 만드는 능력이 있어요. 🎉",
        "jobs": ["가수 🎤", "배우 🎬", "방송인 📺"]
    },
    # 필요하면 나머지 유형도 같은 방식으로 추가 가능
}

# 앱 제목
st.title("🌟 MBTI 기반 진로 상담 프로그램 🌟")
st.write("안녕하세요, 전문상담교사 선생님이에요. 👩‍🏫\n"
         "당신의 MBTI를 선택하면, 강점과 어울리는 직업을 알려줄게요! 💡")

# MBTI 선택
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택해 주세요:",
    options=list(mbti_counseling.keys())
)

# 결과 출력
if selected_mbti:
    data = mbti_counseling[selected_mbti]
    st.subheader(f"💌 {selected_mbti} 유형 상담 메시지")
    st.write(f"👉 **당신의 강점**: {data['strength']}")
    st.write("✨ **추천 직업**:")
    for job in data["jobs"]:
        st.write(f"- {job}")

    st.success("진로는 한 가지 답만 있는 게 아니에요. 여러 가능성을 탐색하면서, "
               "자신에게 맞는 길을 찾아가면 된답니다. 🌈")
