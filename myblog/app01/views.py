from django.shortcuts import redirect, render, HttpResponse
from app01.models import Tag,Article,ArticleAuthor,Comment

# Create your views here.
def index(request):
    # return HttpResponse("Hello World".encode('utf-8'))
    return render(request, "index.html")

def clock(request):
    return render(request, "clock.html")

def main(request):
    return render(request, "main.html")

def articles(request):
    return render(request, "articles.html")

def article_post(request):
    article_id = request.GET.get("article_id")
    if article_id is None or not article_id.isdigit():
        raise Http404("Invalid article ID")
    article_id = int(article_id)
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found")
    prev_article = Article.objects.filter(id__lt=article_id).order_by("-id").first()
    next_article = Article.objects.filter(id__gt=article_id).order_by("id").first()
    context = {
        "article": article,
        "prev_article": prev_article,
        "next_article": next_article,
    }
    return render(request, "article_post.html", context)

def archive(request):
    return render(request, "archive.html")

def about(request):
    return render(request, "about.html")

def login(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    return render(request, "login.html")

def test(request):
    return render(request, "test.html")

def redirection(request):
    return redirect("/login/")
    # return redirect("https://www.baidu.com")