import os
import subprocess
import sys

def create_standalone_exe():
    print("Creating standalone executable for Weather App...")
    
    # Install PyInstaller if not already installed
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")
    except Exception as e:
        print(f"Error installing PyInstaller: {e}")
        return
    
    # Build the executable
    print("Building standalone executable...")
    
    # PyInstaller command
    pyinstaller_cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--name=WeatherApp",
        "--onefile",  # Create a single file
        "--windowed",  # Don't show console window
        "--clean",
        "claude.py"
    ]
    
    # Run PyInstaller
    try:
        subprocess.check_call(pyinstaller_cmd)
        print("Executable built successfully.")
    except Exception as e:
        print(f"Error building executable: {e}")
        return
    
    print("\nDone! The standalone executable has been created.")
    print("You can find it at: dist/WeatherApp.exe")
    print("Just double-click to run the application - no installation needed!")

if __name__ == "__main__":
    create_standalone_exe() 