import streamlit as st

st.title("Anushka's Student Prediction App")

study = st.slider("Study Hours", 1, 10, 5)
attend = st.slider("Attendance %", 50, 100, 75)

if st.button("Predict Final Score"):
    final = (study * 5) + (attend * 0.3)
    if final >= 50:
        st.success(f"Pass! Score: {final}")
    else:
        st.error(f"Fail! Score: {final}")
    st.progress(int(final))
