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
    "return enum based on type of query text"
    _q_text = (q_text + '.')[:-1]
    sentences_match = re.findall(PARAGRAPH_pattern, _q_text)
    if len(sentences_match) > 1:
        return QueryType.PARAGRAPH
    elif re.match(URL_pattern, q_text):
        return QueryType.URL
    elif re.match(QUESTION_pattern, q_text):
        return QueryType.QUESTION
    else:
        return QueryType.SENTENCE