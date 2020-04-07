from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,HttpResponse,redirect
from .forms import applicationForm
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def index(request):
    form = applicationForm(request.POST or None)
    POSITIONS = {
        'Python Developer': "Python Developer",
        'Java Developer': 'Java Developer',
        'Web  Developer': 'Web Developer',
    }
    context = {
        'form':form,
        'Positions':POSITIONS
    }
    if request.method == 'POST':
        # print("PRINTING",request.POST)
        form = applicationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(request.POST.get('first_name'),request.POST.get('last_name'),
                      request.POST.get('position'),request.POST.get('github'),
                      request.POST.get('linkedin'),request.POST.get('email'),request.POST.get('about_me'))
            return redirect('/')
    return render(request,'my_form/index.html',context)

def send_mail(f_name,l_name,position,github,linkedin,mail,about):
        '''send email via mailgun'''
        name = f_name + " "+ l_name
        subject = position+" application from "+ name
        text_content = "Linkedin Link = "+ linkedin + "\n" + \
                       "Github Link = "+ github+ "\n"+ \
                       "Email = "+ mail + "\n"+\
                        about
        sender = "senderEmail"
        receipient = "receipientEmail"
        msg = EmailMultiAlternatives(subject, text_content, sender, [receipient])
        msg.send()

