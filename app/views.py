from django.shortcuts import render, redirect
from django.views import View
from .models import Product, CustomerDetails, Town, CustomerAddress, Cart, WishList
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerDetailsForm, CustomerAddressForm
from django.contrib import messages
import json
from django.http import JsonResponse
from django.db.models import Q  # Selecting multiple conditions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def get_total_cart_items(request):
    if request.user.is_authenticated:
        total = len(Cart.objects.filter(user=request.user))
        return total
    else:
        return 0


def get_total_wishlist_items(request):
    if request.user.is_authenticated:
        total = len(WishList.objects.filter(user=request.user))
        return total
    else:
        return 0


def home(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    products = Product.objects.filter(flash_sale=True)
    return render(request, 'app/home.html', locals())


def about(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    return render(request, 'app/about.html', locals())


def contact(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    return render(request, 'app/contact.html', locals())


class CategoryView(View):
    def get(self, request, value):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        product = Product.objects.filter(category=value)
        title = Product.objects.filter(category=value).values('title')
        return render(request, 'app/category.html', locals())


class CategoryTitle(View):
    def get(self, request, value):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        product = Product.objects.filter(title=value)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        product = Product.objects.get(pk=pk)
        wishlist = WishList.objects.filter(Q(product=product) & Q(user=request.user))
        return render(request, 'app/product-detail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/registration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!!')
        else:
            messages.warning(request, 'Invalid Input Data!')
        return render(request, 'app/registration.html', locals())


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        if request.user.is_authenticated:
            form = CustomerDetailsForm()
        else:
            messages.warning(request, 'Login or Sign up to update Profile')
        return render(request, 'app/update-profile.html', locals())

    def post(self, request):
        if request.user.is_authenticated:
            form = CustomerDetailsForm(data=request.POST, instance=request.user)
            if form.is_valid():
                user = request.user
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                gender = form.cleaned_data['gender']
                next_of_kin = form.cleaned_data['next_of_kin']
                next_of_kin_contact = form.cleaned_data['next_of_kin_contact']
                date_of_birth = form.cleaned_data['date_of_birth']
                contact = form.cleaned_data['contact']
                sub_county = form.cleaned_data['sub_county']
                school = form.cleaned_data['school']
                games_of_interest = form.cleaned_data['games_of_interest']
                height_in_cm = form.cleaned_data['height_in_cm']
                weight_in_kgs = form.cleaned_data['weight_in_kgs']
                special_needs = form.cleaned_data['special_needs']

                customer = CustomerDetails(id=request.user.id, user=user, first_name=first_name,
                                           last_name=last_name, gender=gender, next_of_kin=next_of_kin,
                                           next_of_kin_contact=next_of_kin_contact,
                                           date_of_birth=date_of_birth, contact=contact,
                                           sub_county=sub_county, school=school,
                                           games_of_interest=games_of_interest, height_in_cm=height_in_cm,
                                           weight_in_kgs=weight_in_kgs, special_needs=special_needs)

                customer.save()
                messages.success(request, 'Details Updated Successfully')
            else:
                messages.warning(request, 'Invalid Input data')
        else:
            messages.warning(request, 'Please Login or Signup to update profile details')

        return render(request, 'app/update-profile.html', locals())


@login_required
def profile(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    if request.user.is_authenticated:
        to_display = CustomerDetails.objects.filter(user=request.user)
        # return render(request, 'app/profile.html', locals())
    else:
        messages.warning(request, 'Login or Sign up to view Profile')
    return render(request, 'app/profile.html', locals())


class AddressView(View):
    def get(self, request):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        if request.user.is_authenticated:
            form = CustomerAddressForm()
        else:
            messages.warning(request, 'Login or Sign up to Create Address')
        return render(request, 'app/address-update.html', locals())

    def post(self, request):
        if request.user.is_authenticated:
            form = CustomerAddressForm(data=request.POST, instance=request.user)
            if form.is_valid():
                user = request.user
                county = form.cleaned_data['county']
                town = form.cleaned_data['town']
                pick_up_station = form.cleaned_data['pick_up_station']
                zip_code = form.cleaned_data['zip_code']
                contact = form.cleaned_data['contact']

                address = CustomerAddress(user=user, county=county, town=town,
                                          pick_up_station=pick_up_station, zip_code=zip_code,
                                          contact=contact)

                address.save()
                messages.success(request, 'Address Created Successfully')
            else:
                messages.warning(request, 'Invalid Input data')
        else:
            messages.warning(request, 'Please Login or Signup to update Address Details')

        return render(request, 'app/address-update.html', locals())


class AddressUpdateView(View):
    def get(self, request, pk):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        if request.user.is_authenticated:
            form = CustomerAddressForm()
        else:
            messages.warning(request, 'Login or Sign up to update Address')
        return render(request, 'app/address-update.html', locals())

    def post(self, request, pk):
        if request.user.is_authenticated:
            form = CustomerAddressForm(data=request.POST, instance=request.user)
            if form.is_valid():
                user = request.user
                county = form.cleaned_data['county']
                town = form.cleaned_data['town']
                pick_up_station = form.cleaned_data['pick_up_station']
                zip_code = form.cleaned_data['zip_code']
                contact = form.cleaned_data['contact']

                address = CustomerAddress(id=pk, user=user, county=county, town=town,
                                          pick_up_station=pick_up_station, zip_code=zip_code,
                                          contact=contact)

                address.save()
                messages.success(request, 'Address Updated Successfully')
            else:
                messages.warning(request, 'Invalid Input data')
        else:
            messages.warning(request, 'Please Login or Signup to update Address Details')

        return render(request, 'app/address-update.html', locals())


def address(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    if request.user.is_authenticated:
        to_display = CustomerAddress.objects.filter(user=request.user)
    else:
        messages.warning(request, 'Login or Sign up to view Address')
    return render(request, 'app/address.html', locals())


def get_towns(request):
    data = json.loads(request.body)
    county_id = data["id"]
    print(county_id)
    towns = Town.objects.filter(county__id=county_id)
    return JsonResponse(list(towns.values("id", "town")), safe=False)


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/show-cart')


def check_for_discount(amount):
    if amount > 10000:
        return 0.95 * amount
    else:
        return amount


def show_cart(request):
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        price = p.quantity * p.product.current_price
        amount += price
    total_amount = check_for_discount(amount=amount)
    return render(request, 'app/show-cart.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # selecting a particular cart item of current user
        current_cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        current_cart_item.quantity += 1
        current_cart_item.save()

        # we need to show updated details: price and quantity change
        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for p in cart:
            price = p.quantity * p.product.current_price
            amount += price
        total_amount = check_for_discount(amount=amount)

        data = {
            'quantity': current_cart_item.quantity,
            'amount': amount,
            'totalamount': total_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # selecting a particular cart item of current user
        current_cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        current_cart_item.quantity -= 1
        current_cart_item.save()

        # we need to show updated details: price and quantity change
        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for p in cart:
            price = p.quantity * p.product.current_price
            amount += price
        total_amount = check_for_discount(amount=amount)

        data = {
            'quantity': current_cart_item.quantity,
            'amount': amount,
            'totalamount': total_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # selecting a particular cart item of current user
        current_cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        current_cart_item.delete()

        # we need to show updated details: price and quantity change
        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for p in cart:
            price = p.quantity * p.product.current_price
            amount += price
        total_amount = check_for_discount(amount=amount)

        data = {
            'amount': amount,
            'totalamount': total_amount
        }
        return JsonResponse(data)


class CheckOutView(View):
    def get(self, request):
        total_cart_items = get_total_cart_items(request)
        total_wishlist_items = get_total_wishlist_items(request)
        user = request.user
        address = CustomerAddress.objects.filter(user=user)
        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for p in cart:
            price = p.quantity * p.product.current_price
            amount += price
        total_amount = check_for_discount(amount=amount)
        return render(request, 'app/checkout.html', locals())


def selected_address(request):
    if request.method == 'GET':
        address_id = request.GET['address_id']
        current_address = CustomerAddress.objects.get(id=address_id)
        shipping_cost = current_address.town.shipping_cost

        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for p in cart:
            price = p.quantity * p.product.current_price
            amount += price
        total_amount = check_for_discount(amount=amount) + shipping_cost

        data = {
            'shipping_cost': shipping_cost,
            'total_amount': total_amount
        }
        return JsonResponse(data)


def plus_wishlist(request):
    if request.method == 'GET':
        product_id = request.GET['prod_id']
        product = Product.objects.get(id=product_id)
        user = request.user
        WishList(user=user, product=product).save()
        data = {'message': 'Wishlist Added Successfully'}
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == 'GET':
        product_id = request.GET['prod_id']
        product = Product.objects.get(id=product_id)
        user = request.user
        WishList.objects.filter(user=user, product=product).delete()
        data = {'message': 'Wishlist Added Successfully'}
        return JsonResponse(data)


def search(request):
    query = request.GET['search']
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    products = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'app/search.html', locals())


def shop(request):
    products = Product.objects.all()
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    return render(request, 'app/shop.html', locals())


def wishlist_display(request):
    wishlist = WishList.objects.filter(user=request.user)
    total_cart_items = get_total_cart_items(request)
    total_wishlist_items = get_total_wishlist_items(request)
    return render(request, 'app/wishlist.html', locals())


def remove_wishlist(request):
    if request.method == 'GET':
        wishlist_id = request.GET['wishlist_id']
        WishList.objects.filter(id=wishlist_id).delete()
        data = {}
        return JsonResponse(data)

