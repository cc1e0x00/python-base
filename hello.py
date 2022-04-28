#!/usr/bin/env python3

""" "Hello world" multi-languages.

Based on languages configured in ENV "LANG".

How to use:

Set your variable LANG in a correct way.

Example:
    
    export LANG=en_US.UTF-8
    export LANG=pt_BR

Run
    python3 hell0.py
    ou
    ./hello.py

"""
__version__  = "0.0.1"
__author__ = "cc1e0x00"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, Word!"


if  current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg - "Bonjour Monde!"

print(msg)
