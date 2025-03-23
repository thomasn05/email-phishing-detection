from django.shortcuts import render
from joblib import load

md = load("./ML_model/email_model.joblib")
# Create your views here.
def start(request):
    return render(request, 'index.html')

def dataGiven(request):
    e_body = request.POST['email']
    y_pred = md.predict([e_body])
    if y_pred[0] == 'Phishing Email':
        y_pred = "No signs of phishing within the body of the email. Make sure to review the sender & any links provided."
    else:
        y_pred = "Signs of phishing. Proceed with caution. If sender email checks out, continue as normal."
    return render(request, 'answer.html', {'Answer' : y_pred})