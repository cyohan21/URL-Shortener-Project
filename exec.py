import random
import string
import json

class URLShortenerDatabase:
    def __init__(self):
        self.url_map = {}
        self.id = 1
    
    def view_url_map(self):
        if not self.url_map:
            print("URL map is empty.")
        else:
            print("URL Map:")
            print(json.dumps(self.url_map, indent=4)) # Added Pretty Print

    def generate_random_string(self, length=6):
        chars = string.ascii_letters + string.digits
        return 'https://short.ly/' + ''.join(random.choice(chars) for _ in range(length)) # Converted Shortened Code to Shortened URL
    
    def shorten_url(self, long_url):
        for id, data in self.url_map.items():
            if data["Long URL"] == long_url:
                print(f"URL already exists: {data['Short URL']}")
            return
            
        short_url = self.generate_random_string()
        self.url_map[self.id] = {"Long URL": long_url, "Short URL": short_url}
        self.id += 1
        return short_url
    
    def get_og_url(self, short_url):
        for data in self.url_map.values():
            if data["Short URL"] == short_url:
                return data["Long URL"]
        return "Invalid shortened URL."

class URLShortenerApp:

    def __init__(self):
        self.db = URLShortenerDatabase() # Composition rather than inheritance as im using the classes as front/backend separately.

    def main(self):

        prompt = """Welcome to the URL Shortener App! Please enter one of the following: 
        1: Shorten URL
        2: Get Original URL
        3: View URL Map
        4: Exit"""

        valid_responses = ['1', '2', '3', '4']

        while True:
            welcome_input = get_valid_input(prompt, valid_responses)

            if welcome_input == '1':
                self.shorten_url_input()
            elif welcome_input == '2':
                self.get_og_url_input()
            elif welcome_input == '3':
                self.db.view_url_map()
            elif welcome_input == '4':
                print('Goodbye!')
                exit()
    
    def shorten_url_input(self):
        long_url = input('Enter long URL: ')

        for id, data in self.db.url_map.items():
            if data["Long URL"] == long_url:
                print(f"Shortened URL already exists for this URL: {data['Short URL']}")
                return

        short_url = self.db.shorten_url(long_url)
        print(f"Shortened URL: {short_url}")

    def get_og_url_input(self):

        short_url = input('Enter shortened URL: ')
        og_url = self.db.get_og_url(short_url)
        print(f"Original URL: {og_url}")

def get_valid_input(prompt, valid_responses):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_responses:
            return user_input
        else:
            print("I didn't get that, sorry. Please try again.")


if __name__ == "__main__":
    URLShortenerApp().main()
