from django.db import models

# Create your models here.
# model = table

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
            
    def __str__(self):
        return self.title + ' - ' + self.author.name



    

# .get
# .all
# .created
    
#     author = Author(
# ...     name="Jasmin",
# ...     email="jasmin@gmail.com",
# ...     joining=date
# ... )
# >>> 
# >>> author.save()
    

# filter
    


# ORM -> object relational mapping


# class Example:
#     def __init__(self) -> None:
#         self.name = "Hello"

# exe = Example()
# exe.name = "New Name"


# post_1.title = "New Title"
# post_1.save()
