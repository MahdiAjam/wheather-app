@echo off
echo Installing Weather App...
echo =============================================

REM Create installation directory
set INSTALL_DIR=%USERPROFILE%\WeatherApp
echo Creating installation directory: %INSTALL_DIR%
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copy files
echo Copying files...
copy claude.py "%INSTALL_DIR%\"
copy requirements.txt "%INSTALL_DIR%\"
copy weather_icon.ico "%INSTALL_DIR%\"
copy WeatherApp.bat "%INSTALL_DIR%\"

REM Create desktop shortcut
echo Creating desktop shortcut...
set SHORTCUT_PATH=%USERPROFILE%\Desktop\Weather App.lnk
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%INSTALL_DIR%\WeatherApp.bat'; $Shortcut.IconLocation = '%INSTALL_DIR%\weather_icon.ico'; $Shortcut.Save()"

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo =============================================
echo Installation complete!
echo You can now run Weather App from your desktop shortcut or from %INSTALL_DIR%\WeatherApp.bat
echo =============================================

pause 