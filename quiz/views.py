# coding: utf-8 

from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

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
	number = int(number)
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	question = questions[number - 1]
	if number > questions.count():
		return redirect("completed_page", quiz.slug)
	context = {
			"question_number": number,
			"question": question.question,
			"answer1": question.answer1,
			"answer2": question.answer2,
			"answer3": question.answer3,
			"quiz": quiz,
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


