from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """创建Todo-List的数据库模型"""
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    flag = models.CharField(max_length=2)  # 已经完成的事项flag为0，待办事项flag为1
    priority = models.CharField(max_length=2)
    pubtime = models.DateTimeField(auto_now_add=True)  # todo实例的发布时间，默认为当前时间

    def __str__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    # 首先通过priority属性排序，然后通过pubtime属性排序
    class Meta:
        ordering = ['priority', 'pubtime']

