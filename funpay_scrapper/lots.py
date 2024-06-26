import re
import requests
from bs4 import BeautifulSoup

class Lots:
    """
    Class for representing a Funpay Lots object.

    Attributes:
        id (str): The ID of the lots.
        url (str): The URL of the lots.
        data (str): The raw HTML data of the lots.

    Methods:
        get_data(): Retrieves the raw HTML data of the lots.
        clean_text(text): Cleans the text by removing extra whitespace and stripping.
        lots_links(max_limit=10): Returns a dictionary of lots links.
        sort_lots(sort_by="lowest"): Sorts the lots links by cost.
    """
    def __init__(self, ID: int):
        """
        Initializes the Lots object.

        Args:
            ID (int): The ID of the lots.
        """
        self.id = str(ID)
        self.url = f"https://funpay.com/lots/{self.id}/"
        self.data = None

        self.get_data()

    def get_data(self):
        """
        Retrieves the raw HTML data of the lots.

        Returns:
            str: The raw HTML data of the lots.

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
        Cleans the text by removing extra whitespace and stripping.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        return re.sub(r'\s+', ' ', text).strip()

    def lots_links(self, max_limit=10):
        """
        Returns a dictionary of lots links.

        Args:
            max_limit (int, optional): The maximum number of lots links to return. Defaults to 10.

        Returns:
            dict: A dictionary of lots links.
        """
        soup = BeautifulSoup(self.data, "html.parser")
        lots = soup.find("div", class_="tc table-hover table-clickable tc-short showcase-table tc-lazyload tc-sortable showcase-has-promo") or soup.find("div", class_="tc table-hover table-clickable tc-short showcase-table tc-lazyload tc-sortable")
        lots_links = {}
        if lots:
            lots = lots.find_all("a", class_="tc-item")[:max_limit]
            for i, lot in enumerate(lots):
                href = lot.get("href")
                cost_element = lot.find("div", class_="tc-price")
                seller_element = lot.find("div", class_="tc-user")
                seller_element = seller_element.find("div", class_="media-body")
                seller_element = seller_element.find("div", class_="media-user-name")

                cost = self.clean_text(cost_element.text) if cost_element else 'Unknown'
                seller = self.clean_text(seller_element.text) if seller_element else 'Unknown'
                item_name = str(i+1)

                lots_links[item_name] = {
                    "href": href,
                    "cost": cost,
                    "seller": seller
                }
        return lots_links
    
    def sort_lots(self, sort_by="lowest"):
        """
        Sorts the lots links by cost.

        Args:
            sort_by (str, optional): The order to sort the lots by. Defaults to "lowest".

        Returns:
            dict: The sorted lots links.

        Raises:
            ValueError: If the sort_by parameter is invalid.
        """
        lots_links = self.lots_links()
        if sort_by == "lowest":
            lots_links = dict(sorted(lots_links.items(), key=lambda x: float(x[1]["cost"].split(sep=" ")[0])))
        elif sort_by == "highest":
            lots_links = dict(sorted(lots_links.items(), key=lambda x: float(x[1]["cost"].split(sep=" ")[0]), reverse=True))
        else:
            raise ValueError("Invalid sort_by parameter. Only 'lowest' and 'highest' are accepted.")
        return lots_links
