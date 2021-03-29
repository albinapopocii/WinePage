from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.db.models import Q

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    article = Article.objects.all()
    event = Event.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'article': article, 'event':event}
    return render(request, 'store/homepage.html', context)


def basket_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/basket_page.html', context)


def blog_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    event = Event.objects.all()
    context = {'event': event, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/blog_page.html', context)


def event_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    article = Article.objects.all()
    context = {'article': article, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/event_page.html', context)


def one_article_page(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    article = Article.objects.get(id=id)
    products = Product.objects.all()
    context = {'article': article, 'products': products, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/one_article_page.html', context)


def one_product_page(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    product = Product.objects.get(id=id)
    article = Article.objects.all()
    products = Product.objects.all()
    context = {'article': article, 'product': product, 'products': products, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/one_product_page.html', context)


def one_event_page(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    events = Event.objects.get(id=id)
    product = Product.objects.all()
    context = {'events': events, 'product': product, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/one_event_page.html', context)


def product_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']
    product = Product.objects.all()
    article = Article.objects.all()
    context = {'product': product, 'article': article, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/product_page.html', context)


def category_product_page(request, type):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    product = Product.objects.filter(type=type)
    products = Product.objects.all()
    article = Article.objects.all()
    context = {'product': product, 'article': article, 'products': products, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/product_page.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('', safe=False)



def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.delivery:
            DeliveryOrder.objects.create(
                customer=customer,
                order=order,
                address=data['delivery']['address'],
                phoneNumber=data['delivery']['phoneNumber'],
                city=data['delivery']['city-'],
            )
    else:
        print('User not logged in')
    # print('data', request.body)
    return JsonResponse('', safe=False)


def contact_us(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/contact_us.html', context)


def about_us(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/about_us.html', context)


def terms_conditions(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/terms_conditions.html', context)


def privacy_policy(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/privacy_policy.html', context)
