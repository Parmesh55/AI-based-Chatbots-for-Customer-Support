@echo off
REM Change directory to your project folder (if not already there)
cd /d "D:\AI-based Chatbots for Customer Support"

REM Activate the virtual environment
call venv\Scripts\activate

REM Run the Flask application
python app.py

REM Optional: Pause so the command window doesn’t close immediately
pause
