import streamlit as st
from utils import fetch_all_car_data, add_car_data
import pandas as pd
from streamlit_option_menu import option_menu

def admin_portal():
    # st.markdown("<h1 style='text-align: center;'>Admin Portal</h1>", unsafe_allow_html=True)
    # st.write("Welcome to the Admin Portal. Here you can manage your application.")

    # Sidebar for admin portal navigation
    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>Welcome Admin</h1>", unsafe_allow_html=True)
        

        
        admin_page = option_menu(
            "Navigation", 
            ["Home", "Get Car Data", "Add New Car Data"],
            icons=["house", "search", "plus-circle"],
            menu_icon="cast",
            default_index=0,
        )
        st.success("Welcome to the Automobile Damage Detection Admin Portal. Manage car data and monitor the application here.")
        st.info("Currently logged in as Admin")

        if st.button("Logout"):
            st.write("Redirecting to the main website...")
            # st.experimental_set_query_params(admin="false")
            st.query_params.admin = "false"
            st.markdown('<meta http-equiv="refresh" content="0; url=https://automobile-damage-detection.streamlit.app" />', unsafe_allow_html=True)


    if admin_page == "Home":
        st.image('adminbanner.jpg')
        st.markdown("***")
        st.markdown("<h2 style='text-align: center; font-size: 32px;'>ADMIN HOME</h2>", unsafe_allow_html=True)
        
        # st.markdown("<h3 style='text-align: center;'>Welcome, Admin</h3>", unsafe_allow_html=True)
        st.write("Here you can manage the car data and monitor the performance of the Automobile Damage Detection application.")
        
        st.markdown("### Features", unsafe_allow_html=True)
        st.write("""
        <ul style='font-size: 18px;'>
            <li><b>Get Car Data</b>: View all the car data available in the database.</li>
            <li><b>Add New Car Data</b>: Add new car information to the database.</li>
            <li><b>Logout</b>: Securely log out of the admin portal.</li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("***")
        
        st.markdown("<h3 style='text-align: center;'>Overview</h3>", unsafe_allow_html=True)
        st.write("The Admin Portal is your central hub for managing the Automobile Damage Detection application. Here you can:")
        
        st.write("""
        <ul style='font-size: 18px;'>
            <li>View comprehensive data about cars in the system.</li>
            <li>Add new car entries to keep the database updated.</li>
            <li>Monitor application performance and ensure data integrity.</li>
            <li>Logout securely when your work is done.</li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("***")
        
        st.markdown("<h3 style='text-align: center;'>Statistics</h3>", unsafe_allow_html=True)
        st.write("Here are some quick statistics about the current database:")
        
        st.markdown("""
        <ul style='font-size: 18px;'>
            <li>Total Cars: <b>150</b></li>
            <li>Total Brands: <b>25</b></li>
            <li>Latest Entry: <b>2024</b></li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.success("For more information, visit the [Automobile Damage Detection App](https://automobile-damage-detection.streamlit.app).")

    elif admin_page == "Get Car Data":
        # st.markdown("<h2 style='text-align: center;'>Get Car Data</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Get Car Data</h2>", unsafe_allow_html=True)
        st.markdown("***")
        st.write("Fetch and display car data from the database. This feature allows you to view all the car details stored in the database. Simply click the button below to retrieve and display the data in a tabular format.")
        st.markdown("### Instructions")
        st.write("1. Click the **Get Car Data** button to fetch the latest car data from the database.")
        st.write("2. The car data will be displayed in a table format below the button.")
        st.write("3. If no data is found, you will see a warning message.")
        st.markdown("***")
        col1, col2, col3 = st.columns([1, 2, 1])
        # with col2:
        st.info("Click the button above to fetch car data.")
        if st.button("Get Car Data"):
            car_data = fetch_all_car_data()
            if car_data:
                df = pd.DataFrame(car_data)
                st.table(df)
            else:
                st.warning("No car data found.")
            # else:
                # st.info("Click the button above to fetch car data.")

    elif admin_page == "Add New Car Data":
        st.markdown("<h2 style='text-align: center;'>Add New Car Data</h2>", unsafe_allow_html=True)
        st.markdown("***")
        st.write("Add new car data to the database by filling out the form below. This feature allows you to input and save new car details into the database, ensuring that all relevant information is accurately recorded.")

        st.markdown("### Instructions")
        st.write("1. Fill in each field in the form with the car's details.")
        st.write("2. Ensure that all required fields are completed accurately.")
        st.write("3. Click the **Add Car Data** button to save the new car data to the database.")
        st.write("4. You will receive a success message once the data is added successfully.")
        st.markdown("***")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            registration = st.text_input("Registration")
            car_brand = st.text_input("Car Brand")
            colour = st.text_input("Colour")
            model = st.text_input("Model")
            car_type = st.text_input("Type")
            fuel = st.text_input("Fuel")
            year_of_manufacture = st.number_input("Year of Manufacture", min_value=1900, max_value=2100, step=1)
            car_price = st.number_input("Car Price", min_value=0)

            if st.button("Add Car Data"):
                if registration and car_brand and colour and model and car_type and fuel and year_of_manufacture and car_price:
                    car_data = {
                        'Registration': registration,
                        'Car Brand': car_brand,
                        'Colour': colour,
                        'Model': model,
                        'Type': car_type,
                        'Fuel': fuel,
                        'Year of Manufacture': year_of_manufacture,
                        'Car Price': car_price
                    }
                    add_car_data(car_data)
                    st.success("Car data added successfully!")
                else:
                    st.warning("Please fill out all fields.")
