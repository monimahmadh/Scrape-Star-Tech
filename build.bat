@echo off
echo Activating virtual environment...
call myenv\Scripts\activate

echo Rebuilding executable...
pyinstaller --onefile --name scrape_startech scrape_startech.py

echo Done!
pause
