## creating an frontend app with Streamlit to access the backend API's we made earlier

import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://localhost:8000"  # Change this to your backend API URL

st.title("Backend API Frontend")
st.write("This is a simple frontend to interact with the backend API.")

menu = ["Home", "Get Students", "Add Student", "Update Student", "Delete Student", "Search Students"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Backend API Frontend")
    st.write("Use the sidebar to navigate through different options.")


elif choice == "Get Students":
    st.subheader("Get All Students")
    response = requests.get(f"{BASE_URL}/students/")
    if response.status_code == 200:
        students = response.json()
        df = pd.DataFrame(students)
        st.dataframe(df)
    else:
        st.error("Failed to fetch students.")


elif choice == "Add Student":
    st.subheader("Add a New Student")
    roll_number = st.number_input("Roll Number", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    grade = st.text_input("Grade")
    if st.button("Add Student"):
        student_data = {"roll_number": roll_number, "name": name, "age": age, "grade": grade}
        response = requests.post(f"{BASE_URL}/students/", json=student_data)
        if response.status_code == 201:
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student.")


elif choice == "Update Student":
    st.subheader("Update an Existing Student")
    student_id = st.number_input("Student ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    grade = st.text_input("Grade")
    if st.button("Update Student"):
        student_data = {"name": name, "age": age, "grade": grade}
        response = requests.put(f"{BASE_URL}/students/{student_id}/", json=student_data)
        if response.status_code == 200:
            st.success("Student updated successfully!")
        else:
            st.error("Failed to update student.")


elif choice == "Delete Student":
    st.subheader("Delete a Student")
    student_id = st.number_input("Student ID", min_value=1)
    if st.button("Delete Student"):
        response = requests.delete(f"{BASE_URL}/students/{student_id}/")
        if response.status_code == 204:
            st.success("Student deleted successfully!")
        else:
            st.error("Failed to delete student.")


elif choice == "Search Students":
    st.subheader("Search Students")
    query = st.text_input("Search Query")
    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/students/search/", params={"q": query})
        if response.status_code == 200:
            students = response.json()
            df = pd.DataFrame(students)
            st.dataframe(df)
        else:
            st.error("Failed to search students.")

# To run this app, save it as app.py and use the command: streamlit run app.py

