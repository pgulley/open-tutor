from knowledge_component import KC
import pickle
import random
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

from openai import OpenAI


class StudentModel():
	# > Student Model
	#	> Knowledge Graph - This will just be loaded from a pickled file on load. 
	# 	> Status ie: Current KC, Current Chapter
	#	> Interaction History?

	def __init__(self):
		#For now we always start with the fresh KG
		self.KG = pickle.load(open("sociology_kg.pickle", "rb"))
		self.chapter = "chapter 1"
		self.kc = random.choice(list(self.KG[self.chapter]))
		self.history = []

	def get_recs(self):
		#Lots of little things to improve once we have learning objectives making more sense. 

		#For now we'll just give a few options randomly selected
		kc_links = [i for i in self.KG[self.kc] if type(i) != str]

		chapter_links = [i for i in self.KG[self.chapter] if type(i) != str]

		if len(kc_links) > 2:
			kc_links = random.sample(kc_links, 2)
			chapter_links = random.sample(chapter_links, 3)
			kc_links.extend(chapter_links)
			recs = kc_links

		else:
			recs = random.sample(chapter_links, 5)

		self.recs = {k.id:k for k in recs}

		return recs


	def set_kc(self, kc_id):
		kc = self.recs[kc_id]
		self.kc = kc
		self.chapter = f"chapter {kc.chapter}"

	def record_action(self,agent, text):
		self.history.append({
			"i":len(self.history)+1,
			"agent":agent,
			"text":text
		})

	def graded(self, grade):
		##This method will update the currently active kc based on the recieved grade. 
		#If >.8, the current lo and any subsidiary ones will be incremented a good deal
		#etc...

		pass

class TutorModel():
	#This guy mostly just manages talking to openai

	def __init__(self):
		self.oai_client = OpenAI()
		self.kc = None
		self.question = ""
		self.reference_answer = ""

		self.jinja_env = Environment(
			loader=FileSystemLoader("prompt_templates"),
			autoescape=select_autoescape()
		)


	def target_lo(self, term):
		##Soo really this is going to be a method that determines the learning objective for a given term
		#but for now we'll just sub it in
		print(term)
		active_lo = [t for t in term.learning_objectives.values() if t.active == True]
		return active_lo[0].title

	def generate_question(self, term):
		#Render all the relevant templates,
		# then send the request out to openai,
		# then parse the response and save it to the tutor object.

		self.term = term

		self.objective = self.target_lo(term)
		objective_template = self.jinja_env.get_template(f"{self.objective}.j2")
		self.objective_description = objective_template.render()

		system_question_template = self.jinja_env.get_template("system_question.j2")
		system_prompt = system_question_template.render()

		user_question_template = self.jinja_env.get_template("user_question.j2")
		user_prompt = user_question_template.render(term=term,
											objective=self.objective, 
											objective_description=self.objective_description)

		response = self.oai_client.chat.completions.create(
		  model="gpt-3.5-turbo-0125",
		  response_format={ "type": "json_object" },
		  messages=[
			{"role": "system", "content": system_prompt},
			{"role": "user", "content": user_prompt}
		  ]
		).choices[0].message.content
		
		response = json.loads(response)

		self.question = response["question"]
		self.reference_answer = response["answer"]


	def evaluate_response(self, student_response):

		system_eval_template = self.jinja_env.get_template("system_eval.j2")
		system_prompt = system_eval_template.render(
			term=self.term,
			question=self.question,
			answer=self.reference_answer)

		response = self.oai_client.chat.completions.create(
		  model="gpt-3.5-turbo-0125",
		  response_format={ "type": "json_object" },
		  messages=[
			{"role": "system", "content": system_prompt},
			{"role": "user", "content": student_response}
		  ]
		).choices[0].message.content
		
		response = json.loads(response)

		return response


if __name__ == "__main__":
	##little demo loop for testing
	sm = StudentModel()
	tm = TutorModel()

	recs = sm.get_recs()
	print(recs)

	sm.set_kc(recs[0])
	
	tm.generate_question(sm.kc)
	print(tm.question)
	print(tm.reference_answer)
	demo_answer = "TESTTESTTESTTEST"
	grade = tm.evaluate_response(demo_answer)
	print(grade)
	demo_answer = "I don't want to answer this question"
	grade = tm.evaluate_response(demo_answer)
	print(grade)