import streamlit as st
from PIL import Image
import os
import json
from roboflow import Roboflow
from utils import fetch_car_data, calculate_damage_estimation, fetch_car_brand_prices
import time
import pandas as pd
from pdf_generator import generate_pdf
from numbercheck import extract_text_from_image

def car_damage_detection_page():
    st.subheader("Verify car authenticity by uploading Car Image")
    
    # Initialize session state variables
    if 'file_path' not in st.session_state:
        st.session_state.file_path = None
    if 'prediction_json' not in st.session_state:
        st.session_state.prediction_json = None
    if 'car_data_found' not in st.session_state:
        st.session_state.car_data_found = False
    if 'car_number' not in st.session_state:
        st.session_state.car_number = None

    # Upload image file for number plate detection
    File = st.file_uploader(label="Upload Image")
    if File:
        # Ensure the images directory exists before saving
        image_dir = './images'
        os.makedirs(image_dir, exist_ok=True)  # Create the directory if it doesn't exist
        image_path = os.path.join(image_dir, File.name)
        with open(image_path, mode='wb') as w:
            w.write(File.getvalue())
        st.session_state.file_path = image_path  # Save path in session state for later use

        # Display the uploaded image
        if os.path.exists(image_path):
            st.success("Image uploaded successfully")
            st.image(image_path, width=300)

        # Combined button to extract text and fetch car details
        if st.button("Verify Car Authenticity"):
            with st.spinner("Verifying..."):
                # Step 1: Extract text from the uploaded image
                car_number = extract_text_from_image(image_path).strip()  # Strip any extra spaces
                st.session_state.car_number = car_number  # Save the car number in session state
                st.subheader(f"Car Number: {car_number}")
                
                # Step 2: Fetch car details based on the extracted car number
                if car_number:
                    car_data = fetch_car_data(car_number)
                    if car_data is None:
                        st.error(f"Car with Registration No '{car_number}' not found.")
                        st.session_state.car_data_found = False
                    else:
                        st.success("Car data found. You can proceed with damage detection.")
                        st.session_state.car_data_found = True
                        st.session_state.car_details = car_data  # Save car details for later use

    # Display car details if found
    if st.session_state.car_data_found:
        st.write("Car Data:")

        # Display car details in table
        columns_order = ['Registration', 'Car Brand', 'Model', 'Colour', 'Type', 'Fuel', 'Year of Manufacture', 'Car Price']  # specify the order
        car_data_df = pd.DataFrame([st.session_state.car_details])[columns_order]

        car_data_df.rename(columns={'Registration': 'Registration No.'}, inplace=True)
        car_data_df.rename(columns={'Car Brand': 'Brand'}, inplace=True)
        car_data_df.rename(columns={'Colour': 'Body Color'}, inplace=True)
        car_data_df.rename(columns={'Type': 'Body Style'}, inplace=True)
        car_data_df.rename(columns={'Fuel': 'Fuel Type'}, inplace=True)
        car_data_df.rename(columns={'Year of Manufacture': 'Registration Year'}, inplace=True)
        car_data_df.rename(columns={'Car Price': 'Reselling Value (in INR)'}, inplace=True)
        
        st.table(car_data_df)
        
        st.markdown("***")
        st.warning("Upload an image of the car to detect damages and estimate repair costs.")

        # Upload an image of the car for damage detection
        image_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        if image_file is not None:
            if not os.path.exists("tempDir"):
                os.makedirs("tempDir")
            file_path = os.path.join("tempDir", image_file.name)
            with open(file_path, "wb") as f:
                f.write(image_file.getbuffer())
            st.session_state.file_path = file_path

            col1, col2 = st.columns(2)
            with col1:
                st.image(Image.open(file_path), width=400, caption="Uploaded Image")

            # Roboflow setup for damage detection
            rf = Roboflow(api_key="LRvtIEC3Onz66K3Q2C0b")
            project = rf.workspace("automobile-damage-detection").project("automobile-damage-detection")
            model = project.version(1).model

            confidence_threshold = 20
            overlap_threshold = 20

            # Predict damage using the uploaded image
            with st.spinner("Detecting damage..."):
                prediction = model.predict(file_path, confidence=confidence_threshold, overlap=overlap_threshold)
                prediction.save("prediction.jpg")
                st.session_state.prediction_json = prediction.json()

            # Display the prediction image
            if st.session_state.prediction_json:
                with col2:
                    st.image("prediction.jpg", width=400, caption="Predicted Image")

                prediction_json = st.session_state.prediction_json

                # Fetch the damage price data for the car's brand
                car_brand = st.session_state.car_details.get("Car Brand")

                # Ensure car_brand is a string
                if isinstance(car_brand, str):
                    price_mapping = fetch_car_brand_prices(car_brand)
                else:
                    st.error(f"Error: Expected 'Car Brand' to be a string, but got {type(car_brand)}")
                    return

                # Calculate the total price and damage details
                total_price, price_details = calculate_damage_estimation(prediction_json, price_mapping)

                # Display damage estimation results
                st.markdown("## Damage Estimations")

                for detail in price_details:
                    st.markdown(f"""
                        <div style="background-color: #b9b9c7; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                            <h4 style="color: #333;">Damaged Part: <span style="color: #cc0000;">{detail[1]}</span></h4>
                            <h4 style="color: #333;">Damage Percent: <span style="color: #0066cc;">{detail[0]*100} %</span></h4>
                            <h4 style="color: #333;">Estimated Price: ₹ <span style="color: #009933;">{detail[2]:.2f}</span></h4>
                        </div>
                    """, unsafe_allow_html=True)

                # Display the total price estimation
                st.markdown(f"""
                    <div style="background-color: #b9b9c7; padding: 20px; border-radius: 5px; margin-top: 20px;">
                        <h3 style="color: #333; text-align: center;">Total estimated price of repair: ₹  <span style="color: #ff6600;">{total_price:.2f}</span></h3>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("***")
                col1, col2, col3 = st.columns([1, 1, 1])

                # Provide options to download results
                with col2:
                    st.download_button(
                        label="Download prediction Results (JSON)",
                        data=json.dumps(prediction_json),
                        file_name="prediction_results.json",
                        mime="application/json",
                        key="download_button_json"
                    )

                    pdf_buffer = generate_pdf(st.session_state.car_details, prediction_json, total_price, price_details, "prediction.jpg")
                    st.download_button(
                        label="Download prediction Results (PDF)",
                        data=pdf_buffer,
                        file_name="prediction_results.pdf",
                        mime="application/pdf",
                        key="download_button_pdf"
                    )
