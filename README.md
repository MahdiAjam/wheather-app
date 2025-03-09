# Modern Weather App

A beautiful, modern weather application with a dark-themed UI that displays current weather conditions for any city.

## Features

- Modern dark-themed UI
- Real-time weather data from OpenWeatherMap API
- Displays temperature, humidity, pressure, wind speed, visibility, and more
- Dynamic theming based on weather conditions
- Responsive design with scrollable interface

## Installation

### Option 1: Using the Installer (Recommended)

1. Run the `build_installer.bat` file by double-clicking it
2. Follow the prompts to install the required dependencies and build the installer
3. Once complete, navigate to the `dist` folder
4. Run the `.msi` installer file and follow the installation wizard
5. The application will be installed and a shortcut will be created on your desktop

### Option 2: Manual Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application directly:
   ```
   python kharazmi/claude.py
   ```

## Building the Installer Manually

If you want to build the installer manually:

1. Install cx_Freeze:
   ```
   pip install cx_Freeze
   ```

2. Create the application icon:
   ```
   python create_icon.py
   ```

3. Build the executable:
   ```
   python setup.py build
   ```

4. Create the MSI installer:
   ```
   python setup.py bdist_msi
   ```

5. The installer will be available in the `dist` folder

## System Requirements

- Windows 10 or later
- Python 3.7 or later
- Internet connection (for weather data)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons and emojis used for weather conditions 