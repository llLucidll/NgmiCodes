import pytest
from Notes import Note, NoteManager
## Tests for the Note Class


def test_init():
    note = Note("title", "content", "12-25-2004")
    assert note.title == "title" and note.content == "content" and note.date == "12-25-2004"

def test_semantic():
    note = Note("title", "content", "12-25-2004")

    assert note.semanticSearch("title") == True 
    assert note.semanticSearch("content") == True
    assert note.semanticSearch("This word does not exist") == False


## Tests for the NoteManager class


def test_add():
    noteManager = NoteManager()
    note = Note("title", "content", "12-25-2005")