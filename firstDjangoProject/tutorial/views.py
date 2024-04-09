from django.http import HttpResponse

def homepage(request):
    response="Benvenuto sul sito! \n"
    response+="Nuove features in arrivo..."

    return HttpResponse(response)