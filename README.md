 Unit Converter App
A simple and interactive unit converter built with Python and Streamlit. It allows users to convert values between different units of Length and Temperature with ease.

📋 Features

Convert between Length units:

Meters ↔ Kilometers ↔ Miles


Convert between Temperature units:

Celsius ↔ Fahrenheit ↔ Kelvin


Clean and user-friendly interface
Instant results with a single click


🛠️ Tech Stack

Python 3.x
Streamlit


🚀 Getting Started
1. Prerequisites
Make sure you have Python installed. Then install Streamlit:
bashpip install streamlit
2. Clone the Repository
bashgit clone https://github.com/your-username/unit-converter-app.git
cd unit-converter-app
3. Run the App
bashstreamlit run app.py
The app will open in your browser at http://localhost:8501.

📁 Project Structure
unit-converter-app/
│
├── app.py          # Main Streamlit application
└── README.md       # Project documentation

📖 How to Use

Select a category — Choose between Length or Temperature.
Enter a value — Type in the number you want to convert.
Select units — Pick the From unit and the To unit.
Click Convert — The result will be displayed instantly.


🔢 Conversion Reference
Length
FromToFormulaMetersKilometers÷ 1000MetersMiles÷ 1609.34KilometersMeters× 1000KilometersMiles÷ 0.6214MilesMeters× 1609.34MilesKilometers× 1.6093
Temperature
FromToFormulaCelsiusFahrenheit(°C × 9/5) + 32CelsiusKelvin°C + 273.15FahrenheitCelsius(°F − 32) × 5/9FahrenheitKelvin(°F − 32) × 5/9 + 273.15KelvinCelsiusK − 273.15KelvinFahrenheit(K − 273.15) × 9/5 + 32

🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

📄 License
This project is open source and available under the MIT License.
