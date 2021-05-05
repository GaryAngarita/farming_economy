from django.shortcuts import render, redirect
import random
from time import gmtime, strftime
import tkinter
from tkinter import messagebox

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
            str = f'{len(activities) + 1}. You have gathered {potatoes} potatoes. Keep it up! {myTime}'
        elif crop == "corn":
            corn = round(random.random() * 2) + 4
            myCorn += corn
            request.session['corn'] = myCorn
            str = f'{len(activities) + 1}. You have gathered {corn} corn. Well done! {myTime}'
        else:
            wheat = round(random.random() * 5) + 7
            myWheat += wheat
            request.session['wheat'] = myWheat
            str = f'{len(activities) + 1}. You have gathered {wheat} wheat. Awesome job! {myTime}'
        activities.insert(0, str)
        request.session['activities'] = activities
        if request.session['gold'] >= 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Congratulation!", f'You made {myGold} gold!')
            return redirect('/delete')
        elif len(request.session['activities']) == 25 and request.session['gold'] < 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Sorry!", f'You only earned {myGold} gold')
            return redirect('/delete')
    return redirect('/')

def process_gold(request):
    if request.method == "POST":
        myPotatoes = request.session['potatoes']
        myCorn = request.session['corn']
        myWheat = request.session['wheat']
        myGold = request.session['gold']
        profit = request.POST['sell']
        activities = request.session['activities']
        if profit == 'potatoes':
            cropGold = myPotatoes * 10
            myPotatoes = 0
            request.session['potatoes'] = myPotatoes
            str = f'{len(activities) + 1}. You have sold all your {profit} and earned {cropGold}. Wow!'
            #if request.session['potatoes'] <= 0 and profit == 'potatoes':
            #    str = f'{len(activities)}. You have sold all your potatoes'
        elif profit == 'corn':
            cropGold = myCorn * 7
            myCorn = 0
            request.session['corn'] = myCorn
            str = f'{len(activities) + 1}. You have sold all your {profit} and earned {cropGold}. Wow!'
            #if request.session['wheat'] <= 0 and profit == 'wheat':
            #    str = f'{len(activities)}. You have sold all your wheat'
        elif profit == 'wheat':
            cropGold = myWheat * 5
            myWheat = 0
            request.session['wheat'] = myWheat
            str = f'{len(activities) + 1}. You have sold all your {profit} and earned {cropGold}. Wow!'
            #if request.session['corn'] <= 0 and profit == 'corn':
            #    str = f'{len(activities)}. You have sold all your corn'     
        myGold += cropGold
        request.session['gold'] = myGold
        activities.insert(0, str)
        request.session['activities'] = activities

        if request.session['gold'] >= 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Congratulation!", f'You made {myGold} gold!')
            return redirect('/delete')
        elif len(request.session['activities']) == 25 and request.session['gold'] < 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Sorry!", f'You only earned {myGold} gold')
            return redirect('/delete')
    return redirect('/')

def gamble(request):
    if request.method == 'POST':
        wager = request.POST['wager']
        myGold = request.session['gold']
        activities = request.session['activities']
        if wager == 'slots' and request.session['gold'] > 0:
            myWager = random.randint(-50, 50)
            myGold += myWager
            if myWager > 0:
                str = f'{len(activities) + 1}. You have earned {myWager} gold!'
            else:
                str = f'{len(activities) + 1}. You have lost {abs(myWager)} gold!'
        else:
            str = f'{len(activities) + 1}. You do not have any gold to gamble'
        request.session['gold'] = myGold
        activities.insert(0, str)
        request.session['activities'] = activities

        if request.session['gold'] >= 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Congratulation!", f'You made {myGold} gold!')
            return redirect('/delete')
        elif len(request.session['activities']) == 25 and request.session['gold'] < 500:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Sorry!", f'You only earned {myGold} gold')
            return redirect('/delete')
    return redirect('/')

def delete(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
