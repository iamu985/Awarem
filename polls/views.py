from django.shortcuts import render, get_object_or_404, redirect
from . models import Questions
from .forms import PollCreateQuestionForm
from main.forms import CreatePetitionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from voting.models import Vote

# Create your views here.

def polls_list_view(request):
    polls = Questions.objects.all()
    context = {
        'polls':polls,
    }
    return render(request, 'polls/index.html', context)

def polls_detail_view(request, question_id):
    poll = Questions.objects.get(pk=question_id)
    context = {
        'poll':poll,
    }
    return render(request, 'polls/details.html', context)

def polls_vote_view(request, question_id):
    if request.method == 'POST':
        print('POST METHOD VOTE')      
        question = get_object_or_404(Questions, pk=question_id)
        user = request.user
        if request.POST['choice'] == 'upvote':
            print('VOTE:UPVOTE')
            Vote.objects.record_vote(question, user, +1)
            result = Vote.objects.get_score(question)
            context = {'poll':question, 'result':result}
            return render(request, 'polls/result.html', context)
        if request.POST['choice'] == 'downvote':
            result = Vote.objects.record_vote(question, user, -1)
            result = Vote.objects.get_score(question)
            context = {'poll':question, 'result':result}
            return render(request, 'polls/result.html', context)
        else:
            context = {'poll':question}
            return redirect('polls:polls')
    return redirect('polls:polls')

def polls_petition_create_view(request):
    form = CreatePetitionForm()
    context = {'petition_form':form}
    return render(request, 'polls/petition-create.html', context)
