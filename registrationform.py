import streamlit as st

st.title("Event Registration Form")

st.write("Please fill out the form below to register for the event.")

with st.form("registration_form"):

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    
    event_day = st.selectbox("Which day will you attend?", ("Day 1", "Day 2", "Both Days"))
    participation = st.radio("Are you participating in any event activity?", ("Yes", "No"))
    dietary_pref = st.selectbox("Do you have any dietary preferences?", ("None", "Vegetarian", "Vegan", "Gluten-Free", "Other"))
    tshirt_size = st.selectbox("T-shirt Size", ("XS", "S", "M", "L", "XL", "XXL"))

    feedback = st.text_area("Any specific questions or feedback?")
    consent = st.checkbox("I agree to share my details for the event purpose.")

    submit_button = st.form_submit_button("Submit")

if submit_button:
    if consent:
        st.success(f"Thank you {name} for registering!")
        st.write(f"Your details have been submitted: \nEmail: {email}, \nPhone: {phone}, \nEvent Day: {event_day}, \nParticipation: {participation}, \nT-shirt Size: {tshirt_size}, \nDietary Preference: {dietary_pref}")
    else:
        st.error("You must agree to share your details to register.")
