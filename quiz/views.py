# coding: utf-8 

from django.shortcuts import render

def index(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request):
	return render(request, "quiz/question.html")

def result(request):
	return render(request, "quiz/result.html")

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
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


