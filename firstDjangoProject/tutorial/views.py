from django.http import HttpResponse
from django.shortcuts import render

"""
Vediamo meglio come è fatta la request e come possiamo utilizzarla.
print(“RESPONSE: ” + str(request)) 
RESPONSE: <WSGIRequest: GET '/home/'>
Tre info:
1. Questa richiesta è stata parsata tramite WSGI
2. è una get. Possiamo usare parametri.
3. Path specificato dall utente, visto che potrei arrivare da piu punti

print("Caratteristiche di request " + str(dir(request)))
Caratteristiche di request ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', 
'_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 
'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 
'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 
'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']

request è un oggetto di tipo HttpRequest. Tutti questi campi sono accedibili.
contiene tutte le informazioni relative alla richiesta HTTP fatta dal client al server.
alcuni di questi attributi...

Metodo HTTP: Puoi accedere al metodo HTTP utilizzato nella richiesta tramite request.method. Ad esempio, GET, POST, PUT, ecc.
Parametri GET/POST: Puoi accedere ai parametri passati nella richiesta GET o POST. Per esempio, request.GET per i parametri GET e request.POST per i parametri POST.
Sessioni: Puoi accedere alle sessioni dell'utente attraverso request.session. Questo è utile per memorizzare dati specifici dell'utente tra le richieste.
Utente autenticato: Se l'utente è autenticato, puoi accedere alle informazioni sull'utente attraverso request.user.
Metadati della richiesta: Puoi accedere ai metadati della richiesta come l'indirizzo IP del client attraverso request.META.
Cookie: Puoi accedere ai cookie inviati dal client attraverso request.COOKIES.
File caricati: Se il client ha inviato dei file, puoi accedere a essi attraverso request.FILES.
Altro: request contiene molte altre informazioni utili, come l'URL richiesto, l'host, il protocollo utilizzato, ecc.

In generale, l'oggetto request è essenziale per interagire con i dati inviati dal client e per prendere decisioni sulla risposta da restituire. 
Ogni vista in Django riceve un oggetto request e ritorna una risposta HTTP che può includere dati dinamici generati dal server.

Ovviamente per accedere al campo 'user' è necessario eseguire le migrazioni (python manage.py migrate).
Se l'user non è autenticato troveremo AnonymousUser

GET possiamo considerarlo come un dizionario. 
url_path?param1=value1&param2=value2...
request.GET[“param_name”]
"""


def homepage(request):
    ctx = {"title":"Tende Luxo"}
    return render(request, template_name="home.html", context=ctx)

def elenco_parametri(request):
    response=""
    for k in request.GET:
        response+=request.GET[k]+" "
    return HttpResponse(response)

def numpd(request):
    if not request.GET["num"].isdigit():
        return HttpResponse("Non hai inserito un numero")
    else:
        num = int(request.GET["num"])
        if num%2==0:
            return HttpResponse("Hai inserito un numero pari")
        else:
            return HttpResponse("Hai inserito un numero dispari")

def nomeparam(request):
    nome = request.GET["nome"]
    return HttpResponse("ciao, "+nome+"!")

def welcomenome(reuquest,nome):
    welcome_nome = nome
    nome_splittato = welcome_nome.split("_")[1]
    return HttpResponse("Ciao, "+nome_splittato+"!")
        


    
        