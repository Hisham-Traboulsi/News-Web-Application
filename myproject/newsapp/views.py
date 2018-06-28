from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import UserAccount, Article, Comment, Rating
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.core import serializers
from datetime import datetime

# display the articles on the given template
def index(request):
    article_list = Article.objects.order_by('category')
    template = loader.get_template('newsapp/news.html')
    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))

# display the login page
def display_login(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return render(request, "newsapp/login.html")

# display the register page
def display_register(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return render(request, "newsapp/register.html")

# check if user is logged in before running the function below it
@login_required(login_url = '/newsapp/login/')
def display_account_info(request):
    # display the account information page
    return render(request, "newsapp/account_info.html")

# allow the user to logout
def logout_view(request):
    # logs out the current user that has a logged in session
    logout(request)
    return render(request, "newsapp/login.html")

# proccess the registration data that is retrieved from the register page
def register_account(request):
    # check if request.metho is post since we are posting data to the server
    if request.method == 'POST':

        # get the data needed for creating a new user
        first_name = request.POST["firstname"]
        last_name = request.POST["surname"]
        username = request.POST["email"]
        password = request.POST["password"]
        phone_number = request.POST.get("mobile")

        # check if the user exists if so the return not successful to indicate that they are registered
        if User.objects.filter(username = username).exists():
            output = "not successful"
            return JsonResponse(output, content_type = 'application/json', safe=False)

        # if they are not registered the creat a new user object with values retrieved assigned to the attributes of the model
        user_entry, created = User.objects.get_or_create(
            username = username,
            password = make_password(password),
            first_name = first_name,
            last_name = last_name,
            email = username,
        )
        # save the new user in to the db
        user_entry.save();

        # fetch the user we just created
        user = User.objects.get(username = username)
        # create a new user account for the user this is to sotre any extra data ie phone number
        user_account_entry, created = UserAccount.objects.get_or_create(
            user = user,
            phone_number = phone_number,
        )
        #  save the new user account as well
        user_account_entry.save();
        # return success back to clinet to indicate that registrationwas successful
        output = "success"
        return JsonResponse(output, content_type='application/json', safe=False)
    # if the method is not post just return unsuccessful
    return JsonResponse("unsuccessful", content_type='application/jsno', safe=False)

# this function is to allow users to log in to their account
def login_to_account(request):
    # check if the method sent in the http message is get
    if request.method == 'GET':
        # get data needed to authenticate user
        username = request.GET["email"]
        password = request.GET["password"]
        # prevent repeated refreshing to the page whe redirected
        next = request.GET.get('next')
        # we try to authnticate the user this will hold a bool value
        user = authenticate(request, username=username, password=password)

        # if the user exists and user is true
        if user is not None:
            # login the user
            login(request, user)

            # again to prevent multiple refreshes to the page
            if next:
                return redirect(next)
            # return a jason success reponse back to the user
            output = "success"
            return JsonResponse(output, content_type='application/json', safe=False)
        # return a json unsuccessful json response
        output = "Unsuccessful"
        return JsonResponse(output, content_type='application/json', safe=False)
    # return a jason unsuccessful reponse we method is not get
    output = "Unsuccessful"
    return JsonResponse(output, content_type='application/json', safe=False)

# check if the user use logged in
@login_required(login_url='/newsapp/login/')
def get_user_data(request, username):
    # this function retrieves the users data to diaply on the account_info page
    if request.method == 'GET':
        # get the data that belongs to the user
        user = User.objects.get(username = username)
        last_name = user.last_name

        user_account = UserAccount.objects.get(user = user)
        phone_number = user_account.phone_number
        # place the data in a list

        # return a json response with the data
        return JsonResponse(phone_number, content_type = 'application/json', safe = False)
    #return a json unsuccessful json response when method is not get
    return JsonResponse("unsuccessful", content_type = 'application/json', safe = False)

# check if the user is logged in
@login_required(login_url='/newsapp/login/')
def update_user_info(request, username):
    # update the users data based on the username given as a parameter
    if request.method == 'PUT':
        # since PUT isnt supported much we place the data in to a dictionary
        # access the data from dictionary
        data = QueryDict(request.body)
        firstname = data.get("firstname")
        surname = data.get("surname")
        number = data.get("phone_number")
        # check if the account exists or not
        account_exists = UserAccount.objects.filter(phone_number = number).exists()

        # if the follow is validupdate the users data with the data they sent and return successful back to user
        if len(number) == 11 or len(number) == 0 and account_exists == False:
            user = User.objects.get(username = username)
            user_account = UserAccount.objects.get(user = user)

            user.first_name = firstname
            user.last_name = surname

            user_account.phone_number = number

            user_account.save()
            user.save()
            return JsonResponse("success", content_type='application/json', safe =False)
        # if the length of the number passed is greater than 11 or less 11 or the account account_exists
        # return the phrase phone number to indicate if that the phone number exists
        if len(number) < 11 or len(number) > 11 or account_exists:
            return JsonResponse("phone_number", content_type='application/json', safe=False)
        # return if there is a problem
        return JsonResponse("Unsuccessful", content_type='application/json', safe=False)
    #return if the method is not put
    return JsonResponse("Unsuccessful", content_type='application/json', safe=False)

def data(request, article_id):
    # get the necessary data for the selected article and render it on the page
    selected_article = get_object_or_404(Article, pk=article_id)
    article_id = Article.objects.get(pk = article_id)
    comments = Comment.objects.filter(article = article_id)
    ratings = Rating.objects.filter(article = article_id, user_email = request.user)
    return render(request, 'newsapp/data.html', {'selected_article': selected_article, 'comments': comments, 'ratings': ratings})

# check if user is logged in, allows the user to add comments
@login_required(login_url='/newsapp/login/')
def add_comment(request):
    if request.method == 'POST':

        article_id = request.POST["article_id"]
        user_fullname = request.POST["user_full_name"]
        comment_data = request.POST["comment"]
        username = request.POST["username"]

        article_instance = Article.objects.get(pk = article_id)

        comment_entry, created = Comment.objects.get_or_create(
            article = article_instance,
            user_full_name = user_fullname,
            user_email = username,
            comment = comment_data,
            pub_date = datetime.now(),
        )

        comment_entry.save();

        data = list(("success", comment_entry.id))

        return JsonResponse(data, content_type="application/json", safe=False)
    return JsonResponse("unsuccessful", content_type="application/json", safe=False)

# check if the user is logged in, allows the logged in user to delete thier own comment
@login_required(login_url='/newsapp/login')
def delete_comment(request, comment_id):
    if request.method == 'DELETE':
        comment_instance = Comment.objects.get(id = comment_id)
        comment_instance.delete();

        return JsonResponse("delete successful", content_type='application/json', safe=False)

# checks if the user is logged in, allows the logged in to like or dislike an article
@login_required(login_url='/newsapp/login')
def rate(request):
    if request.method =='POST':
        article_id = request.POST["article_id"]
        user_email_address = request.POST["user_email"]
        rating = request.POST["rating"]

        rating_check = Rating.objects.filter(article = article_id, user_email = request.user).exists();

        if rating_check == False:
            article_instance = Article.objects.get(id = article_id)

            rating_instance, created = Rating.objects.get_or_create(
                article = article_instance,
                user_email = user_email_address,
                rating_type = rating,
            )

            rating_instance.save();
            data = list(("successful", rating_instance.rating_type))
            return JsonResponse("successful", content_type="application/json", safe=False)
        rating_temp = Rating.objects.get(article = article_id, user_email = request.user)
        if rating_check == True and rating_temp.rating_type == True and rating == "True":
            rating_temp.delete()
            return JsonResponse("deletedRating", content_type="application/json", safe=False)
        elif rating_check == True and rating_temp.rating_type == False and rating == "False":
            rating_temp.delete()
            return JsonResponse("deletedRating", content_type="application/json", safe=False)
        elif rating_check == True and rating_temp.rating_type == True and rating == "False":
            rating_temp.rating_type = rating
            rating_temp.save();
            return JsonResponse("switchRating", content_type="application/json", safe=False)
        elif rating_check == True and rating_temp.rating_type == False and rating == "True":
            rating_temp.rating_type = rating
            rating_temp.save();
            return JsonResponse("switchRating", content_type="application/json", safe=False)

        return JsonResponse("unsuccessful", content_type="application/json", safe=False)
    return JsonResponse("unsuccessful", content_type="application/json", safe=False)
