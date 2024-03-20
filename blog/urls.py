from django.urls import path
from blog.views import homepage, blog, example_route, \
    blog_post, authors, blog_post_create, blog_post_update


app_name = "blog"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('blog/', blog, name="blog_list"),
                                                        
    path('blog/<int:id>/', blog_post, name="blog_post"),

    path('blog/create/', blog_post_create, name="blog_post_create"),

    path('blog/<int:id>/update/', blog_post_update, name="blog_post_update"),

    path('example-route/', example_route, name="example_route"),

    path('authors/', authors, name="authors"),
]
