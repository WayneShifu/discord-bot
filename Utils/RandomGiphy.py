import requests
import random

class RandomGiphy:
    def __init__(self, giphy_api_key, _message):
        self.giphy_api_key = giphy_api_key
        self.message = _message

    def _fetch_gif_by_keyword(self, keyword):
        url = f'https://api.giphy.com/v1/gifs/search?api_key={self.giphy_api_key}&q={keyword}&limit=1'
        response = requests.get(url)
        data = response.json()

        if data['data']:
            return data['data'][0]['images']['original']['url']
        else:
            print(f'No GIFs found for keyword: {keyword}')
            return None

    @staticmethod
    def _should_send_gif():
        rn = random.randint(1, 20)
        print(f"giphy random number: {rn}")
        return rn == 1

    def _get_gif_url(self):
        keyword = random.choice(self.message.content.split())
        return self._fetch_gif_by_keyword(keyword)

    async def send(self):
        if self._should_send_gif():
            gif_url = self._get_gif_url()
            if gif_url:
                await self.message.channel.send(f'{gif_url}\nPowered by GIPHY')