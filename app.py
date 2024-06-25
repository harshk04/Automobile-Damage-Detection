import streamlit as st
from streamlit_option_menu import option_menu
from car_damage_detection import car_damage_detection_page
from utils import fetch_car_data
from admin_portal import admin_portal

# Set the page config
st.set_page_config(page_title="Automobile Damage Detection", layout="wide")

# Check for admin page in query params
query_params = st.query_params
if 'admin' in query_params:
    admin_portal()
else:
    # Sidebar for navigation using option_menu
    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
        page = option_menu(
            "Navigation", 
            ["Home", "Car Damage Detection", "Contact Us"],
            icons=["house", "search", "envelope"],
            menu_icon="cast",
            default_index=0,
        )

    # Fixed header
    

    # Placeholder for the admin button
    admin_button_placeholder = st.empty()

    # Home Page
    if page == "Home":
        st.image( 'banner.png')
        st.markdown("***")
        st.markdown("<h2 style='text-align: center;'>Project Information</h2>", unsafe_allow_html=True)
        # st.header("Project Information")
        st.header("1. Home Page")
        st.write("Welcome to the Automobile Damage Detection App. This app allows users to detect damages in cars and estimate repair costs using image processing and machine learning.")
        st.write("To get started, navigate to the Car Damage Detection page.")
        st.header("2. Dashboard")
        st.header("3. Contact Us")
        st.write("This section provides contact information for getting in touch with the developer or project owner.")
        st.write("Please note that the accuracy of the model is based on the dataset available during model training. For real-world predictions, the accuracy may vary.")

    # Car Damage Detection Page
    elif page == "Car Damage Detection":
        st.markdown("<h1 style='text-align: center;'>Automobile Damage Detection</h1>", unsafe_allow_html=True)
        st.markdown("***")
        car_damage_detection_page()

    # Contact Us Page

    elif page == "Contact Us":
        st.markdown("<h1 style='text-align: center;'>Automobile Damage Detection</h1>", unsafe_allow_html=True)
        # st.markdown("***")
        # st.header("Our Team")
        # row1 = st.columns(3)
        # row2 = st.columns(3)

        # for col in row1:
        #     tile = col.container(height=120)
        #     tile.title(":balloon:")

            
        st.markdown("***")
        st.header("Contact Me")
        st.write("Please fill out the form below to get in touch with me.")

        # Input fields for user's name, email, and message
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message", height=150)

        # Submit button
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
                        if username == "admin" and password == "password":  # Replace with your credentials
                            st.session_state['admin_authenticated'] = True
                            st.session_state['show_admin_login'] = False
                            st.success("Login successful")
                            # Set the query parameter to redirect to the admin page
                            st.query_params.admin = "true"
                        else:
                            st.error("Invalid credentials")
        else:
            admin_portal()
