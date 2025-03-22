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
    return render(request, 'index.html', {'answer' : y_pred})