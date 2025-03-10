@echo off
echo Uninstalling Weather App...
echo =============================================

REM Remove installation directory
set INSTALL_DIR=%USERPROFILE%\WeatherApp
echo Removing installation directory: %INSTALL_DIR%
if exist "%INSTALL_DIR%" rmdir /s /q "%INSTALL_DIR%"

REM Remove desktop shortcut
echo Removing desktop shortcut...
set SHORTCUT_PATH=%USERPROFILE%\Desktop\Weather App.lnk
if exist "%SHORTCUT_PATH%" del "%SHORTCUT_PATH%"

echo =============================================
echo Uninstallation complete!
echo =============================================

pause 