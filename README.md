# Dashboard-Design-Based-on-Python-and-CAN-Communication
This repository contains the code for a dashboard designed using Raspberry Pi and an ESP32 microcontroller. The dashboard provides real-time monitoring and visualization of motor performance data, including motor speed and battery current, obtained through CAN communication with the motor controller.

Features:
Raspberry Pi Integration: Utilizes the Raspberry Pi as the main computing platform for running the dashboard application, providing a user-friendly interface for displaying motor performance data.

ESP32 Microcontroller: Interfaces with an ESP32 microcontroller via CAN communication to retrieve motor performance data from the motor controller in real-time.

CAN Communication: Implements CAN communication protocol to establish a reliable communication link between the Raspberry Pi and the ESP32 microcontroller, enabling seamless transmission of motor performance data.

Python and Pygame: The dashboard display is coded using Python programming language, with the Pygame library utilized for enhanced graphical rendering and interactivity, resulting in a visually appealing and intuitive user interface.

Usage:
Setup Hardware: Connect the Raspberry Pi and ESP32 microcontroller according to the hardware setup described in the documentation.

Clone the Repository: Clone this repository to your Raspberry Pi by running the git clone command.

Install Dependencies: Install the necessary Python libraries, including Pygame, on your Raspberry Pi using pip install pygame.

Configure CAN Communication: Configure CAN communication settings on both the Raspberry Pi and the ESP32 microcontroller to establish communication between the two devices.

Run the Dashboard: Execute the Python script responsible for running the dashboard application on the Raspberry Pi, and ensure that the ESP32 microcontroller is powered and connected to the CAN bus.

Monitor Motor Performance: Use the dashboard interface to monitor real-time motor performance data, including motor speed and battery current, displayed in an interactive and visually appealing manner.

Contributions:
Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please feel free to open an issue or submit a pull request.

License:
This project is licensed under the MIT License.

Feel free to adjust the description as needed to better fit your project's specifics!
