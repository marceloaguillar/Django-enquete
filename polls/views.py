from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question
# Create your views here.               


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5] #PEGA TODAS AS PERGUNTAS 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

                                            
def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "Selecione uma opção"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))