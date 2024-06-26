import requests
from bs4 import BeautifulSoup

class Profile:
    """
    Class representing a Funpay profile.

    Attributes:
        id (int): The ID of the profile.

    Methods:
        get_data(): Retrieves the raw HTML data of the profile.
        rating(): Returns the rating of the profile.
        nickname(): Returns the nickname of the profile.
        offers(): Returns a list of offers made by the profile.
        reviews(max_limit=10): Returns a dictionary of reviews made by the profile.
    """

    def __init__(self, ID: int):
        self.id = ID
        self.url = f"https://funpay.com/users/{self.id}/"
        self.data = None

        self.__get_data__()

    def __get_data__(self):
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
            self.__get_data__()
        soup = BeautifulSoup(self.data, "html.parser")
        rating_element = soup.find("div", class_="rating-value text-nowrap inline-block-vat mr10")
        if rating_element:
            try:
                rating_text = rating_element.find("span", class_="big").text
                return float(rating_text)
            except:
                return str(rating_text)
        return None

    def nickname(self):
        """
        Returns the nickname of the profile.

        Returns:
            str or None: The nickname of the profile, or None if not found.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        nickname_element = soup.find("span", class_="mr4")
        return nickname_element.text if nickname_element else None

    def offers(self):
        """
        Returns a list of offers made by the profile.

        Returns:
            list: A list of offers made by the profile.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        offers_list = soup.find("div", class_="mb20")
        offers_title = offers_list.find_all("div", class_="offer-list-title")
        return [offer.find("h3").text for offer in offers_title]

    def reviews(self, max_limit=10):
        """
        Returns a dictionary of reviews made by the profile.

        Args:
            max_limit (int, optional): The maximum number of reviews to return. Defaults to 10.

        Returns:
            dict: A dictionary of reviews made by the profile.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        reviews_list = soup.find_all("div", class_="review-compiled-review")
        reviews = {}
        for i, review in enumerate(reviews_list):
            if i == max_limit:
                break
            rating = review.find("div", class_="review-item-rating visible-xs").find("div", class_="rating").find("div").get("class")[0].replace("rating", "")
            text = review.find("div", class_="review-item-text").text.strip()
            reviews[str(i+1)] = {"rating": rating, "text": text}
        return reviews
