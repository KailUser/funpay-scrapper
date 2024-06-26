import requests
from bs4 import BeautifulSoup


class Profile:
    """
    Class for representing a Funpay profile.

    Attributes:
        id (str): The ID of the profile.
        url (str): The URL of the profile.
        data (str): The raw HTML data of the profile.

    Methods:
        get_data(): Retrieves the raw HTML data of the profile.
        rating(): Returns the rating of the profile.
        nickname(): Returns the nickname of the profile.
        offers(): Returns a list of offers made by the profile.
    """

    def __init__(self, ID: int):
        self.id = str(ID)
        self.url = f"https://funpay.com/users/{self.id}/"
        self.data = None

        self.get_data()
    def get_data(self):
        """
        Retrieves the raw HTML data of the profile.

        Returns:
            str: The raw HTML data of the profile.

        Raises:
            Exception: If there is an error getting the data.
        """
        if self.data is None:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.text
            else:
                raise Exception(f"Error getting data for ID: {self.id}. Status code: {response.status_code}")
        return self.data

    def rating(self):
        """
        Returns the rating of the profile.

        Returns:
            float or None: The rating of the profile, or None if not found.
        """
        if self.data is None:
            self.get_data()
        soup = BeautifulSoup(self.data, "html.parser")
        rating_element = soup.find("div", class_="rating-value text-nowrap inline-block-vat mr10")
        if rating_element:
            try:
                rating_text = rating_element.find("span", class_="big").text
                return float(rating_text)
            except:
                return str(rating_text)
        else:
            return None

    def nickname(self):
        """
        Returns the nickname of the profile.

        Returns:
            str or None: The nickname of the profile, or None if not found.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        nickname_element = soup.find("span", class_="mr4")
        if nickname_element is not None:
            return nickname_element.text
        else:
            return None

    def offers(self):
        """
        Returns a list of offers made by the profile.

        Returns:
            list: A list of offers made by the profile.
        """
        # print(f"Getting offers for ID: {self.id}")
        soup = BeautifulSoup(self.data, "html.parser")
        offers_list = soup.find("div", class_="mb20")
        offers_title = []
        if offers_list is not None:
            offers_title = offers_list.find_all("div", class_="offer-list-title")
        offers = []
        for offer in offers_title:
            offers.append(offer.find("h3").text)
        return offers

    # def reviews(self, max_limit=10):
        # soup