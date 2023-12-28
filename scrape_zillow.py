import requests
from bs4 import BeautifulSoup

def get_number_of_rooms(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Adjust the tag and class based on Zillow's HTML structure
        rooms_tag = soup.find('span', class_='your-room-class')

        if rooms_tag:
            number_of_rooms = rooms_tag.text.strip()
            return number_of_rooms
        else:
            return "Number of rooms not found on the page."

    else:
        return "Failed to retrieve the page. Status code:", response.status_code

# Example URL of a Zillow house page
zillow_url = "https://www.zillow.com/example-house-url"

number_of_rooms = get_number_of_rooms(zillow_url)
print("Number of rooms:", number_of_rooms)
