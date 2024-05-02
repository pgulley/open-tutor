from flask import Flask
from models import StudentModel, TutorModel

app = Flask(__name__)

SM = StudentModel
TM = TutorModel


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_recs")
def get_student_recs():
	return SM.get_recs()

@app.route("/kc")
def choose_kc(kc):
	SM.set_kc(kc)
	TM.generate_question(SM.kc)
	SM.record_action("tutor", TM.question)
	return {"question":TM.question}


"""Unimplemented:

def evaluate_response(response):
	SM.record_action("student", response)
	TM.evaluate_response(response)
	#this whole biz ain't implimented in the model

"""
