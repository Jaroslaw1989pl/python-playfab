# build-in modules
from django.http import HttpResponse
from django.template import loader
import bcrypt
# 3rd party modules
from .model.validator import Validator
from .model.user import User


# Create your views here.
def home(request):
    template = loader.get_template("main-home.html")
    context = {
        "title": "Home page"
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("auth-login.html")
    context = {
        "title": "Sign in"
    }
    return HttpResponse(template.render(context, request))

def registration(request):
    template = loader.get_template("auth-registration.html")
    context = {
        "title": "Sign up"
    }

    if request.method == 'POST':
        
        isFormValid = True

        token = request.POST.dict()["csrfmiddlewaretoken"]
        userEmail = request.POST.dict()["userEmail"]
        userPass = request.POST.dict()["userPass"]
        userPassConf = request.POST.dict()["userPassConf"]

        # 1. email validation
        try:
            Validator.input(userEmail).rules(Validator.RULE_REQUIRED, Validator.RULE_EMAIL)
        except Exception as error:
            isFormValid = False
            context["userEmailError"] = error
        finally:
            context["userEmail"] = userEmail

        # 2. password validation
        try:
            Validator.input(userPass).rules(
                Validator.RULE_REQUIRED,
                [Validator.RULE_MIN_LENGTH, 8],
                [Validator.RULE_MAX_LENGTH, 32]
            )
            # Hashing the password
            hashedPass = bcrypt.hashpw(userPass.encode('utf-8'), bcrypt.gensalt())
        except Exception as error:
            isFormValid = False
            context["userPassError"] = error
        finally:
            context["userPass"] = userPass

        # 3. password confirmation
        try:
            Validator.input(userPassConf).rules(
                Validator.RULE_REQUIRED,
                [Validator.RULE_EQUAL, userPass]
            )
        except Exception as error:
            isFormValid = False
            context["userPassConfError"] = error
        finally:
            context["userPassConf"] = userPassConf

        # if isFormValid:
        #     user = User(userEmail, hashedPass)
        #     user.add()

    return HttpResponse(template.render(context, request))