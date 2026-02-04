import requests


def get_random_dog():
    """
    Fetch a random dog image URL
    """
    url = "https://dog.ceo/api/breeds/image/random"
    
    response = requests.get(url)
    
    # Get the JSON data from the response
    data = response.json()
    
    # Return the image URL (it's in data['message'])
    return data['message']

def main():
    print("🐕 Welcome to Random Dog Pictures! 🐕\n")
    
    while True:
        # Call get_random_dog() and save the result
        dog_url = get_random_dog()
        
        # Print the dog image URL
        print(f"Here's your random dog: {dog_url}\n")
        
        # Ask user if they want another dog
        answer = input("Want another dog? (yes/no): ").lower()
        
        # If they say 'no', break the loop
        if answer == 'no' or answer == 'n':
            print("\nThanks for looking at dogs! 🐾")
            break

# Run the program
if __name__ == "__main__":
    main()