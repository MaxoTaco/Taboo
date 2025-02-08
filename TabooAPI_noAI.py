import requests

# Define the base URL
base_url = "https://www.taboocardsapi.com/api/"

# Function to call the /api/cards endpoint
def get_all_cards():
    url = f"{base_url}cards"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Print the response JSON if successful
        print("Cards:", response.json())
    else:
        print(f"Failed to fetch cards. Status code: {response.status_code}")

# Function to call the /api/cards/random endpoint
def get_random_card():
    url = f"{base_url}cards/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Print the response JSON if successful
        print("Random Card:", response.json())
    else:
        print(f"Failed to fetch random card. Status code: {response.status_code}")

# Calling the functions
#get_all_cards()
get_random_card()
