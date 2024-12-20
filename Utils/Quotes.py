import requests
import json

class Quotes:
    def __init__(self, string):
        if string == 'random':
            self.quote = self._random_quote()
        elif string == 'today':
            self.quote = self._today_quote()

    def get_quote(self):
        return self.quote

    def _random_quote(self) -> str:
        return self._return_quote("random")

    def _today_quote(self) -> str:
        return self._return_quote("today")

    @staticmethod
    def _return_quote(q) -> str:
        resp = requests.get(f'https://zenquotes.io/api/{q}')
        json_data = json.loads(resp.text)
        quote = json_data[0]['q']
        author = json_data[0]['a']
        full_phrase = f"*{quote}*\nby: `{author}`"
        return full_phrase