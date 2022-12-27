from enum import Enum
import re

class QueryType(Enum):
    URL = "url"
    QUESTION = "question"
    SENTENCE = "sentence"
    PARAGRAPH = "paragraph"

PARAGRAPH_pattern = re.compile("[\w\!\,\"\#\$\%\&\(\)\*\+\/\:\;\<\=\>\@\^\`\{\|\}\~\t ]+.")

URL_pattern = re.compile("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")

QUESTION_pattern = re.compile("[^.!?]+\?")

def classify_query_service(q_text:str):
    """
    return enum based on type of query text

    args: q_text : str
    retrun type of query : str

    first priority is URL check because URL and paragraph may have more than one '.'
    next is if its not URL then if there are more than one sentences than its paragraph
    next between question and sentence if its ending with '?' then its question else its sentence.
    """
    _q_text = (q_text + '.')[:-1]
    sentences_match = re.findall(PARAGRAPH_pattern, _q_text)
    
    if re.match(URL_pattern, q_text):
        return QueryType.URL
    elif len(sentences_match) > 1:
        return QueryType.PARAGRAPH
    elif re.match(QUESTION_pattern, q_text):
        return QueryType.QUESTION
    else:
        return QueryType.SENTENCE