from django.shortcuts import render, redirect
from .models import *
from .forms import *
from build.gsheet.auth import queryResponse
from datetime import datetime

# Create your views here.
def done(request):
    return render(request, "build/done.html")

def bookTickets(request):   
    booked = Ticket.objects.all()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            real_form = form.save(commit=False)
            real_form.amt = (real_form.seats.count('A') + real_form.seats.count('B') + real_form.seats.count('C') + real_form.seats.count('D') + real_form.seats.count('E') + real_form.seats.count('F') + real_form.seats.count('G') + real_form.seats.count('H') + real_form.seats.count('I') + real_form.seats.count('J')) * 800

            real_form.amt += (real_form.seats.count('K') + real_form.seats.count('L') + real_form.seats.count('M') + real_form.seats.count('N') + real_form.seats.count('O')) * 500

            queryResponse(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), real_form.first_name, real_form.last_name, real_form.contact_no, real_form.email, real_form.age, real_form.quantity, real_form.seats, real_form.amt, real_form.tr_id, str(Ticket.objects.all().count()+2))
            form.save() 
            return redirect("done")
        else:
            return render(request, 'build/book.html', {'form':form, 'booked':booked})
    else:
        form = TicketForm()
        return render(request, 'build/book.html', {'form':form, 'booked':booked})
    