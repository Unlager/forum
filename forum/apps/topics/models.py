from django.db import models

class Topic(models.Model):
	topic_title = models.CharField('Title', max_length = 200, default = '')
	topic_text = models.TextField('Text', default = '')

	def __str__(self):
		return self.topic_title

	class Meta:
		verbose_name = 'Topic'
		verbose_name_plural = 'Topics'

class Comment(models.Model):
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	author_name = models.CharField('Name', max_length = 50, default = '')
	comment_text = models.CharField('Text', max_length = 200, default = '')

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
