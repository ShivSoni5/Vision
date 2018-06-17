#!/usr/bin/python3

from subprocess import call

def make_todo(query):
    call(['todo',query])

def list_todo():
    return (call(['todo']))
    
