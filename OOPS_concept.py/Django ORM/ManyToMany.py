# Many-to-Many Relationship

''' In a many-to-many relationship, multiple records in one table can be associated with multiple records in another table. '''

'''Let’s consider the relationship between teachers and subjects in a school database. One teacher can teach one or many subjects. And also one subject can be taught by one or many teachers. This creates a many-to-many relationship between teachers and subjects'''

'''
To define a many-to-many relationship in Django models, we need to use the keyword ManyToManyField.'''

from django.db import models


class Teacher(models.Model):
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  
  def __str__(self):
        return str(self.first_name)
    
    
class Subject(models.Model):
  teachers = models.ManyToManyField(Teacher)
  title = models.CharField(max_length=250)
  
  def __str__(self):
        return str(self.title)

'''
One thing to note is that we also could use ManyToManyField in the Teacher model also. In that case, we need to put the Subject class first. '''


from django.db import models


class Subject(models.Model):
  title = models.CharField(max_length=250)
  
  def __str__(self):
        return str(self.title)
    
    
class Teacher(models.Model):
  subjects = models.ManyToManyField(Subject)
  
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  
  def __str__(self):
        return str(self.first_name)


'''Another example of a many-to-many relationship can be the relationship between blog posts and tags in a blog website. A blog post can share many tags, and a tag can be shared between many blog posts.

Consider this article about Django. It may have multiple tags: Programming, web development, Django, Python, etc. Another different article that is also related to Python and Django may have similar tags. So that's a many-to-many relationship.'''


from django.db import models


class Post(models.Model):
  title = models.CharField(max_length=450)
  subtitle = models.CharField(max_length=750)
  body = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return str(self.title)
    
    
class Tag(models.Model):
  posts = models.ManyToManyField(Post)
  name = models.CharField(max_length=450)
  
  def __str__(self):
        return str(self.name)