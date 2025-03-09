import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "PIL", "requests", "json", "datetime", "os", "io", "math"],
    "include_files": [],
    "excludes": [],
    "include_msvcr": True,
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Create the executable
executables = [
    Executable(
        "claude.py",  # Your main script (updated path)
        base=base,
        target_name="WeatherApp.exe",  # Name of the executable
        icon="weather_icon.ico",  # Optional: path to your icon file
        shortcut_name="Modern Weather App",
        shortcut_dir="DesktopFolder",
    )
]

setup(
    name="Modern Weather App",
    version="1.0.0",
    description="A modern weather application with beautiful UI",
    options={"build_exe": build_exe_options},
    executables=executables,
    author="Your Name",
) 