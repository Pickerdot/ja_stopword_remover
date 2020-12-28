# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="ja_stopword_remover",
    version="0.2.3",
    description="形態素解析後の日本語の文のリストからストップワードを除去するためのモジュール",
    long_description=readme,
    author="picker.",
    author_email="picker@pickerlav.jp",
    url="https://pickerlab.net/",
    license="MIT",
    packages=["ja_stopword_remover"],
    include_package_data=True,
)
