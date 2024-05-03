# open-tutor
Final Project for CS690, Intelligent Tutors. 


## The Induced Knowledge Graph
`construct_knowledge_graph.ipynb` documents the process of manually piecing together a 'knowledge graph' from the openstax intro to sociology textbook.
Basically, we find "key terms", then assembled every block of text that the key term appears in. each term dangles from the chapter that it's introduced in, and also has connections to all other terms that co-occur in the text we found it in. It's pretty slapdash- future work here might involve spending some time developing a smarter approach, but this will be enough to play with all the functionality

## The "Student Model"
We use the knowledge graph as a basis of a student model, adding on learning objectives to each term. The student model can generate reccomendations for a path through the kg that serves as a curriculum. 

## The Tutor
We use the content in the knowledge graph to generate prompts to an LLM, driving the system to generate question/answer pairs corresponding to the term, the text content, and the learning objective. We throw the question to the user and evaluate their response with another prompt to the llm.
One 'inner loop' of the tutor execution sees at least one feedback cycle with the student. The 'outerloop' corresponds to how the KG is navigated. 
Still figuring out exactly how the student model updates to reflect inner loop performance- but that's an ok open space for a class demo. 

Right now I have pretty good performance using openai's gpt2-turbo model in "completion" mode. Ideally, I think, this would be able to ship with a local huggingface model- in the open source spirit. 

## The UI
The plan will be to impliment the UI as a strictly "add-to" document. 
So far I've implimented the first kc selection prompt, and am successfully interfacing with openai and getting that content into the browser.
Next step is just taking the user response and passing that back to the api.
I might need to actually draw out the state diagram somewhere- as the user experience is mostly managed at the ui level.

I'll spend some time sprucing things up- spinners and timings and all of that come next. 
The Learning Objectives have largely not been implemented- might have to have a component for the badges. 