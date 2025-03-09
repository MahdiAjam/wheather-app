@echo off
echo Creating Weather App Installer for Windows
echo =========================================

echo Installing required packages...
pip install cx_Freeze Pillow requests

echo Creating application icon...
python create_icon.py

echo Building the executable...
python setup.py build

echo Creating the installer...
python setup.py bdist_msi

echo Done! The installer can be found in the 'dist' folder.
echo =========================================

pause 