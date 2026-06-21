from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .utils.pdf import export_pdf
from django.contrib.auth import authenticate, login




def success(request):
    return render(request, "home.html")


from .forms import SignupForm


def signup(request):


    if request.method=="POST":

        form=SignupForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "login"
            )

    else:

        form=SignupForm()

    return render(

        request,

        "signup.html",

        {

        "form":form

        }

    )


from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect

def user_login(request):


    print("LOGIN PAGE OPENED")

    message=""

    if request.method=="POST":

        print("FORM SUBMITTED")

        uname=request.POST.get(
            "username"
        )

        password=request.POST.get(
            "password"
        )

        print("USERNAME =", uname)

        user=authenticate(

            request,

            username=uname,

            password=password

        )

        print("USER =", user)

        if user is not None:

            login(
                request,
                user
            )

            print("LOGIN SUCCESS")

            return redirect(
                "/home/"
            )

        else:

            print("LOGIN FAILED")

            message="Incorrect Username or Password"

    return render(

        request,

        "login.html",

        {

        "message":message

        }

    )









from .models import Subject


def dashboard(request):

    data=Subject.objects.filter(
        user=request.user
    )

    return render(
        request,
        'dashboard.html',
        {'data':data}
    )

from .ai_helper import generate_plan


def timetable(request):

    subjects=Subject.objects.filter(
        user=request.user
    )

    names=[
        s.name
        for s in subjects
    ]

    result=generate_plan(
        names
    )

    return render(
        request,
        'timetable.html',
        {'result':result}
    )

from .forms import SubjectForm
from django.contrib.auth.decorators import login_required
   

@login_required
def add_subject(request):


    form=SubjectForm()

    if request.method=="POST":

        form=SubjectForm(
            request.POST
        )

        if form.is_valid():

            obj=form.save(
                commit=False
            )

            obj.user=request.user

            obj.save()

            return render(

                request,

                "success.html",

                {

                "message":
                "Subject added successfully 📘"

                }

            )

    subjects=Subject.objects.filter(

        user=request.user

    )

    return render(

        request,

        "add_subject.html",

        {

        "form":form,

        "subjects":subjects

        }

    )





import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(


    api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
    

    )

model = genai.GenerativeModel(

    
    "gemini-2.5-flash"
    

    )


def welcome(request):

    return render(
        request,
        'welcome.html'
    )

def home(request):

    return render(
        request,
        'home.html'
    )

def gotologinpage(request):

    return render(
        request,
        'login.html'
    )

def loginpage(request):

    return render(request,'login.html')




def user_logout(request):

    return render(
        request,
        'welcome.html'
    )



def export_timetable(request):


    subjects = Subject.objects.filter(
        user=request.user
    )

    names = [

        i.name

        for i in subjects

    ]

    result = generate_plan(
        names
    )

    return export_pdf(
        result
    )

def chatbot(request):


    answer=""

    if request.method=="POST":

        question=request.POST.get(
            "question"
        )

        try:

            prompt=f"""
    ```

    You are an AI Study Assistant.

    Student question:

    {question}

    Give:

    1. Advice
    2. Short explanation
    3. Motivation

    """

    
            response=model.generate_content(
                question
            )

            answer=response.text

        except Exception:

            answer=(
                "AI unavailable."
            )

    return render(

        request,

        "chatbot.html",

        {

        "answer":answer

        }

    )




