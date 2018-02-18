from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'ajax_polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'ajax_polls/detail.html'
    queryset = Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'ajax_polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kwargs_json = serializers.serialize('json', Choice.objects.all())
        context['kwargs_json'] = kwargs_json
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ajax_polls/details.html', {
            'question': question,
            'error_message': 'No choice was selected',
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('ajax_polls:results', args=(question.id,)))


class AjaxDetails(generic.TemplateView):
    template_name = 'ajax_polls/index.html'
    model = Question

    def get(self, request, *args, **kwargs):
        print(request.GET)
        question_pk = request.GET['question_pk']
        question = get_object_or_404(Question, pk=question_pk)
        print(question)
        data = {queryresponse.pk: {'choice_pk': queryresponse.pk,
                'choice_text': queryresponse.choice_text}
                for queryresponse in Choice.objects.filter(question_id=question_pk)}
        print(data)
        return JsonResponse(data)
