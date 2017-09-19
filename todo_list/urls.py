from django.conf.urls import url
from . import views

# 使用python的r前缀，就不必考虑转义的问题
# 使用正则提取字串，使用（）表示的就是需要提取的分组（Group）
# ^表示行的开头，$表示行的结束
# （?P<name>...）分组，除了原有的编号外再指定一个额外的别名
# \d 数字[0-9]
# + 匹配前一个字符0次或1次
urlpatterns = [
    url(r'^$', views.todolist, name='todo'),
    url(r'^addtodo/$', views.addTodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', views.todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', views.todoback, name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', views.tododelete, name='delete'),
]

