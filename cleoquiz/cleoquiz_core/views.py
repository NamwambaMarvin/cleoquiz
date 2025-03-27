from django.shortcuts import render

# Index
def index(request):
    context = {}
    return render(request, "quiz_default/quiz.html", context)
