@echo off
set EXE_PATH=%cd%\Play.exe
set STARTUP_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set VIDEO_PATH=%STARTUP_PATH%\videos

if not exist "%VIDEO_PATH%" (
    mkdir "%VIDEO_PATH%"
)

if exist "%STARTUP_PATH%\Play.exe" (
    del "%STARTUP_PATH%\Play.exe"
)

copy /Y "%cd%\videos\*.mp4" "%VIDEO_PATH%"

copy /Y "%EXE_PATH%" "%STARTUP_PATH%\Play.exe"

echo Successful!
pause
