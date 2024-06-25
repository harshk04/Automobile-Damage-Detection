# Automobile-Damage-Detection

Welcome to the Automobile Damage Detection App! This application allows users to detect damages in cars and estimate repair costs using image processing and machine learning. The app also includes an admin portal for managing car data and monitoring application performance.

## 📌 Sneak Peek of Main Page 🙈 :



## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

### User Portal
- **Car Damage Detection**: Users can verify car authenticity by checking car details in the database. If the car data matches, users can upload an image of the damaged car, detect damaged parts, and get an estimated cost of damage.
- **PDF Download**: Users can download a PDF report containing the predicted image, car details, damaged parts details, and the total estimated cost.
- **Contact Us**: Users can fill out a form to get in touch with the developer or project owner.

### Admin Portal
- **Home**: Admins can view an overview of the portal's features and some quick statistics about the current database.
- **Get Car Data**: Admins can fetch and display all car data available in the database.
- **Add New Car Data**: Admins can add new car information to the database.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/automobile-damage-detection.git
    cd automobile-damage-detection
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:

    ```sh
    streamlit run app.py
    ```

## Usage

### User Portal
- Navigate to the **Home** page to get an overview of the app and its features.
- Go to the **Car Damage Detection** page to start the damage detection process. Verify the car details and upload an image of the damaged car.
- Visit the **Contact Us** page to reach out to the developer or project owner.

### Admin Portal
- Access the **Admin Home** to view an overview and statistics about the database.
- Use the **Get Car Data** page to fetch and display all car data in the database.
- Go to the **Add New Car Data** page to input and save new car details.

## Admin Login Details

To access the admin portal, use the following login credentials:

- **Username**: `admin`
- **Password**: `password`

## File Structure

- `app.py`: Main application file for the user portal.
- `car_damage_detection.py`: Contains the car damage detection logic.
- `pdf_generator.py`: Generates a PDF report for the detected damages and estimated costs.
- `utils.py`: Utility functions for fetching and adding car data.
- `admin_portal.py`: Contains the admin portal functionalities.

## Contributing

We welcome contributions! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### 📬 Contact


If you want to contact me, you can reach me through below handles.

&nbsp;&nbsp;<a href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/"><img src="https://www.felberpr.com/wp-content/uploads/linkedin-logo.png" width="30"></img></a>

© 2024 Harsh

