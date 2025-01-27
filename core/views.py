from django.shortcuts import render


def server_error(request):
    return render(request, 'core/500.html', status=500)


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)