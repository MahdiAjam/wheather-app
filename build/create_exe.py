import os
import subprocess
import sys
import shutil

def create_standalone_exe():
    print("Creating standalone executable for Weather App...")
    
    # Install PyInstaller if not already installed
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Create icon if it doesn't exist
    if not os.path.exists("weather_icon.ico"):
        print("Creating application icon...")
        try:
            from create_icon import create_weather_icon
            create_weather_icon()
        except Exception as e:
            print(f"Error creating icon: {e}")
            print("Using default icon instead.")
    
    # Build the executable
    print("Building standalone executable...")
    
    # PyInstaller command
    pyinstaller_cmd = [
        "pyinstaller",
        "--name=WeatherApp",
        "--onefile",  # Create a single file
        "--windowed",  # Don't show console window
        "--icon=weather_icon.ico",
        "--add-data=weather_icon.ico;.",
        "--clean",
        "claude.py"  # Updated path to the main script
    ]
    
    # Run PyInstaller
    subprocess.check_call(pyinstaller_cmd)
    
    # Copy the executable to the root directory for easy access
    try:
        shutil.copy("dist/WeatherApp.exe", "WeatherApp.exe")
        print("Executable copied to root directory as WeatherApp.exe")
    except Exception as e:
        print(f"Error copying executable: {e}")
    
    print("\nDone! The standalone executable has been created.")
    print("You can find it at: WeatherApp.exe")
    print("Just double-click to run the application - no installation needed!")

if __name__ == "__main__":
    create_standalone_exe() 