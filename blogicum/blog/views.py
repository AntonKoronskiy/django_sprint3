from django.shortcuts import render

from django.http import HttpResponseNotFound


def index(request):
    template_name = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    flag = False
    current_position = -1
    for i in posts:
        current_position += 1
        if i['id'] == id:
            flag = True
            break
    if flag is not True:
        return HttpResponseNotFound("404")
    context = {'post': posts[current_position]}
    return render(request, template_name, context)
