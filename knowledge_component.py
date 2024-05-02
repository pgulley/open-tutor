import random

class KC():
    #Knowledge Component. 
    #Starting some of the SWENG over here, maybe getting ahead of myself. 
    chapter: str
    title: str
    definition: str

    def __init__(self, chapter, title, definition):
        self.chapter = chapter
        self.title = title
        self.definition = definition
        self.context = []
        self.learning_objectives = {
            "Knowledge":0,
            "Understand":0,
            "Apply":0,
            "Analyze":0
        }

    def get_context(self):
        if len(self.context) == 0:
            return "No Context"
        else:
            return random.choice(self.context).full_text

    def __repr__(self):
        return f"{self.title} : {self.definition[:20]}..."

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



