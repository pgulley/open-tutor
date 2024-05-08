import random
import uuid
from enum import Enum

class Objectives(Enum):
    Knowledge = 1
    Understand = 2
    Apply = 3
    Analyze = 4

class LO():
    def __init__(self, objective):
        self.title = objective.name
        self.ok = False #Mastered
        self.active = False #Currently under study
        self.grade = 0 #Track some bayseian nonsense, tbd

    def json(self):
        return {
            "title":self.title,
            "active":self.active,
            "ok": self.ok,
            "grade":self.grade
        }



class KC():
    #Knowledge Component. 
    #Starting some of the SWENG over here, maybe getting ahead of myself. 
    chapter: str
    title: str
    definition: str

    def __init__(self, chapter, title, definition):
        self.id = uuid.uuid4().hex
        self.chapter = chapter
        self.title = title
        self.definition = definition
        self.context = []

        self.learning_objectives = {o.name:LO(o) for o in list(Objectives)}
        self.learning_objectives["Knowledge"].active = True



    def get_context(self):
        if len(self.context) == 0:
            return "No Context"
        else:
            return random.choice(self.context).full_text

    def __repr__(self):
        return f"{self.title} : {self.definition[:20]}..."

    def json(self):
        return {
        'id':self.id,
        'title':self.title,
        'learning_objectives':[self.learning_objectives[o.name].json() for o in list(Objectives)] 

        }

class ContentExample():
    #A piece of sample text using the KC
    def __init__(self, chapter_slug, text):
        self.chapter = chapter_slug.split("-")[0]
        self.full_chapter = chapter_slug
        self.full_text = text

    def __repr__(self):
        return f"<text-content from chapter {self.chapter}: {self.full_text[:20]}>"

    def __contains__(self, item):
        return (item in self.full_text)



