import streamlit as st
from PIL import Image
import os
import json
from roboflow import Roboflow
from utils import fetch_car_data, calculate_damage_estimation
import time
import pandas as pd
from pdf_generator import generate_pdf

def car_damage_detection_page():
    st.header("Car Damage Detection")

    if 'file_path' not in st.session_state:
        st.session_state.file_path = None
    if 'prediction_json' not in st.session_state:
        st.session_state.prediction_json = None
    if 'car_data_found' not in st.session_state:
        st.session_state.car_data_found = False

    car_number = st.text_area("Enter Car Registration No.", height=150, key="car_number")

    if st.button("Fetch Car Data"):
        if car_number:
            with st.spinner("Fetching car data..."):
                car_data = fetch_car_data(car_number)

                if car_data is None:
                    st.error(f"Car with Registration No '{car_number}' not found.")
                    st.session_state.car_data_found = False
                else:
                    st.success("Car data found. You can proceed with damage detection.")
                    st.session_state.car_data_found = True
                    st.session_state.car_details = car_data  # Save car details for later use

    if st.session_state.car_data_found:
        st.write("Car Data:")

        # Convert car_data dictionary to a pandas DataFrame for tabular display
        car_data_df = pd.DataFrame([st.session_state.car_details])
        st.table(car_data_df)

        st.markdown("***")
        st.warning("Upload an image of the car to detect damages and estimate repair costs.")

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

            rf = Roboflow(api_key="LRvtIEC3Onz66K3Q2C0b")
            project = rf.workspace("automobile-damage-detection").project("automobile-damage-detection")
            model = project.version(1).model

            confidence_threshold = 40
            overlap_threshold = 30

            with st.spinner("Detecting damage..."):
                prediction = model.predict(file_path, confidence=confidence_threshold, overlap=overlap_threshold)
                prediction.save("prediction.jpg")
                st.session_state.prediction_json = prediction.json()

            if st.session_state.prediction_json:
                with col2:
                    st.image("prediction.jpg", width=400, caption="Predicted Image")

                prediction_json = st.session_state.prediction_json
                total_price, price_details = calculate_damage_estimation(prediction_json)

                st.markdown("## Damage Estimations")

                for detail in price_details:
                    st.markdown(f"""
                        <div style="background-color: #b9b9c7; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                            <h4 style="color: #333;">Damaged Part: <span style="color: #cc0000;">{detail[1]}</span></h4>
                            <h4 style="color: #333;">Damage Percent: <span style="color: #0066cc;">{detail[0]*100} %</span></h4>
                            <h4 style="color: #333;">Estimated Price: ₹ <span style="color: #009933;">{detail[2]:.2f}</span></h4>
                        </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div style="background-color: #b9b9c7; padding: 20px; border-radius: 5px; margin-top: 20px;">
                        <h3 style="color: #333; text-align: center;">Total estimated price of repair: ₹  <span style="color: #ff6600;">{total_price:.2f}</span></h3>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown("***")
                col1, col2, col3 = st.columns([1, 1, 1])

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
