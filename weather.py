import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

search = input("Enter the city name: ")
url = f"https://www.google.com/search?q=weather+{search}&hl=en"  # Force English results

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors

    soup = BeautifulSoup(response.text, 'html.parser')

    # Attempt to extract weather data
    location = soup.find('div', id='wob_loc')
    time = soup.find('div', id='wob_dts')
    temp = soup.find('span', id='wob_tm')
    condition = soup.find('span', id='wob_dc')

    # Check if all elements exist
    if None in (location, time, temp, condition):
        print("Error: Could not find weather data. Possible issues:")
        print("- Google’s HTML structure changed (try updating selectors)")
        print("- Invalid city name or no weather data available")
        print("- Regional Google restrictions (try a VPN)")
    else:
        print(f"Weather in {location.text}")
        print(f"Time: {time.text}")
        print(f"Temperature: {temp.text}°C")
        print(f"Condition: {condition.text}")

except requests.RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")