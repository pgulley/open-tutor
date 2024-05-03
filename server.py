from flask import Flask, jsonify, render_template, send_file, request
from models import StudentModel, TutorModel

app = Flask(__name__, template_folder=".")

SM = StudentModel()
TM = TutorModel()


@app.route("/")
def main():
   return send_file("main.html")

@app.route("/style.css")
def style():
	return render_template("style.css")

@app.route("/get_recs")
def get_student_recs():
	recs =  [k.json() for k in SM.get_recs()]
	return recs

@app.route("/choose_kc", methods=["POST"])
def choose_kc():
	SM.set_kc(request.data.decode())
	TM.generate_question(SM.kc)
	SM.record_action("tutor", TM.question)
	return {"question":TM.question}


"""Unimplemented:

def evaluate_response(response):
	SM.record_action("student", response)
	TM.evaluate_response(response)
	#this whole biz ain't implimented in the model

"""


