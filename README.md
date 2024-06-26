# Funpay Scrapper

This library provides convenient methods for scraping data from Funpay, a popular online marketplace for buying and selling game items.

### Profile
The `Profile` class represents a Funpay profile and provides methods for retrieving information about the profile.

- `get_data()`: Retrieves the raw HTML data of the profile.
- `rating()`: Returns the rating of the profile.
- `nickname()`: Returns the nickname of the profile.
- `offers()`: Returns a list of offers made by the profile.

### Lots
The `Lots` class represents a Funpay Lots object and provides methods for retrieving information about the lots.

- `get_data()`: Retrieves the raw HTML data of the lots.
- `clean_text(text)`: Cleans the text by removing extra whitespace and stripping.
- `lots_links(max_limit=10)`: Returns a dictionary of lots links.
- `sort_lots(sort_by="lowest")`: Sorts the lots links by cost.

## Examples

```python
from funpay_scrapper.profile import Profile
from funpay_scrapper.lots import Lots

profile = Profile(5682424) # Initializes the Profile object
print(profile.rating()) # Output: ?
print(profile.nickname()) # Output: Syirezz

print("----------------------------------------------------------------")

lots = Lots(1264) # Initializes the Lots object
x = lots.lots_links(10) # Returns a dictionary of lots links. The maximum number of lots links is 10 or more.
for key, value in x.items():
    print(key, value) # Prints the dictionary of lots links
# Output:
# 1 {'href': 'https://funpay.com/lots/offer?id=17094859', 'cost': '189.71 ₽', 'seller': 'zvadizz01'}
# 2 {'href': 'https://funpay.com/lots/offer?id=23577867', 'cost': '191.90 ₽', 'seller': 'N3CRO88'}
# 3 {'href': 'https://funpay.com/lots/offer?id=19861734', 'cost': '192.06 ₽', 'seller': 'KeyShop4ik'}
# 4 {'href': 'https://funpay.com/lots/offer?id=30402196', 'cost': '193.23 ₽', 'seller': 'cympaynopom'}
# 5 {'href': 'https://funpay.com/lots/offer?id=30190810', 'cost': '193.23 ₽', 'seller': 'ZhannaStewardess'}
# 6 {'href': 'https://funpay.com/lots/offer?id=17462750', 'cost': '194.09 ₽', 'seller': 'Bibba'}
# 7 {'href': 'https://funpay.com/lots/offer?id=17075913', 'cost': '195.55 ₽', 'seller': 'BoBka92PMT'}
# 8 {'href': 'https://funpay.com/lots/offer?id=30404335', 'cost': '195.57 ₽', 'seller': 'nikzpisdili'}
# 9 {'href': 'https://funpay.com/lots/offer?id=23581531', 'cost': '195.58 ₽', 'seller': 'GoodGameKeys'}
# 10 {'href': 'https://funpay.com/lots/offer?id=21583534', 'cost': '196.74 ₽', 'seller': 'Gastello29'}

print("----------------------------------------------------------------")
from funpay_scrapper.utils import Chat, Home

chat = Chat() # Initializes the Chat object
for message in chat.chat_messages():
    print(message, chat.chat_messages()[message]) # Prints the chat messages

home = Home() # Initializes the Home object
print(home.find_game("AFK Arena")) # Output: True, lINK(HREF)  | Warning! Please don't confuse chips id with lots id! 
```