
from django import views
from quizapp.form import QuestionCreateForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import QuestionModel, ScoreModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def UserExits(username):
    if ScoreModel.objects.filter(name=username).exists():
        return True
    return False

def markscount(marks):
    marks += 10
    return marks



class KbcHome(TemplateView):
    template_name = "quizapp/homepage.html"


class FeaturesView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "quizapp/features.html"



class QuestionShow(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self,request,id):
        try:
            questions = QuestionModel.objects.all().get(id=id)
            if id != 1:
                score = ScoreModel.objects.get(name=request.user.username)
                return render(request, "quizapp/questionshow.html",{
                    "option":questions,
                    "score" :score.marks
                })
            else:
                return render(request, "quizapp/questionshow.html",{
                    "option":questions,
                    "score" : 0
                })
        except Exception as e:
            score = ScoreModel.objects.get(name=request.user.username)
            return render(request,"quizapp/scorecard.html",{
                "score" :score.marks
            })
    
    def post(self,request,id):
        data = request.POST
        ans = data.get('answer')
        UserCheck = UserExits(request.user.username)
        if UserCheck:
            score = ScoreModel.objects.all().get(name=request.user.username)
        else:
            mydata = ScoreModel(name=request.user.username, marks=0)
            mydata.save()
            score = ScoreModel.objects.all().get(name=request.user.username)
        if ans == QuestionModel.objects.all().get(id=id).answer:
            if request.user.username == score.name:
                if id == 1:
                    re_set_score = ScoreModel.objects.get(name=request.user.username)
                    re_set_score.marks = str(0)
                    re_set_score.lifeline = str(0)
                    re_set_score.save()
            newscore = ScoreModel.objects.get(name=request.user.username)
            marks = str(markscount(int(newscore.marks)))
            newscore.marks = marks
            newscore.save()
            id = id + 1
            url = reverse("question_show", kwargs={'id':id})
            return HttpResponseRedirect(url)
        else:
            if request.user.username != score.name:
                mydata = ScoreModel(name=request.user.username, marks=0)
                mydata.save()
            if id == 1:
                re_set_score = ScoreModel.objects.get(name=request.user.username)
                re_set_score.marks = str(0)
                re_set_score.lifeline = str(-1)
                re_set_score.save()
            if int(ScoreModel.objects.get(name=request.user.username).lifeline) > 1:
                return render(request,"quizapp/thanks.html")
            life = int(ScoreModel.objects.get(name=request.user.username).lifeline) + 1
            life_line = ScoreModel.objects.get(name=request.user.username)
            life_line.lifeline = str(life)
            life_line.save()
            url = reverse("question_show", kwargs={'id':id})
            return HttpResponseRedirect(url)


class AllScoreView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self,request):
        allscore = ScoreModel.objects.all().order_by('-marks')
        return render(request,'quizapp/topranker.html',{
            "allscore":allscore
        })

class MyScore(LoginRequiredMixin ,View):
    login_url = "login"
    def get(self, request):
        data = ScoreModel.objects.get(name=request.user.username)
        return render(request,"quizapp/myscore.html",{
            'score': data
        })

class QuestionCreate(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        form = QuestionCreateForm()
        return render(request, "quizapp/questioncreate.html",{
            "forms":form
        })

    def post(self,request):
        question = QuestionCreateForm(request.POST)
        if question.is_valid():
            question.save()
            print("question is   ",question)
            return render(request,"quizapp/sucessquestion.html")
        form = QuestionCreateForm()
        return render(request, "quizapp/questioncreate.html",{
            "forms":form
        })