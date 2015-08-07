# coding: utf-8 

from django.shortcuts import render
from quiz.models import Quiz

def index(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
		
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
		"question": u"Hur många bultar har Ölandsbron?",
		"answer1": u"12",
		"answer2": u"66 400",
		"answer3": u"7 428 954",
		"quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def result(request, slug):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_slug": slug, 
	}
	return render(request, "quiz/result.html", context)

# quizzes = {
# 	"klassiker": {
#    		"name": u"Klassiska böcker",
# 	   	"description": "Hur bra kan du dina klassiker?"
# 	},
# 	"fotboll": {
# 	   	"name": "Största fotbollslagen",
# 	   	"description": "Kan du dina lag?"
# 	},
# 	"kanda-hackare": {
# 	    	"name": "Världens mest kända hackare",
# 	    	"description": "Hackerhistoria är viktigt, kan du den?"	},
# }


