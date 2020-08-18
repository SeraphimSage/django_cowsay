from django.shortcuts import render
from homepage.models import Cowsay_Model
from homepage.forms import Cowsay_Form
import subprocess


def index(request):
    cowsays = ""
    if request.method == "POST":
        form = Cowsay_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Help from Matt seeing that text needed to be text_input to match what was said in the forms.
            Cowsay_Model.objects.create(text=data.get("text_input"))
            text = data.get("text_input")
            cowsays = subprocess.check_output(["cowsay", text], text=True)
            print(cowsays)
    form = Cowsay_Form()
    return render(
        request,
        "index.html",
        {
            "title": "What does the Cows Say?",
            "form": form,
            "cowsays": cowsays
        }
    )


def history_view(request):
    cowsay_history = Cowsay_Model.objects.order_by("-id")[:10]
    return render(request, "history.html", {"title": "What's the last 10 things the cow has said?", "data": cowsay_history})
