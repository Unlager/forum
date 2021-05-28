from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Topic, Comment


def index(request):
    latest_topics_list = Topic.objects.order_by('-id')
    return render(request, 'topics/list.html', {'latest_topics_list': latest_topics_list})


def post(request):
    if request.user.is_authenticated:
        return render(request, 'topics/post.html')
    raise Http404("Статья не найдена!")


def create_post(request):
    if request.user.is_authenticated:
        try:
            topic = Topic(topic_title=request.POST['title'], topic_text=request.POST['text'],
                          author_id=request.user.id, topic_subject=request.POST['options'])
        except:
            topic = Topic(topic_title=request.POST['title'], topic_text=request.POST['text'],
                          author_id=request.user.id, topic_subject='ФЛУД')
        topic.save()
    return HttpResponseRedirect('/')


def detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        name = User.objects.get(id=topic.author_id)

    except:
        raise Http404("Статья не найдена!")
    latest_comments_list = topic.comment_set.order_by('id')
    return render(request, 'topics/detail.html',
                  {'topic': topic, 'latest_comments_list': latest_comments_list, 'name': name})


def leave_comment(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except:
        raise Http404("Статья не найдена!")
    if request.user.is_authenticated:
        topic.comment_set.create(author_name=request.user, comment_text=request.POST['text'], author_id=request.user.id)
    return HttpResponseRedirect(reverse('topics:detail', args=(topic.id,)))


def delete_post(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        if request.user.is_authenticated and request.user.id == topic.author_id or request.user.is_staff == 1:
            topic.delete()
            return HttpResponseRedirect('/')
        else:
            raise Http404("Статья не найдена!")
    except:
        raise Http404("Статья не найдена!")


def delete_comment(request, topic_id, c_id):
    if topic_id != False:
        try:
            topic = Topic.objects.get(id=topic_id)
            comment = Comment.objects.get(id=c_id)
            print(comment)
            if request.user.is_authenticated and request.user.id == comment.author_id or request.user.is_staff == 1:
                comment.delete()
                return HttpResponseRedirect(reverse('topics:detail', args=(topic.id,)))
            else:

                print("Обшибка 1")
                raise Http404("Статья не найдена!")

        except:
            raise Http404("Статья не найдена!")
            print("Обшибка 2")
    else:
        try:
            comment = Comment.objects.get(id=c_id)
            print(comment)
            if request.user.is_authenticated and request.user.id == comment.author_id or request.user.is_staff == 1:
                comment.delete()
                return HttpResponseRedirect(reverse('accounts:my_comments'))
            else:

                print("Обшибка 1")
                raise Http404("Статья не найдена!")

        except:
            raise Http404("Статья не найдена!")
            print("Обшибка 2")