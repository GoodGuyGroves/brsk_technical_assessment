#!/usr/bin/env python
"""Combines word_rand.py with Typer to create a CLI tool"""
import asyncio
import word_rand
import typer

app = typer.Typer()


@app.command()
def replace(sentence: str, upper: bool = False):
    # This doc string is being used for --help output
    """
    - Input a word to be replaced by another word that starts with the same first letter and is the same length.

    - If you input a sentence, every word in that sentence will be replaced. Make sure to quote your sentence.
    """
    sentence_len = len(sentence.split())
    if sentence_len > 1:
        verbage = "sentence"
    else:
        verbage = "word"

    result = asyncio.run(main(sentence))
    if upper:
        typer.secho(f"Old {verbage}: {sentence.upper()}", fg=typer.colors.BLUE)
        typer.secho(f"New {verbage}: {result.upper()}", fg=typer.colors.GREEN)
    else:
        typer.secho(f"Old {verbage}: {sentence}", fg=typer.colors.BLUE)
        typer.secho(f"New {verbage}: {result}", fg=typer.colors.GREEN)


async def main(user_input):
    """Kicks off the show"""
    words_url = "http://www.mieliestronk.com/corncob_lowercase.txt"
    scrabble = word_rand.WordRand()
    await scrabble.download_words(words_url)
    new_sentence = await scrabble.randomise_sentence(user_input)
    return new_sentence


if __name__ == "__main__":
    app()
