# brsk_technical_assessment
My submission for the brsk.co.uk technical assessment

[Original tech assessment](https://gitlab.com/brsk-uk/technical-assessment)

### Notes

- I started by putting the downloaded words into a Pandas DataFrame but using raw Python dicts turned out to be quicker and 'cheaper' overall
# Instructions

Copy and paste the below commands into your terminal based on the operating system / tool you are using to install Pipenv, a tool to create and manage Python virtual environments.
## Installing pipenv

### Ubuntu/Debian

```
sudo apt install pipenv
```

### Fedora

```
sudo dnf install pipenv
```

### Pipx

```
pipx install pipenv
```

### Homebrew

```
brew install pipenv
```

## Activating Python virtual environment

Now that you have Pipenv installed, you can open the directory where `scrabble.py` exists and in your terminal run the following command:
```
pipenv shell
```
The above command will create your python virtual environment and install the Python packages required to make `scrabble.py` run.

## Executing CLI tool

Each time you need to run `scrabble.py` you have to first make sure your Python virtual environment is running. To do so, it's the same command as the above. Make sure you are in the directory where `scrabble.py` exists and run:
```
pipenv shell
```

With your Python virtual environment activated, you can run `scrabble.py` in two ways, you can either use `python` to execute the script or you can run the script directly using the 'dot-slash' (`./`) method.

The script `scrabble.py` can only take a single argument, so if you pass `scrabble.py` multiple words to substitute, make sure you please surround your whole sentence in quotes. If you only want to substitute a single word, surrounding in quotes is not 100% required but still good practice.

### Executing with `python`

Single word:
```
python scrabble.py armageddon
```

Multiple words:
```
python scrabble.py "lightly fried fish fillets"
```

### Executing using 'dot-slash'

Single word:
```
./scrabble.py gecko
```

Multiple words:
```
./scrabble.py "my awesome leopard gecko"
```

## Logging

If you ran `scrabble.py` to create a substitution that you forgot to write down but you also want to find out what the result was, `scrabble.py` will create a log file called `word_rand.log` that you can open in your text editor of choice that keeps track of all substitutions. Look for lines that state "Replacing sentence".

### Viewing `word_rand.log` on the command line

If you want to display all the text in your terminal, execute:
```
cat word_rand.log
```

If you want to browse the whole file (it may be large) execute:
```
less word_rand.log
```

### Example output in `word_rand.log`

This example was on the first run of `scrabble.py` and the input was "my awesome leopard gecko":

```
2020-11-28 17:45:49,098:DEBUG:word_rand: Looking for words.txt locally, else downloading from URL
2020-11-28 17:45:49,098:DEBUG:word_rand: Found words.txt, reading words from local file instead
2020-11-28 17:45:49,104:DEBUG:word_rand: Building dictionary from provided words
2020-11-28 17:45:49,122:DEBUG:word_rand: Finding replacement word starting with M that is 2 letters long
2020-11-28 17:45:49,122:DEBUG:word_rand: Replacing 'my' with 'ms'
2020-11-28 17:45:49,122:DEBUG:word_rand: Finding replacement word starting with A that is 7 letters long
2020-11-28 17:45:49,122:DEBUG:word_rand: Replacing 'awesome' with 'attends'
2020-11-28 17:45:49,122:DEBUG:word_rand: Finding replacement word starting with L that is 7 letters long
2020-11-28 17:45:49,122:DEBUG:word_rand: Replacing 'leopard' with 'legible'
2020-11-28 17:45:49,122:DEBUG:word_rand: Finding replacement word starting with G that is 5 letters long
2020-11-28 17:45:49,122:DEBUG:word_rand: Replacing 'gecko' with 'greet'
2020-11-28 17:45:49,122:DEBUG:word_rand: Replacing sentence 'my awesome leopard gecko' with 'ms attends legible greet'
```