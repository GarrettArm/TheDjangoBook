from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description_text = [
            """This is the "hello world" app of django tutorials: <a href="https://docs.djangoproject.com/en/2.0/intro/tutorial01/">Polls</a>.""",
            """It is a three-page-deep app that teaches the basics of the django framework:  setting up and interacting with sql, user authentication, styling, routing, etc.""",
        ]
        context["description"] = description_text
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        polls_index_url = reverse("polls:index")
        context["polls_index_url"] = polls_index_url
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context["question"].id)
        kwargs_json = serializers.serialize("json", Choice.objects.all())
        context["kwargs_json"] = kwargs_json
        polls_index_url = reverse("polls:index")
        context["polls_index_url"] = polls_index_url
        polls_detail_url = reverse("polls:detail", args=(context["question"].id,))
        context["polls_detail_url"] = polls_detail_url
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {"question": question, "error_message": "No choice was selected"},
        )
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
