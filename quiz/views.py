from django.shortcuts import render

def index(request):
	return render(request, "quiz/index.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def result(request):
	return render(request, "quiz/result.html")

