from django.shortcuts import render
from joblib import load

md = load("backmodel/ML_model/email_model.joblib")
# Create your views here.
def start(request):
    return render(request, 'index.html')

def dataGiven(request):
    e_body = request.GET['email_b']
    y_pred = md.predict([e_body])
    print(y_pred)
    if y_pred[0] == 1:
        y_pred = "No signs of phishing within the body of the email. Make sure to review the sender & any links provided."
    else:
        y_pred = "Signs of phishing. Proceed with caution. If sender email checks out, continue as normal."
    return render(request, 'answer.html', {'Answer' : y_pred})