import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"

st.title("us visa predicator")

st.markdown("enter your details below")


continent = st.selectbox(
    "Continent",
    ["Asia", "Europe", "North America", "South America", "Africa", "Oceania"]
)
education_of_employee=st.selectbox("education",["High School","Master's","Bachelor's"])
has_job_experience=st.selectbox("Has Job Experience?", ["Yes", "No"])
requires_job_training=st.selectbox("Requires Job Training?", ["Yes", "No"])
no_of_employees=st.number_input("Number of Employees", min_value=0)
region_of_employment=st.selectbox("region_of_employment",['West', 'Northeast', 'South', 'Midwest', 'Island'])
prevailing_wage=st.number_input("Prevailing Wage", min_value=0.0)
unit_of_wage=st.selectbox("unit_of_wage",['Hour', 'Year', 'Week', 'Month'])
full_time_position=st.selectbox("Full Time Position?", ["Yes", "No"])


has_job_experience = "Y" if has_job_experience == "Yes" else "N"
requires_job_training = "Y" if requires_job_training == "Yes" else "N"
full_time_position = "Y" if full_time_position == "Yes" else "N"

if st.button("predict"):
    input_data = {
    "continent": continent,
    "education_of_employee": education_of_employee,
    "has_job_experience": has_job_experience,
    "requires_job_training": requires_job_training,
    "no_of_employees": no_of_employees,
    "region_of_employment": region_of_employment,
    "prevailing_wage": prevailing_wage,
    "unit_of_wage": unit_of_wage,
    "full_time_position": full_time_position
}
    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"predict us visa {result}")
        else:
            st.error(f"api error{response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("could not connect with fast api")
