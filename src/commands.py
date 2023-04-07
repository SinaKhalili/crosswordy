import json
import os
import textwrap

import openai

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY


def command_handler(body):
    """
    Dispatch to the appropriate command handler.
    """
    command = body["data"]["name"]
    message = body["data"]["options"][0]["value"]

    if command == "word":
        return word(message)
    elif command == "hint":
        return hint(message)
    else:
        return {"statusCode": 400, "body": json.dumps("unhandled command")}


def word(user_word):
    """
    Return a crossword hint for the given message.
    """
    prompt = f"""
    Create a crossword hint for the given message. It will act as the answer
    to the crossword hint you create.
    Respond with just the hint. You can use classic
    tropes from the New York Times crossword, like rhetorical questions,
    puns, allusions, or whatever crossword tropes you like.
    
    Answer: {user_word}
    Hint: ____
    (Reply with just the hint.)
    """
    prompt = textwrap.dedent(prompt)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a bot to help solve and create crosswords.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    hint = response["choices"][0]["message"]["content"]

    data = {
        "content": "",
        "embeds": [
            {
                "type": "rich",
                "title": f"{user_word}",
                "description": f"{hint}",
                "color": 0x000000,
            }
        ],
    }

    return {
        "statusCode": 200,
        "body": json.dumps({"type": 4, "data": data}),
    }


def hint(user_hint):
    """
    Return a crossword word for the given hint.
    """
    prompt = f"""
    Create a crossword like answer for the given message. You can
    interpret the message as a crossword hint.
    Respond with just the word. You can use classic
    tropes from the New York Times crossword, like rhetorical questions,
    puns, allusions, or whatever crossword tropes you like.
    In crosswords, the answer is usually a word, but it can be a phrase.
    Its written in all caps and without punctuation or spaces.
    
    Hint: {user_hint}
    Answer: ____
    (Reply with just the answer.)
    """
    prompt = textwrap.dedent(prompt)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a bot to help solve and create crosswords.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    word = response["choices"][0]["message"]["content"]

    data = {
        "content": "",
        "embeds": [
            {
                "type": "rich",
                "title": f"{word}",
                "description": f"{user_hint}",
                # the new york times crossword color
                "color": 0x000000,
            }
        ],
    }

    return {
        "statusCode": 200,
        "body": json.dumps({"type": 4, "data": data}),
    }
