import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight 😔", "#F4A261"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight 😊", "#2A9D8F"
    elif 25 <= bmi < 29.9:
        return "Overweight 😟", "#E9C46A"
    else:
        return "Obese 😨", "#E76F51"

# Streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
st.markdown("""
    <style>
        body { text-align: center; }
        .big-font { font-size:25px !important; font-weight:bold; }
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #2A9D8F;'>BMI Calculator ⚖️</h1>", unsafe_allow_html=True)

weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01, format="%.2f")

cols1 , cols2 = st.columns(2)
with cols1:
 if st.button("Calculate BMI 🏋️‍♂️"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        status, color = get_bmi_status(bmi)
        st.markdown(f"""<p class='big-font' style='color:{color};'>Your BMI: {bmi}</p>""", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:22px; color:{color};'>{status}</p>", unsafe_allow_html=True)
    else:
        st.info("Please enter valid values for weight and height!")
      
with cols2 :
  if st.button("clear ❌"): 
     st.rerun()
   
     



        
        

        
