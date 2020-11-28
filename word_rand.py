"""Scrabble sentence and word substituter"""
import aiohttp
import random
import logging

logger = logging.getLogger("word_rand")
logger.setLevel(logging.DEBUG)

log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")

file_handler = logging.FileHandler(filename="word_rand.log", encoding="utf-8", mode="a")
file_handler.setFormatter(log_format)

logger.addHandler(file_handler)


class WordRand:
    """Returns a new sentence with each word replaced with a new word of the same starting letter and length"""

    def __init__(self):
        self.all_words_dict = {}

    async def download_words(self, words_url):
        """Check if words.txt exists locally, else downloads words from URL"""
        logger.debug("Looking for words.txt locally, else downloading from URL")
        try:
            with open("words.txt", "r") as local_file:
                logger.debug("Found words.txt, reading words from local file instead")
                content = "".join(local_file.readlines())
                await self.create_dict(content)
        except FileNotFoundError as e:
            logger.error("Error %s", e)
            logger.debug(
                "No words.txt found locally, downloading words from url: %s", words_url
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(words_url) as response:
                    body_text = await response.text()
                    await self.create_dict(body_text)
            with open("words.txt", "w") as local_file:
                logger.debug("Storing words locally in words.txt")
                local_file.write(body_text)

    async def create_dict(self, words_dict: str):
        """Takes multiple words as a single string and sorts into a dictionary"""
        logger.debug("Building dictionary from provided words")
        for word in words_dict.splitlines():
            first_letter = word[0]
            word_length = len(word)
            self.all_words_dict.setdefault(first_letter, {}).setdefault(
                word_length, []
            ).append(word)

    async def random_replace_word(self, word: str) -> str:
        """Returns a random word matching the input words starting letter and length"""
        logger.debug(
            "Finding replacement word starting with %s that is %i letters long",
            word[0].upper(),
            len(word),
        )
        try:
            new_word = random.choice(self.all_words_dict[word[0]][len(word)])
            logger.debug("Replacing '%s' with '%s'", word, new_word)
            return new_word
        except KeyError as e:
            logger.error("whelp, too many letters for word '%s': %s", word, e)
            return word

    async def randomise_sentence(self, sentence: str) -> str:
        """Substitutes old word for new word"""
        new_sentence = []
        for word in sentence.split():
            result = await self.random_replace_word(word)
            new_sentence.append(result)
        new_sentence = " ".join(new_sentence)
        logger.debug("Replacing sentence '%s' with '%s'", sentence, new_sentence)
        return new_sentence
