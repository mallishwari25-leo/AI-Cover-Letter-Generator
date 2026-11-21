import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="AI Cover Letter Generator",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Cover Letter Generator")
st.write("Create a professional cover letter using Artificial Intelligence.")

# Get Gemini API key
api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password"
)

# User information
st.subheader("Personal Information")

name = st.text_input("Your Full Name")
email = st.text_input("Your Email Address")
phone = st.text_input("Your Phone Number")

st.subheader("Job Information")

job_title = st.text_input("Job Title")
company = st.text_input("Company Name")

job_description = st.text_area(
    "Paste the Job Description"
)

skills = st.text_area(
    "Enter Your Skills, Qualifications and Experience"
)

# Generate button
if st.button("Generate Cover Letter"):

    if not all([
        api_key,
        name,
        email,
        job_title,
        company,
        job_description,
        skills
    ]):
        st.warning("Please fill in all required fields.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            prompt = f"""
            Write a professional and personalized job application
            cover letter using the following information.

            Applicant Name: {name}
            Email: {email}
            Phone: {phone}
            Job Title: {job_title}
            Company: {company}
            Job Description: {job_description}
            Skills and Experience: {skills}

            Requirements:
            1. Use a professional tone.
            2. Highlight relevant skills and qualifications.
            3. Explain why the applicant is suitable for the role.
            4. Show interest in joining the company.
            5. Include a professional closing.
            6. Do not invent qualifications or experience.
            """

            with st.spinner("Generating your cover letter..."):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            st.success("Your cover letter has been generated!")

            st.subheader("Your AI-Generated Cover Letter")

            st.text_area(
                "Generated Cover Letter",
                value=response.text,
                height=400
            )

            st.download_button(
                label="Download Cover Letter",
                data=response.text,
                file_name="cover_letter.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
