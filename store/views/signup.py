from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')


    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            context = {
                'error': error_message,
                'values': values
            }
            return render(request, 'signup.html', context)

    def validateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "First name required!!"
        elif len(customer.first_name) < 1:
            error_message = "First name must have atleast 2 character"
        elif not customer.last_name:
            error_message = "Last name required!!"
        elif len(customer.last_name) < 1:
            error_message = "Last name must have atleast 2 character"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 charater long"
        elif len(customer.password) < 6:
            error_message = "Password must be 6 charater long"
        elif len(customer.email) < 5:
            error_message = "Email must have atleat 5 charater"
        elif customer.isExist():
            error_message = "Email already registered"

        return error_message