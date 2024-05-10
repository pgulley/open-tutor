Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# open-tutor
Final Project for CS690, Intelligent Tutors. 

There is a working prototype now!


## Running

set an environment variable `OPENAI_API_KEY=yourapikey12345` - you can't use mine :) 

Then, to run, just:  `flask --app server --debug run`

Changes to the knowledge component object require rebuilding the knowledge graph- right now that's done just by re-running the `construct_knowledge_graph.ipynb` notebook. 

## The Induced Knowledge Graph
`construct_knowledge_graph.ipynb` documents the process of manually piecing together a 'knowledge graph' from the openstax intro to sociology textbook.
Basically, we find "key terms", then assembled every block of text that the key term appears in. each term dangles from the chapter that it's introduced in, and also has connections to all other terms that co-occur in the text we found it in. It's pretty slapdash- future work here might involve spending some time developing a smarter approach, but this will be enough to demo all the required functionality

## The "Student Model"
We use the knowledge graph as a basis of a student model, adding on learning objectives to each term. The student model can generate reccomendations for a path through the kg that serves as a curriculum. Currently working with sort of a random-walk approach- but the chapter data and the learning objective data can help steer that. 

## The Tutor
We use the content in the knowledge graph to generate prompts to an LLM, driving the system to generate question/answer pairs corresponding to the term, the text content, and the learning objective. We throw the question to the user and evaluate their response with another prompt to the llm.
One 'inner loop' of the tutor execution sees at least one feedback cycle with the student. The 'outerloop' corresponds to how the KG is navigated. 
Still figuring out exactly how the student model updates to reflect inner loop performance- but that's an ok open space for a class demo. 

Right now I have pretty good performance using openai's gpt3-turbo model in "completion" mode. Ideally, I think, this would be able to ship with a local huggingface model- in the open source spirit. 

## The UI
I've implimented an mvp here- it's a Vue app which presents lessons to the user. A lesson is: a topic choice, and a tutor interaction. When a lesson is over, a new one begins. The 'outer loop' is essentially a user-direct random walk through the knowledge graph, but the 'inner loop' is present in its entierty, sans grading at this stage. 


# Next Steps for polish-  
[] Css scroll snapping for individual text output - maybe unneccesary

[] "inactive" state for KC selection

[] Better colors overall?


# Next steps for functionality

[X] Inner-loop timeouts - if still incorrect or almost after so many tries, should be able to just give up

[X] Option to see the correct answer after some number of tries.

[] Grading feedback to the model

[] More sophisticated graph navigation, including changing learning objectives. 

[] More sophisticated graph structure

[] Mastery propogation...

[] Some kind of final output! 
