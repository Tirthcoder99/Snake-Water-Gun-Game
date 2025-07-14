''''
1 for Snake
-1 for Water
0 for Gun
'''
import streamlit as st
import random

st.set_page_config(page_title="Snake Water Gun", page_icon="🎮", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #00FFFF;'>🐍 Snake, 💧 Water, 🔫 Gun</h1>
    <style>
    .stRadio > div {
        flex-direction: row;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Choice dictionary
YOUDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDic = {1: "Snake", -1: "Water", 0: "Gun"}

# User input
YOUstr = st.radio("Choose your move:", list(YOUDict.keys()), horizontal=True)

# Only run this when button is clicked
if st.button("Play"):
    YOU = YOUDict[YOUstr]
    Computer = random.choice([-1, 0, 1])

    st.write(f"**You chose:** {reverseDic[YOU]}")
    st.write(f"**Computer chose:** {reverseDic[Computer]}")

    # Game logic
    if Computer == YOU:
        result = "It's a TIE!"
    elif (Computer == -1 and YOU == 1) or (Computer == 1 and YOU == 0) or (Computer == 0 and YOU == -1):
        result = "🎉 You WIN!"
    elif (Computer == -1 and YOU == 0) or (Computer == 1 and YOU == -1) or (Computer == 0 and YOU == 1):
        result = "❌ You LOSE!"
    else:
        result = "⚠️ Something went wrong!"

    st.markdown(f"<h2 style='color: yellow;'>{result}</h2>", unsafe_allow_html=True)

