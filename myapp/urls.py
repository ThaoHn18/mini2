from django.conf.urls import url
# from django.urls.resolvers import URLPattern
from . import views # file urls.py và views.py cùng 1 folder
urlpatterns = [
    url(r"^$", views.index , name="index"),   #^$ là bắt đầu và kết thúc luôn thì nó rỗngn :))
    url(r"^add-author$",views.add_author, name='add_author'),
    url(r"^add-book$",views.add_book, name='add_book'),
    url(r"^author/(?P<author_id>[0-9]+)$",views.view_detail_author, name="view_detail_author" ),
    url(r"^update-author/(?P<author_id>[0-9]+)$", views.update_author, name= "update_author"),
    url(r"^delete-author/(?P<author_id>[0-9]+)$", views.delete_author, name= "delete_author"),
    url(r"^home$", views.home, name="home")
]