from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Topic, Comment

def index(request):
	latest_topics_list = Topic.objects.order_by('id')[:5]
	return render(request, 'topics/list.html', {'latest_topics_list': latest_topics_list})

def detail(request, topic_id):
	try:
		topic = Topic.objects.get(id = topic_id)
	except:
		raise Http404("Статья не найдена!")
	latest_comments_list = topic.comment_set.order_by('-id')[:10]
	return render(request, 'topics/detail.html', {'topic': topic, 'latest_comments_list': latest_comments_list})



def leave_comment(request, topic_id):
	try:
		topic = Topic.objects.get(id=topic_id)
	except:
		raise Http404("Статья не найдена!")

	topic.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
	return HttpResponseRedirect( reverse('topics:detail', args = (topic.id,)))