from django.db import models

class Category(models.Model):
	name = models.CharField('Название', max_length=50)
	url = models.SlugField('URL', max_length=200, unique=True, default="")
	objects = models.Manager()

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, verbose_name='Катерогия товаров', on_delete=models.SET_NULL, null=True)
	name = models.CharField('Название', max_length=200)
	price = models.FloatField('Цена')
	availability = models.BooleanField('В наличии', default=False,null=True, blank=True)
	image = models.ImageField('Фото (640x360)', null=True, blank=True)
	description = models.TextField('Описание', default='')
	contact = models.TextField('Контакты', default='')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name

	def is_availible(self):
		return self.availability

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
