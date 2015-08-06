from django.shortcuts import render

def index(request):
	return render(request, "quiz/index.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def result(request):
	return render(request, "quiz/result.html")

quizzes = {
	"klassiker": {
   		"name": "Klassiska böcker",
	   	"description": "Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": "Största fotbollslagen",
	   	"description": "Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": "Världens mest kända hackare",
	    	"description": "Hackerhistoria är viktigt, kan du den?"	},
}


