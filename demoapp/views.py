from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import loginform, userloginform, donmngmtloginform, recipientloginform, branchloginform, \
    donationform, requestdonationform
from demoapp.models import recipient, branchmngmt, donation, requestdonation


# Create your views here.
def home(request):
    return render(request,'home.html')

def user_registration(request):

    form1 = loginform()
    form2 = userloginform()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = userloginform(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_user = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()

            return redirect('loginview')

    return render(request, 'user_registration.html', {'form1': form1, 'form2': form2})


def donmngmt_registration(request):
    form1 = loginform()
    form2 = donmngmtloginform()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = donmngmtloginform(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_donmngmt = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('loginview')

    return render(request, 'donator_registration.html', {'form1': form1, 'form2': form2})


def recipient_registration(request):
    form1 = loginform()
    form2 = recipientloginform()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = recipientloginform(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_recipient = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('loginview')

    return render(request, 'recipient_registration.html', {'form1': form1, 'form2': form2})


def branch_registration(request):
    form1 = loginform()
    form2 = branchloginform()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = branchloginform(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_branchmngmt = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('loginview')

    return render(request, 'branch_registration.html', {'form1': form1, 'form2': form2})



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_staff:
                login(request, user)
                return redirect('adminhome')

            elif user.is_user:
                login(request, user)
                return redirect('userhome')

            elif user.is_donmngmt:
                login(request, user)
                return redirect('donationhome')

            elif user.is_recipient and user.Recipient.status == 1:
                print(user)
                login(request, user)
                return redirect('recipienthome')

            elif user.is_branchmngmt and user.branch.status == 1:
                login(request, user)
                return redirect('branchhome')

            else:
                messages.info(request, 'You are not a verified user')

        else:
            messages.info(request, 'invalid Credentials')
    return render(request, 'login.html')


def register(request):
    return render(request,'register.html')

def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    return render(request,'userhome.html')

def donationhome(request):
    return render(request,'donationhome.html')

def recipienthome(request):
    return render(request,'recipienthome.html')

def branchhome(request):
    return render(request,'branchhome.html')


# Approval

def recipient_approval_list(request):
    data = recipient.objects.all()
    return render(request, 'view_recipient.html', {'data': data})



def approve_recipient (request,user_id):
    data = recipient.objects.get(user_id=user_id)
    data.status = 1
    data.save()
    messages.info(request, 'recipient is approved to log in')
    return redirect('recipient_approval_list')



def reject_recipient(request,user_id):
    data = recipient.objects.get(user_id=user_id)
    data.status = 2
    data.save()
    messages.info(request, 'recipient approval request  is rejected')
    return redirect('recipient_approval_list')



def branch_approval_list(request):
    data = branchmngmt.objects.all()
    return render(request, 'view_branch.html', {'data': data})



def approve_branch(request, user_id):
    data = branchmngmt.objects.get(user_id=user_id)
    data.status = 1
    data.save()
    messages.info(request, 'Branch is approved to log in')
    return redirect('branch_approval_list')



def reject_branch(request, user_id):
    data = branchmngmt.objects.get(user_id=user_id)
    data.status = 2
    data.save()
    messages.info(request, 'Branch approval request  is rejected')
    return redirect('branch_approval_list')


# Donation

def add_donation(request):
    form = donationform()
    u = request.user
    if request.method=='POST':
        form = donationform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewDonation')
    return render(request,'add_donation.html',{'form':form})


def viewDonation(request):
    u = request.user
    data = donation.objects.filter(user=u)
    return render(request, 'view_donation.html', {'data': data})


def AdmviewDonation(request):
    data = donation.objects.all()
    return render(request, 'viewadm_donation.html', {'data': data})


def approve_donation(request,id):
    teacher = donation.objects.get(id=id)
    teacher.status = True
    teacher.status = 1
    teacher.save()
    messages.info(request, 'accept student leave')
    return redirect('AdmviewDonation')

# Reject Teacher's leave
def reject_donation(request, id):
    teacher = donation.objects.get(id=id)
    if request.method == 'POST':
        teacher.status = 2
        teacher.save()
        messages.info(request,'rejected student leave')
    return redirect('AdmviewDonation')


def request_donation(request):
    form = requestdonationform()
    u = request.user
    if request.method=='POST':
        form = requestdonationform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_reqDonation')
    return render(request,'request_donation.html',{'form':form})


def view_reqDonation(request):
    u = request.user
    data = requestdonation.objects.filter(user=u)
    return render(request, 'viewreq_donation.html', {'data': data})


def AdmviewDonationRequest(request):
    data = requestdonation.objects.all()
    return render(request, 'viewadm_donationrequest.html', {'data': data})


def approve_donationrequest(request,id):
    teacher = requestdonation.objects.get(id=id)
    teacher.status = True
    teacher.status = 1
    teacher.save()
    messages.info(request, 'accept student leave')
    return redirect('AdmviewDonationRequest')


def reject_donationrequest(request, id):
    teacher = requestdonation.objects.get(id=id)
    if request.method == 'POST':
        teacher.status = 2
        teacher.save()
        messages.info(request,'rejected student leave')
    return redirect('AdmviewDonationRequest')
