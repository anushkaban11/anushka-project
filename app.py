import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Predictor PRO", page_icon="🎓")

st.title("🎓 Student Prediction PRO")
st.write("Final Year AI Project - Anushka Ban")

study = st.slider("Daily Study Hours", 0, 12, 5)
attendance = st.slider("Attendance %", 0, 100, 75)
internal = st.slider("Internal Marks (out of 30)", 0, 30, 20)
sleep = st.slider("Sleep Hours", 0, 12, 7)

if st.button("Predict Final Result"):
    score = (study * 4.5) + (attendance * 0.3) + (internal * 1.2) + (sleep * 1.5)
    if score > 100:
        score = 99.5
    
    st.divider()
    
    if score >= 40:
        st.success(f"PASS! Predicted Score: {score:.1f} / 100")
        st.balloons()
    else:
        st.error(f"NEED IMPROVEMENT! Predicted Score: {score:.1f} / 100")
    
    st.progress(int(score))
    
    if score >= 80:
        grade = "A+ (Excellent)"
    elif score >= 65:
        grade = "B+ (Good)"
    elif score >= 50:
        grade = "C (Average)"
    elif score >= 40:
        grade = "D (Just Pass)"
    else:
        grade = "F (Fail)"
    
    st.metric("Your Grade", grade)
    
    data = pd.DataFrame({
        'Factor': ['Study', 'Attendance', 'Internal', 'Sleep'],
        'Score': [study*8, attendance, internal*3.3, sleep*8]
    })
    st.bar_chart(data.set_index('Factor'))


