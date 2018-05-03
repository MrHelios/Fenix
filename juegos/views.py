from django.http import HttpResponse, Http404

def juego1_view(request):
    raise Http404('No puedes acceder a esta pagina.')


def juego1_download(request):
    raise Http404('No puedes acceder a esta pagina.')
