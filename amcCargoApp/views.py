from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LahoreWeeklyClosing, LahoreAccount

from django.apps import apps


@login_required(login_url='/admin/')
def account_closing_details(request):
    if request.method == "POST":
        city = request.POST.get('city')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')

        mdl = city+'Account'
        Model = apps.get_model('amcCargoApp', mdl)
        all_details = Model.objects.filter(Date__range=[start_date, end_date])

        total_amount_to_pay = 0
        total_truck_rent = 0
        for to_pay_total in all_details:
            total_amount_to_pay+=to_pay_total.To_Pay

        for truck_rent_total in all_details:
            total_truck_rent+=truck_rent_total.Truck_Rent

        mdl_closing = city+'WeeklyClosing'
        Model_Closing = apps.get_model('amcCargoApp', mdl_closing)
        previous_balance = Model_Closing.objects.filter().latest('id').Previous_Balance

        total_balance = total_truck_rent+previous_balance+total_amount_to_pay



        context = {
        'all_details': all_details,
        'start_date':start_date,
        'end_date': end_date,
        'city': city,
        'total_amount_to_pay':total_amount_to_pay,
        'previous_balance':previous_balance,
        'total_balance':total_balance,
        'total_truck_rent':total_truck_rent,
        }

        return render(request, 'summary.html', context)
    return render(request, 'single.html')


def summary_details(request):
    if request.method == "POST":
        total_balance = request.POST.get('total-balance')
        recovery = request.POST.get('recovery')
        city = request.POST.get('city')
        
        context = {
            'total_balance':total_balance,
            'recovery':recovery
        }

        return render(request, 'summary-final.html', context)

