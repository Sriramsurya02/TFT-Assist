# TFT-Assist

A Python automation script that uses Selenium to collect Team Planner codes from https://tactics.tools and saves them into a local Notepad file (Top Comps.txt).
The script automatically:
- Opens Top Comps.txt in Notepad
- Launches Chrome via Selenium
- Navigates to the STATS page
- Scrolls through available comps
- Clicks "Copy Team Planner code" buttons
- Reads the copied code from the clipboard
- Writes all collected codes into the file

**How It Works**
- Launches Notepad with Top Comps.txt
- Opens Chrome using Selenium WebDriver
- Navigates to: https://tactics.tools
- Clicks the STATS section
- Finds all buttons with: aria-label="Copy Team Planner code"
- Scrolls and clicks each button
- Reads copied data using pyperclip
- Prevents duplicate collection
- Saves all codes to Top Comps.txt
- Closes the browser

**Requirements**

- Python 3.8+
- Google Chrome
- ChromeDriver (matching your Chrome version)

**Python Packages**
Install required packages:
pip install selenium pyperclip

**Important Notes**
- The script uses random delays to simulate human interaction.
- If a browser alert appears, the script waits until it is manually closed.
- The file Top Comps.txt is overwritten each time the script runs.
- ChromeDriver must match your installed Chrome version.
- This script is designed for Windows (uses notepad.exe).

**Key Technologies Used**
Selenium WebDriver
pyperclip
subprocess
WebDriverWait / Expected Conditions
