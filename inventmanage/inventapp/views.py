from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import inspect
import inventapp.models as models
from inventapp.sqlqueries import *

modelNames = list()
for name, obj in inspect.getmembers(models, inspect.isclass):
    modelNames.append(name.lower())

# Create your views here.

def index(request):
    return render(request, "index.html", {"modelNames":modelNames,})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('user_login'))

def register(request):

    registered = False
    username = "Customer"

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        username = request.POST.get("username")
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('user_login'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    cust_dict = {
        "registered" : registered,
        "user_form" : user_form,
        "profile_form" : profile_form,
        "username" : username,
    }
    return render(request, "authentication/registration.html", context = cust_dict)

def user_login(request):
    loginFailed = False
    if request.method == 'POST':
    # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check if the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                loginFailed = False
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            loginFailed = True
            return render(request, 'authentication/login.html', {'loginFailed' : loginFailed,})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'authentication/login.html', {'loginFailed' : loginFailed,})

def getDBObject(objectType,caller,objectId=None):
        modelClass1 = globals()[objectType.title()]
        modelClass = 'inventapp_{}'.format(objectType)
        if caller == 'modelObjects':
            return model_objects(modelClass, objectId)
        elif caller == 'showObjectDetails':
            return show_object_details(modelClass, objectId)
        elif caller == 'showObjectList':
            return show_objects_list(modelClass)
        elif caller == 'saveObject':
            return modelClass1.objects.last()

def getContextObject(objectType,objectId=None):
        print('INSDE')
        if objectType == 'item':
            print('finside')
            inventory = Inventory.objects.all().only("inv_id")
            print(inventory)
            values = list()
            for x in inventory:
                values.append(x.inv_id)


            objectSet0 = {
                    'values':  values,
                    'targetControlID': 'id_inv',
                    }

            additionalObjects = {
                    'Item0':objectSet0,
                    }

            return additionalObjects #additionalObjects

        elif objectType == 'customer':
            print('finside')
            user = UserProfile.objects.all().only("users_id")
            print(user)
            values = list()
            for x in user:
                values.append(x.users_id)

            objectSet0 = {
                    'values':  values,
                    'targetControlID': 'id_users',
                    }

            additionalObjects = {
                    'Customer0':objectSet0,
                    }

            return additionalObjects #additionalObjects

        elif objectType == 'orders':
            print('finside')
            user = UserProfile.objects.all().only("users_id")
            print(user)
            values1 = list()
            for x in user:
                values1.append(x.users_id)

            payment = Payment.objects.all().only("pay_id")
            print(payment)
            values2 = list()
            for x in payment:
                values2.append(x.pay_id)

            item = Item.objects.all().only("item_id")
            print(item)
            values3 = list()
            for x in item:
                values3.append(x.item_id)

            customer = Customer.objects.all().only("customer_id")
            print(customer)
            values4 = list()
            for x in customer:
                values4.append(x.customer_id)

            objectSet0 = {
                    'values':  values1,
                    'targetControlID': 'id_users',
                    }
            objectSet1 = {
                    'values':  values2,
                    'targetControlID': 'id_pay',
                    }
            objectSet2 = {
                    'values':  values3,
                    'targetControlID': 'id_item',
                    }
            objectSet3 = {
                    'values':  values4,
                    'targetControlID': 'id_customer',
                    }

            additionalObjects = {
                    'Customer0':objectSet0,
                    'Customer1':objectSet1,
                    'Customer2':objectSet2,
                    'Customer3':objectSet3,
                    }

            return additionalObjects #additionalObjects

        elif objectType == 'payment':
            print('finside')
            user = UserProfile.objects.all().only("users_id")
            print(user)
            values1 = list()
            for x in user:
                values1.append(x.users_id)

            customer = Customer.objects.all().only("customer_id")
            print(customer)
            values4 = list()
            for x in customer:
                values4.append(x.customer_id)

            objectSet0 = {
                    'values':  values1,
                    'targetControlID': 'id_users',
                    }

            objectSet3 = {
                    'values':  values4,
                    'targetControlID': 'id_customer',
                    }

            additionalObjects = {
                    'Customer0':objectSet0,
                    'Customer3':objectSet3,
                    }

            return additionalObjects #additionalObjects

def modelObjects(request, objectType):
    print(modelNames)
    if 'edit' in request.GET:
        objectId = request.GET['objectId']
        objToUpdate = list(getDBObject(objectType,'modelObjects',objectId)[0][0])
        objectColumnList = getDBObject(objectType,'showObjectList')[1]
        fieldNames = [x[0] for x in objectColumnList]
        objDict = dict(zip(fieldNames, objToUpdate))
        context = {"objectType": objectType,
                "objectToUpdate":objDict,
                "modelNames":modelNames,
                "otherObjects":getContextObject(objectType),
        }

        templateFile = objectType+'Form.html'
        return render(request,templateFile, context)
    else: # if request is to add a new object
        context = {"objectType": objectType,
        "modelNames": modelNames,
        "otherObjects":getContextObject(objectType),
        }

        templateFile = objectType+'Form.html'
        return render(request,templateFile, context)

def updateObject(request,objectType,objectId):
    if request.POST:
        modelClass = 'inventapp_{}'.format(objectType)
        id = 'id'+'='+str(objectId)
        values = [id]
        if request.GET['operation'] == 'update':
            for key in request.POST:
                if key != 'csrfmiddlewaretoken':
                    if isinstance(request.POST[key], str):
                        values.append(key+"="+"'{}'".format(request.POST[key]))
                    else:
                        values.append(key+"="+str(request.POST[key]))
            print(values)
            update_object(modelClass, values, objectId)
        elif request.GET['operation'] == 'delete':
            delete_object(modelClass, objectId)

        context = {
        "objectType":objectType,
        "objectID":objectId,
        "Operation":request.GET['operation'],
        "modelNames":modelNames,
        }
        return render(request,"saveConfirmation.html",context)

def saveObject(request,objectType):
    if request.POST:
        modelClass = 'inventapp_{}'.format(objectType)
        id = getDBObject(objectType,'saveObject').id + 1
        values = [id]
        for key in request.POST:
            if key != 'csrfmiddlewaretoken':
                values.append(request.POST[key])
        print(values)
        save_object(modelClass, values)

        context = {
        "objectType":objectType,
        "objectID":values[0],
        "Operation":'add',
        "modelNames":modelNames,
        }
        return render(request,"saveConfirmation.html",context)

def showObjectDetail(request,objectType,objectId):
    objDetails = list(getDBObject(objectType,'showObjectDetails',objectId)[0][0])
    objectColumnList = getDBObject(objectType,'showObjectList')[1]
    fieldNames = [x[0] for x in objectColumnList]
    objDict = dict(zip(fieldNames, objDetails))
    context = {
            "object": objDict,
            "objectType": objectType,
            "modelNames":modelNames,
    }

    return render(request, 'showObjectDetail.html', context)

def showObjectList(request,objectType):
    objectList = getDBObject(objectType,'showObjectList')[0]
    objectColumnList = getDBObject(objectType,'showObjectList')[1]
    if len(objectList) > 0:
        fieldNames = [x[0] for x in objectColumnList]
        noEntry = False
    else:
        fieldNames = []
        noEntry = True
    context = {
        "noEntry": noEntry,
        "objects": objectList,
        "objectType": objectType,
        "fieldNames": fieldNames,
        "modelNames":modelNames,
    }

    return render(request, 'showObjectList.html', context)
