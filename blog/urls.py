from django.urls import path
from blog.views import homepage, blog, example_route, blog_post, authors


app_name = "blog"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('blog/', blog, name="blog_list"),

    path('blog/<str:slug>/', blog_post, name="blog_post") ,

    path('example-route/', example_route, name="example_route"),

    path('authors/', authors, name="authors"),
]
