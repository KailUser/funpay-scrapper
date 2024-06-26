import re
import requests
from bs4 import BeautifulSoup


class Chat:
    def __init__(self):
        self.url = "https://funpay.com/chat/?node=flood"
        self.data = None

        self.__get_data__()

    def __get_data__(self):
        if self.data is None:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.text
            else:
                raise Exception(f"Error getting data. Status code: {response.status_code}")
    
    def clean_text(self, text):
        return re.sub(r"\s+", " ", text)
    
    def chat_messages(self, max_limit=10):
        soup = BeautifulSoup(self.data, "html.parser")
        message_history = soup.find("div", class_="chat-message-list")
        dict_of_messages = {}
        i = 0
        for message in message_history.find_all("div", class_="chat-msg-item chat-msg-with-head") or message_history.find_all("div", class_="chat-msg-item"):
            if i == max_limit:
                break
            text = message.find("div", class_="chat-msg-text").text
            if text == "The message has been hidden." or text == "Сообщение скрыто.":
                continue
            sender = message.find("div", class_="media-user-name").find("a").text
            dict_of_messages[i] = {"sender": sender, "text": text}
            i += 1
        
        return dict_of_messages

class Home():
    def __init__(self):
        self.url = "https://funpay.com/"
        self.data = None

        self.__get_data__()

    def __get_data__(self):
        if self.data is None:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.text
            else:
                raise Exception(f"Error getting data. Status code: {response.status_code}")
    
    def find_game(self, name: str = None):
        soup = BeautifulSoup(self.data, "html.parser")
        for i in soup.find_all("div", class_="game-title"):
            if name in i.text:
                return True, i.find("a")["href"]
        return False, None