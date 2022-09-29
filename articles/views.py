from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from . models import Article


# Create your views here.
class ArticleListView(ListView):
	model = Article
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'detail.html'

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		likes_connected = get_object_or_404(Article, id=self.kwargs['pk'])
		liked = False
		if likes_connected.likes.filter(id=self.request.user.id).exists():
			liked = True
		data['number_of_likes'] = likes_connected.number_of_likes()
		data['post_is_liked'] = liked
		return data

def ArticleLike(request, pk):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

