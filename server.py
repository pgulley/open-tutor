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


@app.route("/student_response", methods=["POST"])
def evaluate_response():
	response = request.data.decode()
	SM.record_action("student", response)
	grade = TM.evaluate_response(response)
	return grade

@app.route("/reference_answer")
def get_answer():
	return {"reference_answer": TM.reference_answer}

##Eventually a:
"""
def final_grade():
	SM.graded(request.data.decode())

"""