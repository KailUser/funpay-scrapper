import re
import requests
from bs4 import BeautifulSoup

class Chips():
    """
    Represents a Chips object.
    """

    def __init__(self, ID: int):
        """
        Initializes the Chips object.

        Args:
            ID (int): The ID of the chips.
        """
        self.id = str(ID)
        self.url = f"https://funpay.com/chips/{self.id}/"
        self.data = None

        self.__get_data__()

    def __get_data__(self):
        """
        Retrieves the raw HTML data of the chips.

        Returns:
            str: The raw HTML data of the chips.

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

    def clean_text(self, text):
        """
        Cleans the given text by removing multiple whitespaces.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        return re.sub(r"\s+", " ", text)
    
    
    def chips_links(self, max_limit=10):
        """
        Returns a dictionary of chips links.

        Args:
            max_limit (int, optional): The maximum number of chips links to return. Defaults to 10.

        Returns:
            dict: A dictionary of chips links.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        chips_list = soup.find("div", class_="tc table-hover table-clickable showcase-table tc-sortable tc-lazyload showcase-has-promo")
        chips = {}
        if chips_list:
            chips_list = chips_list.find_all("a", class_="tc-item")[:max_limit]
            for i, chip in enumerate(chips_list):
                href = chip.get("href")
                server = chip.find("div", class_="tc-server hidden-xxs").text
                seller = chip.find("div", class_="tc-user").find("div", class_="media-user-name").text
                amount = chip.find("div", class_="tc-amount").text.strip().replace(" ", "")
                price = chip.find("div", class_="tc-price").find("div").text.strip()

                chips[str(i+1)] = {
                    "href": href,
                    "server": self.clean_text(server),
                    "seller": self.clean_text(seller),
                    "amount": int(999831029) if str(amount) == "∞" else int(amount),
                    "price": float(price.split(sep=" ")[0])
                }
        return chips    

