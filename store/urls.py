from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='store/homepage'),
    path('basket_page/', views.basket_page, name='store/basket_page'),
    path('blog_page/', views.blog_page, name='store/blog_page'),
    path('event_page/', views.event_page, name='store/event_page'),
    path('one_article_page/<id>', views.one_article_page, name='store/one_article_page'),
    path('one_product_page/<id>', views.one_product_page, name='store/one_product_page'),
    path('one_event_page/<id>', views.one_event_page, name='store/one_event_page'),
    path('product_page/', views.product_page, name='store/product_page'),
    path('category_product_page/<type>', views.category_product_page, name='store/category_product_page'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('contact_us/', views.contact_us, name='store/contact_us'),
    path('privacy_policy/', views.privacy_policy, name='store/privacy_policy'),
    path('about_us/', views.about_us, name='store/about_us'),

]
