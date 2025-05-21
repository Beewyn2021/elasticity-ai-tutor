import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key-here"))

st.set_page_config(page_title="Econ AI Tutor", page_icon="🐧", layout="wide")

st.markdown("""
    <style>
    .main {background-color: #fef6f6;}
    .title {color: #264653; font-size: 30px; font-weight: bold;}
    .btn {
        font-size: 18px;
        background-color: #f37272;
        border-radius: 10px;
        color: white;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🐧 AI Tutor: Elasticity of Demand (Year 1)</div>', unsafe_allow_html=True)
st.image("penguin_icon.png", width=80)

user_input = st.text_input("อยากรู้อะไรบ้าง (เช่น Elasticity คืออะไร?)")

if user_input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly economics tutor who speaks Thai and English."},
            {"role": "user", "content": user_input}
        ]
    )
    st.success(response.choices[0].message.content)

col1, col2 = st.columns(2)
with col1:
    if st.button("แสดงกราฟ :bar_chart:"):
        st.image("elasticity_graph.png")
with col2:
    st.markdown("### 📝 คำถามเรื่อง Elasticity")
    
    question = "ถ้าราคาเพิ่มขึ้น 10% แล้วปริมาณที่ต้องการลดลง 20% ค่า Ed เท่ากับเท่าไร?"
    st.write(question)

    options = {
    "A. -0.5": "A",
    "B. -1": "B",
    "C. -2": "C",  # correct
    "D. 2": "D"
}
selected_label = st.radio("เลือกคำตอบของคุณ:", list(options.keys()), index=None, key="quiz1")

if selected_label:
    selected = options[selected_label]
    if selected == "C":
        st.success("✅ ถูกต้อง! Ed = -2 แสดงว่าอุปสงค์มีความยืดหยุ่น")
    else:
        st.error("❌ ยังไม่ถูก ลองใหม่! เฉลย: C. -2")

    if selected:
        if selected == "C":
            st.success("✅ ถูกต้อง! Ed = -2 แสดงว่าอุปสงค์มีความยืดหยุ่น")
        else:
            st.error(f"❌ ยังไม่ถูก ลองใหม่! เฉลย: C. -2")
