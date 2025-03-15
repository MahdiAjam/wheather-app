# Modern Weather App

A beautiful, modern weather application with a dark-themed UI that displays current weather conditions for any city.

## A demo of app
https://github.com/user-attachments/assets/bea76d9d-c7f7-4417-a37e-3c875ed76bc2

## Features

- Modern dark-themed UI
- Real-time weather data from OpenWeatherMap API
- Displays temperature, humidity, pressure, wind speed, visibility, and more
- Dynamic theming based on weather conditions
- Responsive design with scrollable interface

## Installation

### Option 1: Standalone Executable (Easiest)

1. Run the `create_single_exe.bat` file by double-clicking it
2. Wait for the process to complete
3. Find the `WeatherApp.exe` file in the root directory
4. Double-click the executable to run the application - no installation needed!
5. You can copy this single .exe file to any Windows computer and it will run without installation

### Option 2: Using the MSI Installer

1. Run the `build_installer.bat` file by double-clicking it
2. Follow the prompts to install the required dependencies and build the installer
3. Once complete, navigate to the `dist` folder
4. Run the `.msi` installer file and follow the installation wizard
5. The application will be installed and a shortcut will be created on your desktop

### Option 3: Manual Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application directly:
   ```
   python kharazmi/claude.py
   ```

## Building the Executables Manually

### For Standalone EXE (PyInstaller)

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the application icon:
   ```
   python create_icon.py
   ```

3. Build the standalone executable:
   ```
   pyinstaller --name=WeatherApp --onefile --windowed --icon=weather_icon.ico kharazmi/claude.py
   ```

4. The executable will be available in the `dist` folder

### For MSI Installer (cx_Freeze)

1. Install cx_Freeze:
   ```
   pip install cx_Freeze
   ```

2. Build the executable:
   ```
   python setup.py build
   ```

3. Create the MSI installer:
   ```
   python setup.py bdist_msi
   ```

4. The installer will be available in the `dist` folder

## System Requirements

- Windows 10 or later
- No Python installation needed for the standalone executable or MSI installer
- Internet connection (for weather data)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons and emojis used for weather conditions 