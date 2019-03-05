from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'ajax_polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description = [
            """Remember the Polls app?  This page does the same task, but uses Ajax instead.""",
            """Ajax is a kind of javascript that allows a webpage to send requests and accept responses without refreshing the entire page.""",
            """When you request the page at the url you see in your browser's location bar, Django does a plain vanilla html response.  The response has a bit of javascript, which attaches an ajax function to a click event.  Clicking a Question or Choice above activates that ajax function.""",
            """Here is the interesting part of ajax:  Activating the ajax functions sends a request to a different url from the one in the browser location bar.  You wire up the ajax url to hit a separate function in the appserver, which processes the ajax request and returns the response as json directly back to the requesting ajax.""",
            """""",
        ]
        context['description'] = description
        return context


class AjaxDetails(generic.TemplateView):
    template_name = 'ajax_polls/index.html'
    model = Question

    def get(self, request, *args, **kwargs):
        if request.GET['function'] == 'pull_choices':
            question_pk = request.GET['question_pk']
            payload = {queryresponse.pk: {'choice_pk': queryresponse.pk,
                    'choice_text': queryresponse.choice_text}
                    for queryresponse in Choice.objects.filter(question_id=question_pk)}
            return JsonResponse(payload)

    def post(self, request, *args, **kwargs):
        choice_pk = request.POST['choice_pk']
        question_pk = request.POST['question_pk']
        count = ajax_vote(question_pk, choice_pk)
        payload = {'count': count, }
        return JsonResponse(payload)


def ajax_vote(question_pk, choice_pk):
    question = get_object_or_404(Question, pk=question_pk)
    try:
        selected_choice = question.choice_set.get(pk=choice_pk)
    except (KeyError, Choice.DoesNotExist):
        return False
    selected_choice.votes += 1
    selected_choice.save()
    return selected_choice.votes
