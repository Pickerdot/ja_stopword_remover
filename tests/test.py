import sys
import os
from sklearn.pipeline import Pipeline

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ja_stopword_remover.remover import SKStopwordRemover, StopwordRemover

# 多田なの(@ohta_nano)さんの詩です。
text_list = [
    [
        "僕",
        "たち",
        "は",
        "プラネタリウム",
        "に",
        "立て籠もり",
        "夜明け",
        "の",
        "シーン",
        "だけ",
        "繰り返す",
    ],
    [
        "桜",
        "って",
        "「",
        "さくら",
        "」",
        "って",
        "読む",
        "って",
        "あなた",
        "から",
        "教えて",
        "もらう",
        "人",
        "に",
        "なりたい",
    ],
]


def test_StopwordRemover():
    stopwordRemover = StopwordRemover()

    pre_num = len(text_list[0])

    text_list_result = stopwordRemover.remove(text_list)

    post_num = len(text_list_result[0])

    assert pre_num > post_num


def test_SKStopwordRemover():

    sKKStopwordRemover = SKStopwordRemover(one_character=False)

    step = [("StopwordRemover", sKKStopwordRemover)]

    pipe = Pipeline(steps=step)

    pipe.fit(text_list)

    text_list_result = pipe.transform(text_list)

    assert len(text_list_result[0]) < len(text_list[0])


def test_choose_parts():
    stopwordRemover = StopwordRemover()
    stopwordRemover.choose_parts(
        demonstrative=False,
        symbol=False,
        verb=False,
        one_character=False,
        postpositional_particle=False,
        slothlib=True,
        auxiliary_verb=False,
        adjective=False,
    )
