

import streamlit as st
from streamlit_option_menu import option_menu
from car_damage_detection import car_damage_detection_page
from utils import fetch_car_data
from admin_portal import admin_portal

# Set the page config
st.set_page_config(page_title="Automobile Damage Detection", layout="wide")

# Check for admin page in query paramss
query_params = st.query_params
if 'admin' in query_params:
    admin_portal()
else:
    # Sidebar for navigation using option_menu
    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>Welcome User</h1>", unsafe_allow_html=True)
        page = option_menu(
            "Navigation", 
            ["Home", "Car Damage Detection", "Contact Us"],
            icons=["house", "search", "envelope"],
            menu_icon="cast",
            default_index=0,
        )
        st.success("Welcome to the Automobile Damage Detection Website. Verify car authenticity, upload damaged car images, detect damages, get repair cost estimates, and download detailed PDF reports.")
        st.info("Currently logged in as User")


    # Home Page
    if page == "Home":
        st.image('banner.jpg', use_column_width=True)
        st.markdown("***")
        st.markdown("<h2 style='text-align: center;'>Project Information</h2>", unsafe_allow_html=True)
        st.markdown("***")
        st.markdown("""
        ## Welcome to the Automobile Damage Detection App!
        This app offers a variety of features to help you manage and assess car damages effectively. Below are the key functionalities:

        ### Car Damage Detection
        - **Authenticity Check**: Verifies car details in our database to prevent frauds.
        - **Damage Detection**: If the car data matches, upload an image of the damaged car. The system will detect the damaged parts and provide an estimated repair cost.
        - **PDF Report**: Download a detailed PDF report containing the predicted image, car details, damaged parts, and the total estimated cost.

        ### Dashboard
        - **Performance Monitoring**: Monitor the application's performance and manage car data efficiently.
        - **Data Insights**: Gain insights into the types of damages, frequency, and repair costs.

        ### Contact Us
        - **Support**: Reach out to the developer or project owner for support or inquiries.
        - **Feedback**: Provide feedback to help us improve the application.

        To get started, navigate to the **Car Damage Detection** page and upload a car image for an instant damage assessment.
        """)
        
        st.markdown("***")
        
        st.header("How It Works")
        st.markdown("""
        1. **Authenticate Car**: Enter the car details to verify authenticity.
        2. **Upload Image**: Upload an image of the damaged car.
        3. **Detect Damage**: The system analyzes the image and identifies the damaged parts.
        4. **Estimate Cost**: Get an estimated repair cost based on the detected damages.
        5. **Download Report**: Download a PDF report with all the details.
        """)
        
        st.markdown("***")
        
        st.header("Features")
        st.markdown("""
        - **Accurate Damage Detection**: Uses advanced image processing and machine learning to detect damages accurately.
        - **Fraud Prevention**: Ensures car details are verified before processing.
        - **User-Friendly Interface**: Easy-to-use interface for a seamless experience.
        - **Detailed Reports**: Provides comprehensive reports for better understanding and transparency.
        """)
        
        st.markdown("***")
        
        # st.header("Notes")
        st.warning("Please note that the accuracy of the model is based on the dataset available during model training. For real-world predictions, the accuracy may vary.")
        st.success("For more information, visit the [Automobile Damage Detection App](https://automobile-damage-detection.streamlit.app).")

    # Car Damage Detection Page
    elif page == "Car Damage Detection":
        st.markdown("<h1 style='text-align: center;'>Automobile Damage Detection</h1>", unsafe_allow_html=True)
        st.markdown("***")

        st.header("Steps to Detect Car Damages and Estimate Repair Cost")
        st.markdown("""
        Welcome to the Car Damage Detection page. Follow the steps below to detect damages in your car and get an estimated repair cost:

        1. **Enter Car Registration Number**: Verify the car's authenticity by entering the car registration number. This helps prevent fraud.
        2. **Fetch Car Data**: Click the button to fetch car details from the database.
        3. **Upload Damaged Car Image**: If the car data is verified, upload an image of the damaged car.
        4. **Detect Damages**: The system will analyze the image to identify damaged parts.
        5. **Get Repair Cost Estimate**: Receive an estimated repair cost based on the detected damages.
        6. **Download Report**: Download a detailed PDF report with the car details, damage detection results, and estimated repair cost.
        """)
        st.markdown("***")

        car_damage_detection_page()


    # Contact Us Page
    elif page == "Contact Us":
        st.markdown("<h1 style='text-align: center;'>Automobile Damage Detection</h1>", unsafe_allow_html=True)
        st.markdown("***")
        st.header("Contact Us")
        st.write("Please fill out the form below to get in touch with me.")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message", height=150)

        if st.button("Submit"):
            if name.strip() == "" or email.strip() == "" or message.strip() == "":
                st.warning("Please fill out all the fields.")
            else:
                send_email_to = 'kumawatharsh2004@gmail.com'
                st.success("Your message has been sent successfully!")






# elif page == "Contact Us":
    #     st.markdown("***")
    #     st.header("Our Team")
    #     row1 = st.columns(3)

    #     # Data for team members
    #     team_members = [
    #         {"name": "Harsh Kumawat (9922102118)", "image": "1.jpeg", "linkedin": "https://www.linkedin.com/in/alice-smith"},
    #         {"name": "Anmol Dhuwalia (9922102109)", "image": "1.jpeg", "linkedin": "https://www.linkedin.com/in/bob-johnson"},
    #         {"name": "Athatva Goel (9922102097)", "image": "1.jpeg", "linkedin": "https://www.linkedin.com/in/carol-white"}
    #     ]

    #     # Iterate over the columns and add team member details
    #     for col, member in zip(row1, team_members):
    #         with col:
    #             st.image(member["image"], use_column_width=True)
    #             st.markdown(f"<h3 style='text-align: center;'>{member['name']}</h3>", unsafe_allow_html=True)
    #             st.markdown(
    #                 f"<p style='text-align: center;'><a href='{member['linkedin']}' target='_blank'>"
    #                 f"<img src='https://image.flaticon.com/icons/png/512/174/174857.png' width='24'></a></p>",
    #                 unsafe_allow_html=True
    #             )

    #     st.markdown("***")
    #     st.header("Contact Me")
    #     st.write("Please fill out the form below to get in touch with me.")

    #     # Input fields for user's name, email, and message
    #     name = st.text_input("Your Name")
    #     email = st.text_input("Your Email")
    #     message = st.text_area("Message", height=150)

    #     # Submit button
    #     if st.button("Submit"):
    #         if name.strip() == "" or email.strip() == "" or message.strip() == "":
    #             st.warning("Please fill out all the fields.")
    #         else:
    #             send_email_to = 'kumawatharsh2004@gmail.com'
    #             st.success("Your message has been sent successfully!")




    # Admin Login Sections
    admin_button_placeholder = st.empty()
    with admin_button_placeholder.container():
        if not st.session_state.get('admin_authenticated', False):
            if st.sidebar.button("Admin Login", key="admin_login_button"):
                st.session_state['show_admin_login'] = True
            
            if st.session_state.get('show_admin_login', False):
                with st.sidebar.form("login_form"):
                    st.write("Admin Login")
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    login_button = st.form_submit_button("Login")

                    if login_button:
                        if username == "harshk" and password == "test@123":  
                            st.session_state['admin_authenticated'] = True
                            st.session_state['show_admin_login'] = False
                            st.success("Login successful")
                            
                            st.query_params.admin = "true"
                        else:
                            st.error("Invalid credentials")
        else:
            admin_portal()
