from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField('введите название блога',max_length=100)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #атрибут для заготовки выпадающего списка
    TYPE_BLOG = (
        ('Политика', 'Политика'),
        ('Спорт', 'Спорт'),
        ('Путешевствие', 'Путешевствие')
    )
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default='Путешевствие')
    email_author = models.EmailField('введите email автора', default='@gmail.com', null=True)
    views = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'