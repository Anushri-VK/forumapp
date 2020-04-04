from django.shortcuts import render,redirect
from forumapp.models import Question,Answer,Upvote
from datetime import datetime

def dashboard(request):
	author=request.user
	all_questions=Question.objects.all().order_by("-timestamp")
	all_answers=Answer.objects.all().order_by("-timestamp")
	return render(request,"dashboard.html",{"all_questions":all_questions,"all_answers":all_answers})

def questions(request):
	if request.method=="POST":
		question=request.POST["question"]
		question_instance=Question.objects.create(
			author=request.user,
			question=question,
			timestamp=datetime.now()
			)
		question_instance.save()
		return redirect("/dashboard/")
	user=request.user
	all_questions=Question.objects.all().order_by("-timestamp")
	return render(request,"question.html",{"all_questions":all_questions})

def discussion(request,question_id):
	question=Question.objects.get(pk=question_id)
	if request.method=="POST":
		answer=request.POST["answer"]
		answer_instance=Answer.objects.create(
			author=request.user,
			answer=answer,
			question=question,
			timestamp=datetime.now(),
			upvote=1
			)
		answer_instance.save()
		return redirect(f"discussion/{question.id}")
	all_answers=Answer.objects.filter(question=question_id)
	
	return render(request,"discussion.html",{"all_answers":all_answers,"question":question})


def upvote(request,answer_id):
	answer=Answer.objects.get(pk=answer_id)
	upvotes=Upvote.objects.filter(reader=request.user,answer=answer)
	if len(upvotes)==0:
		answer.upvotes+=1
		answer.save()
		upvote=Upvote.objects.filter(reader=request.user,answer=answer)
		upvote.save()
	return redirect(f"/discussion/{answer.question.id}")

def signout(request):
	logout(request)

	return redirect("/signin")



