from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'ajax_polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class AjaxDetails(generic.TemplateView):
    template_name = 'ajax_polls/index.html'
    model = Question

    def get(self, request, *args, **kwargs):
        if request.GET['function'] == 'pull_choices':
            question_pk = request.GET['question_pk']
            data = {queryresponse.pk: {'choice_pk': queryresponse.pk,
                    'choice_text': queryresponse.choice_text}
                    for queryresponse in Choice.objects.filter(question_id=question_pk)}
            return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        choice_pk = request.POST['choice_pk']
        question_pk = request.POST['question_pk']
        count = ajax_vote(question_pk, choice_pk)
        data = {'hi': 'hello', 'bye': 'goodbye', 'count': count}
        return JsonResponse(data)


def ajax_vote(question_pk, choice_pk):
    question = get_object_or_404(Question, pk=question_pk)
    try:
        selected_choice = question.choice_set.get(pk=choice_pk)
    except (KeyError, Choice.DoesNotExist):
        return False
    selected_choice.votes += 1
    selected_choice.save()
    return selected_choice.votes
