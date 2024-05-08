# open-tutor
Final Project for CS690, Intelligent Tutors. 

There is a working prototype now!

## The Induced Knowledge Graph
`construct_knowledge_graph.ipynb` documents the process of manually piecing together a 'knowledge graph' from the openstax intro to sociology textbook.
Basically, we find "key terms", then assembled every block of text that the key term appears in. each term dangles from the chapter that it's introduced in, and also has connections to all other terms that co-occur in the text we found it in. It's pretty slapdash- future work here might involve spending some time developing a smarter approach, but this will be enough to play with all the functionality

## The "Student Model"
We use the knowledge graph as a basis of a student model, adding on learning objectives to each term. The student model can generate reccomendations for a path through the kg that serves as a curriculum. Currently working with sort of a random-walk approach- but the chapter data and the learning objective data can help steer that. 

## The Tutor
We use the content in the knowledge graph to generate prompts to an LLM, driving the system to generate question/answer pairs corresponding to the term, the text content, and the learning objective. We throw the question to the user and evaluate their response with another prompt to the llm.
One 'inner loop' of the tutor execution sees at least one feedback cycle with the student. The 'outerloop' corresponds to how the KG is navigated. 
Still figuring out exactly how the student model updates to reflect inner loop performance- but that's an ok open space for a class demo. 

Right now I have pretty good performance using openai's gpt3-turbo model in "completion" mode. Ideally, I think, this would be able to ship with a local huggingface model- in the open source spirit. 

## The UI
The plan will be to impliment the UI as a strictly "add-to" document. 
So far I've implimented the first kc selection prompt, and am successfully interfacing with openai and getting that content into the browser.
Next step is just taking the user response and passing that back to the api.

I'll spend some time sprucing things up- spinners and timings and all of that come next. 
The Learning Objectives have largely not been implemented- might have to have a component for the badges. 



# Next Steps for polish- 

[X] Spinners, or maybe just throbbing elipsis for when awaiting the tutor response
[X] Css scroll snapping for lesson headers
[X] "inactive" states for student responses 
[X] Better Buttons
[X] "Enter" interaction instead of just submit
[X] feedback status colors and other interactions
### these remaining things are not really neccesary but if the chance comes around
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
