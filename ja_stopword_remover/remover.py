from .stop_words import Stopword
from sklearn.base import BaseEstimator, TransformerMixin

import copy


class StopwordRemover:
    """
    単語のリストからストップワードにあたる単語を除去して返します。
    """

    def __init__(
        self,
    ):
        self.demonstrative = True
        self.symbol = True
        self.verb = True
        self.one_character = True
        self.postpositional_particle = True
        self.slothlib = True
        self.auxiliary_verb = True
        self.adjective = True

    def choose_parts(
        self,
        demonstrative=False,
        symbol=False,
        verb=False,
        one_character=False,
        postpositional_particle=False,
        slothlib=False,
        auxiliary_verb=False,
        adjective=False,
    ):
        """
        ストップワードを品詞ごとに選びたい場合は、下記の品詞を表す変数にFalseを指定。
        stopwordRemover.remove(text_list, demonstrative=False)
        demonstrative：指示語　pronoun：こそあど言葉　symbol:記号　verb：動詞　one_character：一字
        postpositional_particle：助詞　adjective：形容詞　auxiliary_verb：助動詞　slothlib：slothlib収録語
        """

        self.demonstrative = demonstrative
        self.symbol = symbol
        self.verb = verb
        self.one_character = one_character
        self.postpositional_particle = postpositional_particle
        self.slothlib = slothlib
        self.auxiliary_verb = auxiliary_verb
        self.adjective = adjective

    def remove(self, text_list):
        """
        ストップワードを消去したい単語のリストを引数に指定してください。
        """
        stopword_list = []
        stopword = Stopword()
        if self.demonstrative:
            stopword_list.extend(stopword.demonstrative)

        if self.symbol:
            stopword_list.extend(stopword.symbol)

        if self.verb:
            stopword_list.extend(stopword.verb)

        if self.one_character:
            stopword_list.extend(stopword.one_character)

        if self.postpositional_particle:
            stopword_list.extend(stopword.postpositional_particle)

        if self.slothlib:
            stopword_list.extend(stopword.slothlib)

        if self.auxiliary_verb:
            stopword_list.extend(stopword.auxiliary_verb)

        if self.adjective:
            stopword_list.extend(stopword.adjective)

        stopword_list = list(set(stopword_list))

        removed_text_list = []

        y = copy.deepcopy(text_list)

        for text in y:
            for stopword in stopword_list:
                while stopword in text:
                    text.remove(stopword)

            removed_text = []
            for word in text:
                removed_text.append(word)

            removed_text_list.append(removed_text)

        return removed_text_list


class SKStopwordRemover(BaseEstimator, TransformerMixin, StopwordRemover):
    """
    単語のリストからストップワードにあたる単語を除去して返します。
    sl-learnのpipeline用です。
    """

    def __init__(
        self,
        demonstrative=True,
        symbol=True,
        verb=True,
        one_character=True,
        postpositional_particle=True,
        slothlib=True,
        auxiliary_verb=True,
        adjective=True,
    ):
        self.demonstrative = demonstrative
        self.symbol = symbol
        self.verb = verb
        self.one_character = one_character
        self.postpositional_particle = postpositional_particle
        self.slothlib = slothlib
        self.auxiliary_verb = auxiliary_verb
        self.adjective = adjective

    def fit(self, X, y=None):
        return self

    def transform(
        self,
        text_list,
    ):
        self.choose_parts(
            demonstrative=self.demonstrative,
            symbol=self.symbol,
            verb=self.verb,
            one_character=self.one_character,
            postpositional_particle=self.postpositional_particle,
            slothlib=self.slothlib,
            auxiliary_verb=self.auxiliary_verb,
            adjective=self.adjective,
        )
        return self.remove(text_list)
