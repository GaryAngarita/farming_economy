from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session or 'potatoes' not in request.session or 'wheat' not in request.session or 'corn' not in request.session:
        request.session['gold'] = 0
        request.session['potatoes'] = 0
        request.session['corn'] = 0
        request.session['wheat'] = 0
        request.session['activities'] = []
    context = {
        "activities": request.session['activities']
    }
    return render(request, "farm.html", context)

def process_crops(request):
    if request.method == "POST":
        myPotatoes = request.session['potatoes']
        myCorn = request.session['corn']
        myWheat = request.session['wheat']
        myGold = request.session['gold']
        crop = request.POST['crop']
        myTime = strftime("%B %d, %Y %H:%M %p", gmtime())
        activities = request.session['activities']
        if crop == "potatoes":
            potatoes = round(random.random() * 3) + 2
            myPotatoes += potatoes
            request.session['potatoes'] = myPotatoes
            str = f'{len(activities) + 1}. You have gathered {myPotatoes} potatoes. Keep it up!'
        elif crop == "corn":
            corn = round(random.random() * 2) + 4
            myCorn += corn
            request.session['corn'] = myCorn
            str = f'{len(activities) + 1}. You have gathered {myCorn} corn. Well done!'
        else:
            wheat = round(random.random() * 5) + 7
            myWheat += wheat
            request.session['wheat'] = myWheat
            str = f'{len(activities) + 1}. You have gathered {myWheat} wheat. Awesome job!'
        activities.insert(0, str)
        request.session['activities'] = activities
        
    return redirect('/')

def process_gold(request):
    if request.method == "POST":
        myPotatoes = request.session['potatoes']
        myCorn = request.session['corn']
        myWheat = request.session['wheat']
        myGold = request.session['gold']
        profit = request.POST['sell']
        activities = request.session['activities']
        if request.session['potatoes'] == 0 or request.session['corn'] == 0 or request.session['wheat'] == 0:
                str = f'You have sold all of that crop'
        else:
            if profit == 'potatoes':
                myGold = myPotatoes * 10
                myPotatoes = 0
                request.session['potatoes'] = myPotatoes
                str = f'{len(activities) + 1}. You have sold all your {profit} and earned {myGold}. Wow!'
            elif profit == 'corn':
                myGold = myCorn * 7
                myCorn = 0
                request.session['corn'] = myCorn
                str = f'{len(activities) + 1}. You have sold all your {profit} and earned {myGold}. Wow!'
            else:
                myGold = myWheat * 5
                myWheat = 0
                request.session['wheat'] = myWheat
                str = f'{len(activities) + 1}. You have sold all your {profit} and earned {myGold}. Wow!'
            
        request.session['gold'] = myGold
        activities.insert(0, str)
        request.session['activities'] = activities
    return redirect('/')

def delete(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
