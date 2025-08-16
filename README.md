
CBIT Website Scraper Documentation
Overview:
This Python script scrapes visible text content from the CBIT official website (https://www.cbit.ac.in/) and saves it to a local file named script.txt. It is designed to extract announcements, circulars, and other useful information from list items (<li>) and links (<a>).

Features:
- Connects to the CBIT homepage
- Parses HTML using BeautifulSoup
- Extracts visible text from <li> and <a> tags
- Saves the content to script.txt
- Includes error handling and status code checks

Requirements:
To run this script, you need Python installed (version 3.6 or higher recommended). You also need the following Python libraries:
- requests
- beautifulsoup4
You can install them using pip:
pip install requests beautifulsoup4

How to Run:
- Save the Python script as scraper.py.
- Open a terminal or command prompt.
- Navigate to the folder containing scraper.py.
- Run the script using the command:
python scraper.py
- After execution, check the file script.txt in the same folder. It will contain the extracted content from the CBIT website.

File Structure:
CBIT-Scraper/
- scraper.py       → Main scraping script
- script.txt       → Output file with extracted content
- README.txt       → Documentation file

Customization Tips:
If you want to scrape specific sections such as news, events, or faculty details:
- Open the CBIT website in your browser.
- Use developer tools (press F12) to inspect the HTML structure.
- Identify the tag and class name of the section you want.
- Modify the script to target those tags (e.g., div, span, h2, etc.).
- 
License:
This project is intended for educational and personal use only. Please respect the website’s terms of service when scraping content.



