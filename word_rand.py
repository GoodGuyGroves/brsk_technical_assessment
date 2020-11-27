"""Scrabble sentence and word substituter"""
import aiohttp
import random


class WordRand:
    """Returns a new sentence with each word replaced with a new word of the same starting letter and length"""

    def __init__(self):
        self.all_words_dict = {}

    async def download_words(self, words_url):
        """Check if words.txt exists locally, else downloads words from URL"""
        try:
            with open('words.txt', 'r') as local_file:
                content = ''.join(local_file.readlines())
                await self.create_dict(content)
        except FileNotFoundError as e:
            print('Found error', e)
            async with aiohttp.ClientSession() as session:
                async with session.get(words_url) as response:
                    body_text = await response.text()
                    await self.create_dict(body_text)
            with open('words.txt', 'w') as local_file:
                local_file.write(body_text)

    async def create_dict(self, words_dict: str):
        """Takes multiple words as a single string and sorts into a dictionary"""
        for word in words_dict.splitlines():
            first_letter = word[0]
            word_length = len(word)
            self.all_words_dict.setdefault(first_letter, {}).setdefault(
                word_length, []
            ).append(word)

    async def random_replace_word(self, word: str) -> str:
        """Returns a random word matching the input words starting letter and length"""
        try:
            return random.choice(self.all_words_dict[word[0]][len(word)])
        except KeyError as e:
            print("whelp, too many letters: ", e)
            return word

    async def randomise_sentence(self, sentence: str) -> str:
        """Substitutes old word for new word"""
        new_sentence = []
        for word in sentence.split():
            result = await self.random_replace_word(word)
            new_sentence.append(result)
        return " ".join(new_sentence)

# async def main(user_input):
#     """Kicks off the show"""
#     words_url = "http://www.mieliestronk.com/corncob_lowercase.txt"
#     scrabble = WordRand()
#     await scrabble.download_words(words_url)
#     new_sentence = await scrabble.randomise_sentence(user_input)
#     print(new_sentence)


# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main('test example'))
