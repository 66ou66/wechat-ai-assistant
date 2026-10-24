@echo off
cd /d "%~dp0"

rem The DeepSeek API key is loaded automatically from .env (python-dotenv).
rem If several Python versions are installed, adjust the fallback below to
rem the one that has the project dependencies (see requirements.txt).

set "PYTHON=python"
python -c "import pyautogui, pyperclip, keyboard, requests, dotenv" >nul 2>&1
if errorlevel 1 set "PYTHON=py -3.7"

%PYTHON% -c "import pyautogui, pyperclip, keyboard, requests, dotenv" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python dependencies missing: pyautogui / pyperclip / keyboard / requests / python-dotenv
    echo Fix: run  python -m pip install -r requirements.txt
    pause
    exit /b 1
)

%PYTHON% wechat_ai.py
pause
