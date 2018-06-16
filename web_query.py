#!/usr/bin/python3

import webbrowser as wb
import wikipedia as wiki

def google(query):
    wb.open_new_tab(f'https://www.google.com/search?q={query}')


def wiki_search(query):
    try:
        wiki_say = wiki.summary(query)
        return(wiki_say)
    except wiki.exceptions.DisambiguationError:
        return('Try to google it because it is very confusing for me')
