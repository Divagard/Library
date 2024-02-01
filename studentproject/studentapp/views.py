from django.shortcuts import render,redirect
from studentapp.models import stud_det,stud_fee
from studentapp.forms import stud_form,stud_fees

# Create your views here.
def home(request):
    sfm = stud_form()
    if request.method == 'POST':
        stform = stud_form(request.POST)
        if stform.is_valid():
            stform.save()
           # return redirect('stdapp/success.html')
    return render(request,'stdapp/index.html',{'sfms':sfm})

def home2(request):
    #stform = stud_form()
    

    return render(request,'stdapp/success.html')

def home3(request):
    sd = stud_det.objects.all()
    sf = stud_fee.objects.all()
    return render(request,'stdapp/view.html',{'std':sd,'sfd':sf})


def home4(request):
    stfee = stud_fees()
    if request.method == 'POST':
        stfee = stud_fees(request.POST)
        if stfee.is_valid():
            stfee.save()
          #  return redirect('stdapp/success.html')

    return render(request, 'stdapp/fees.html',{'stdfee':stfee})