from fixtures.answers import *

import base64

from src.pandas_questions import (
    question_1,
    question_2,
    question_3,
)

def test_question_1() -> None:
    answer = question_1()
    enc_answer = str(answer).encode("utf-8")
    assert base64.b64encode(enc_answer).decode('utf-8') == answer_1 


def test_question_2() -> None:
    answer = question_2()
    enc_answer = str(answer).encode("utf-8")
    assert base64.b64encode(enc_answer).decode('utf-8') == answer_2 


def test_question_3() -> None:
    answer = question_3()
    enc_answer = str(answer).encode("utf-8")
    assert base64.b64encode(enc_answer).decode('utf-8') == answer_3 

