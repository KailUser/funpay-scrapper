import re
import requests
from bs4 import BeautifulSoup


class Offers:
    """
    Class for scraping offers from funpay.com.

    Attributes:
        url (str): The URL for the offer.
        data (str or None): The raw HTML data of the offer.

    Methods:
        __get_data__(): Retrieves the raw HTML data of the offer.
        clean_text(text): Cleans the provided text.
        get_offer(): Returns a dictionary with the offer details.
    """
    def __init__(self, id):
        """
        Creates an instance of the Offers class.

        Args:
            id (int): The ID of the offer.
        """
        self.url = f"https://funpay.com/lots/offer?id={id}"
        self.data = None

        self.__get_data__()

    def __get_data__(self):
        """
        Retrieves the raw HTML data of the offer.

        Returns:
            str: The raw HTML data of the offer.

        Raises:
            Exception: If there is an error getting the data.
        """
        if self.data is None:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.text
            else:
                raise Exception(f"Error getting data. Status code: {response.status_code}")
        return self.data

    def clean_text(self, text):
        """
        Cleans the provided text.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        return re.sub(r"\s+", " ", text).strip()

    def get_offer(self):
        """
        Returns a dictionary with the offer details.

        Returns:
            dict: A dictionary with the offer details.
                - auto_delivery (str): The availability of auto-delivery.
                - seller (str): The name of the seller.
                - cost_per_lot (str): The cost per lot.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        auto_delivery = "available" if bool(soup.find("div", class_="offer-header-auto-dlv-label")) else "unavailable"
        seller = soup.find("div", class_="media-user-name").find("a").text
        payment_value = soup.find("span", class_="payment-value")
        cost_per_lot = payment_value.text.split("₽")[1].strip() if payment_value else "Undefined"

        return {
            "auto_delivery": auto_delivery,
            "seller": seller,
            "cost_per_lot": cost_per_lot
        }

