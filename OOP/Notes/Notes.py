import re
_WORD_RE = re.compile(r"\b\w+\b", flags = re.UNICODE)
def _tokenize(text: str):
    return (m.group(0).lower() for m in _WORD_RE.finditer(text or ""))

class Note:
    def __init__(self, title: str, content: str, date: str):
        self.title = title
        self.content = content
        self.date = date

        self.keywords = set()

        for word in (title + content):
            self.keywords.add(word)
    
    def semanticSearch(self, keyword: str) -> bool:
        if keyword in self.keywords:
            return True 
        return False 
    
    def __repr__(self) -> str:
        return f"Title: {self.title} \n Content: {self.content} \n Date Created: {self.date}"



class NoteManager:
    def __init__(self):
        self.notes = {}
    
    def addNote(self, note: Note):
        if note.title in self.notes:
            return False 
    
        self.notes[note.title] = Note
        return True 
    
    def delNote(self, note: Note):
        if note.title not in self.notes:
            return False
        del self.notes[note.title]
        return True
    
    def listNotes(self) -> None:
        for _, note in self.notes:
            print(note) 
        
    def searchNotes(self, keyword: str) -> list[Note]:
        result = []

        for _, note in self.notes:
            if note.semanticSearch(keyword):
                result.append(note)
            
        return result 
    




    


