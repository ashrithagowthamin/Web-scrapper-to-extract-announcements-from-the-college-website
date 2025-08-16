from bs4 import BeautifulSoup
import requests

# Step 1: Define the target URL
url = "https://www.cbit.ac.in/"

try:
    # Step 2: Send a GET request to the website
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # Step 3: Check if the request was successful
    if response.status_code == 200:
        # Step 4: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Step 5: Find all <li> and <a> tags with visible text
        tags = soup.find_all(['li', 'a'])

        # Step 6: Write extracted text to a file
        with open("script.txt", "w", encoding="utf-8") as file:
            count = 0
            for tag in tags:
                text = tag.get_text(strip=True)
                if text:
                    print(text)
                    file.write(text + "\n")
                    count += 1

            if count == 0:
                print("⚠️ No visible text found in <li> or <a> tags.")
            else:
                print(f"✅ Successfully saved {count} items to script.txt")

    else:
        print("❌ Failed to retrieve the page. Please check the URL or your internet connection.")

except Exception as e:
    print(f"🚨 An error occurred: {e}")