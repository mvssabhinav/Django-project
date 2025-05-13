from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from .models import Event,Birthday,Marriage
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def eventform(request):
    if request.method=='POST':  
        customer_name=request.POST['customer_Name']
        address=request.POST['Address']
        email=request.POST['Email']
        phone_number=request.POST['Phone_no']
        event_name=request.POST['Event_name']
        venue=request.POST['Venue']
        hall=request.POST['hall']
        event_date=request.POST['date']
        expected_cost=request.POST['Expected_Cost']
        
        events= Event.objects.create(
            user=request.user,
            customer_name=customer_name,
            address=address,
            email=email,
            phone_number=phone_number,
            event_name=event_name,
            venue=venue,
            hall=hall,
            event_date=event_date,
            expected_cost=expected_cost
        )
        events.save()
        return redirect('eventform')
    return render(request,'eventform.html')

def birthday(request):
    if request.method=='POST':
        customer_name=request.POST['customer_name']
        email=request.POST['Email']
        phone_no=request.POST['phone_no']
        capacity=request.POST['capacity']
        No_of_chairs=request.POST['No_of_chairs']
        catering=request.POST['catering']
        theam_decorators=request.POST['Theam_decorator']
        game_host=request.POST['game_host']
        magician=request.POST['Magician']
        tatoo_artist=request.POST['Tatoo_Artist']

        birthday= Birthday.objects.create(
            user=request.user,
            customer_name=customer_name,
            email=email,
            phone_no=phone_no,
            capacity=capacity,
            No_of_chairs=No_of_chairs,
            catering=catering,
            theam_decorators=theam_decorators,
            game_host=game_host,
            magician=magician,
            tatoo_artist=tatoo_artist
        )
        birthday.save()
        return redirect('birthday')
    return render(request,'birthday.html')

def marriage(request):
    if request.method=='POST':
        customer_name=request.POST['customer_name']
        email=request.POST['Email']
        phone_no=request.POST['phone_no']
        photographer=request.POST['Photographer']
        capacity=request.POST['capacity']
        No_of_chairs=request.POST['No_of_chairs']
        catering=request.POST['catering']
        theam_decorators=request.POST['Theam_decorator']
        pre_wedding=request.POST['Pre_wedding']
        mehandi_artist=request.POST['Mehandi_Artist']
        bride_jewellery_rent=request.POST['Bride_jewalary']
        music_dance=request.POST['Music_Dance']
        invitation_gifts=request.POST['Invitation']

        marriage= Marriage.objects.create(
                user=request.user,
                customer_name=customer_name,
                email=email,
                phone_no=phone_no,
                photographer=photographer,
                capacity=capacity,
                No_of_chairs=No_of_chairs,
                catering=catering,
                theam_decorators=theam_decorators,
                pre_wedding=pre_wedding,
                mehandi_artist=mehandi_artist,
                bride_jewellery_rent=bride_jewellery_rent,
                music_dance=music_dance,
                invitation_gifts=invitation_gifts
        )
        marriage.save()
        return redirect('marriage')

    return render(request,'marriage.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'Login.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful.')
        return redirect('Login2')
    
    return render(request, 'Login.html')

def success(request):
    return render(request,'success.html')

# This is for to redirect to /retrieved page (just to redirect to another page after matching username and password) by matching the given username and password in the default database
def Login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username

            if user.is_staff:
                return redirect('staffRetrivedData')
            else:
                return redirect('welcomepage')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'Login2.html')

# This code is for what the data should be shown in /retrived page for that we will use ForeignKey 

def retrieved(request):
    user = request.user
    events = Event.objects.filter(user=user)
    marriage_functions = Marriage.objects.filter(user=user)
    birthday_functions = Birthday.objects.filter(user=user)

    context = {
        'info': events,
        'birthdayfunctions': birthday_functions,
        'marriagefunction': marriage_functions
    }

    return render(request, 'retrieved.html', context)


def staffRetrivedData(request):
    # Check if the logged-in user is a staff member
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to view this page.")

    data = Event.objects.all()
    birthday_functions = Birthday.objects.all()
    marriage_functions = Marriage.objects.all()

    context = {
        'info': data,
        'birthdayfunctions': birthday_functions,
        'marriagefunction': marriage_functions,
    }

    return render(request, 'staffRetrivedData.html', context)

def logout_view(request):
    logout(request)
    return redirect('Login2')

def welcomepage(request):
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')
    
    context = {
        'username': username
    }

    return render(request, 'welcompage.html', context)












# Delete Event for staff
@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if not request.user.is_staff and event.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this data.")
    
    if request.method == 'POST':
        event.delete()
        return redirect('staffRetrivedData' if request.user.is_staff else 'retrieved')
    
    return render(request, 'delete_confirmation.html', {'object': event})

# Delete Birthday for staff
@login_required
def delete_birthday(request, id):
    birthday = get_object_or_404(Birthday, id=id)
    if not request.user.is_staff and birthday.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this data.")
    
    if request.method == 'POST':
        birthday.delete()
        return redirect('staffRetrivedData' if request.user.is_staff else 'retrieved')
    
    return render(request, 'delete_confirmation.html', {'object': birthday})

# Delete Marriage for staff
@login_required
def delete_marriage(request, id):
    marriage = get_object_or_404(Marriage, id=id)
    if not request.user.is_staff and marriage.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this data.")
    
    if request.method == 'POST':
        marriage.delete()
        return redirect('staffRetrivedData' if request.user.is_staff else 'retrieved')
    
    return render(request, 'delete_confirmation.html', {'object': marriage})



def proceed_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Update the status message
    event.status_message = "Your event work has started"
    event.save()

    # Redirect the staff member back to the staffRetrievedData page
    return redirect('staffRetrivedData')





