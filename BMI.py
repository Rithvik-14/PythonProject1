# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0)

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

# compare status value
if status == 'cms':
    # take height input in centimeters
    height = st.number_input('Centimeters', min_value=0)

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter correct height value")

elif (status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters', min_value=0)

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter correct height value")

else:
    # take height input in feet
    height = st.number_input('Feet', min_value=0)

    # 1 meter = 3.28
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except:
        st.text("Enter correct height value")

# check if the button is pressed or not
if st.button('Calculate BMI'):

    # print the BMI INDEX
    st.text(f"Your BMI Index is {bmi}")

    # give the interpretation of BMI index
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")
