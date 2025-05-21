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
    if st.button("เริ่มตอบคำถาม :memo:"):
        st.markdown("- ถ้าราคาเพิ่ม 10% แล้วปริมาณลด 20% → Ed = -2 (Elastic)")
