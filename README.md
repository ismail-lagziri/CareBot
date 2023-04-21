# CareBot

CareBot is a personalized and intelligent chatbot for medical needs, designed to assist users in finding information related to their health and well-being.

![Chatbot UI](/interface.png)

## Overview
The bot is trained on a dataset of intents, which are common questions or statements that a user might ask related to healthcare. The bot uses natural language processing (NLP) techniques to understand the user's query and provide an appropriate response.

## Installation
To use the bot, you will need to install the following dependencies:

- Python 3.6+
- NLTK
- Keras
- NumPy
- Streamlit

You can install the required packages using pip. Here's an example command:
```sh
pip install -r requirements.txt
```

## Training
The bot is trained on a dataset of intents, which are stored in the `intents.json` file. The training script can be found in `training.py`.

The script performs the following steps:

1. Tokenizes each word in the patterns
2. Adds the documents to the corpus
3. Adds the classes to the classes list
4. Lemmatizes and filters the words
5. Creates the bag of words
6. Builds and trains the neural network model
7. Saves the model and training history

You can run the training script using the following command:
```sh
python training.py
```


## Usage
To start the bot, run the following command:
```sh
python interface.py
streamlit run interface.py
```
The bot will launch in your browser. You can enter a question or statement in the text box and click "Rerun" to get a response.
