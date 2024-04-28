import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    def display_all_info(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        for country in self.data:
            print(f"Country: {country['name']['common']}")
            print(f"Currency: {country['currencies'][list(country['currencies'].keys())[0]]['name']}")
            print(f"Currency Symbol: {country['currencies'][list(country['currencies'].keys())[0]]['symbol']}")
            print("-" * 30)

    def display_dollar_countries(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        dollar_countries = [country['name']['common'] for country in self.data if 'USD' in country['currencies']]
        print("Countries with DOLLAR as currency:")
        print(", ".join(dollar_countries))

    def display_euro_countries(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        euro_countries = [country['name']['common'] for country in self.data if 'EUR' in country['currencies']]
        print("Countries with EURO as currency:")
        print(", ".join(euro_countries))

# URL
url = "https://restcountries.com/v3.1/all"
country_info_fetcher = CountryInfoFetcher(url)

# Fetch data from the URL
country_info_fetcher.fetch_data()

# Display all information
country_info_fetcher.display_all_info()

# Display countries with DOLLAR as currency
country_info_fetcher.display_dollar_countries()

# Display countries with EURO as currency
country_info_fetcher.display_euro_countries()