from django.shortcuts import render, redirect, get_object_or_404
from main.forms import productForm
from main.models import product
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect , JsonResponse
from django.urls import reverse

# pass pws : ekqM5XlR7RbiVjz9_s7JXrQtG_Golr-Q
@login_required(login_url='/login')
def show_main(request):
    product_list = product.objects.all()

    filter_type = request.GET.get("filter", "all")  
    if filter_type == "all":
        product_list = product.objects.all()
    else:
        product_list = product.objects.filter(user=request.user)
    
    context = {
        'npm' : '2406354303',
        'name': 'Ghiyas Fazle Mawla Rahmat',
        'class': 'PBP A',
        'project' : 'ChelseaShop',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = productForm(request.POST or None)

    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            # If AJAX request, return JSON with created product data
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({
                    'success': True,
                    'product': {
                        'id': str(product_entry.id),
                        'name': product_entry.name,
                        'description': product_entry.description,
                        'price': product_entry.price,
                        'stock': product_entry.stock,
                        'category': product_entry.category,
                        'thumbnail': product_entry.thumbnail,
                        'is_sale': product_entry.is_sale,
                    }
                })
            return redirect('main:show_main')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    item = get_object_or_404(product, pk=id)

    context = {
        'product': item
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get('filter', 'all')
    qs = product.objects.all()
    if filter_type == 'my' and request.user.is_authenticated:
        qs = qs.filter(user=request.user)

    data = []
    for p in qs:
        data.append({
            'id': str(p.id),
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'stock': p.stock,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'is_sale': p.is_sale,
            'user_id': p.user.id if p.user else None,
            'username': p.user.username if p.user else 'Anonymous',
        })

    return JsonResponse(data, safe=False)
def show_xml_by_id(request, product_id):
   try:
       product_item = product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
       p = product.objects.get(pk=product_id)
       data = {
           'id': str(p.id),
           'name': p.name,
           'description': p.description,
           'price': p.price,
           'stock': p.stock,
           'category': p.category,
           'thumbnail': p.thumbnail,
           'is_sale': p.is_sale,
           'user_id': p.user.id if p.user else None,
           'username': p.user.username if p.user else 'Anonymous',
       }
       return JsonResponse(data)
   except product.DoesNotExist:
       return JsonResponse({'error': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            # If request is AJAX/fetch, return JSON instead of redirect
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'success': True, 'redirect': reverse('main:login')})
            return redirect('main:login')
        else:
            # on AJAX return validation errors as JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
          user = form.get_user()
          login(request, user)
          # build response
          redirect_url = reverse("main:show_main")
          # If AJAX request, return JSON with redirect and set cookie on JsonResponse
          if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                resp = JsonResponse({'success': True, 'redirect': redirect_url})
                resp.set_cookie('last_login', str(datetime.datetime.now()))
                return resp

          response = HttpResponseRedirect(redirect_url)
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    item = get_object_or_404(product, pk=id)
    if request.method == 'POST':
        form = productForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diupdate!')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'success': True, 'product': {'id': str(item.id)}})
            return redirect('main:show_product', id=item.pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = productForm(instance=item)
    context = {'form': form, 'product': item}
    return render(request, 'edit_product.html', context)

def edit_product(request, id):
    item = get_object_or_404(product, pk=id)
    if request.method == 'POST':
        form = productForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diupdate!')
            return redirect('main:show_product', id=item.pk)
    else:
        form = productForm(instance=item)
    context = {'form': form, 'product': item}
    return render(request, 'edit_product.html', context)

def delete_product(request, id):
    item = get_object_or_404(product, pk=id)
    item.delete()
    # If request was made via AJAX/fetch, return JSON so client can update without redirect
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
        return JsonResponse({'success': True})
    return HttpResponseRedirect(reverse('main:show_main'))