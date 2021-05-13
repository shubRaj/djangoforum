from django.shortcuts import render
def page_not_found(request,exception):
    return render(request,'handler/404.html',status=404)
def server_error(request):
    return render(request,'handler/500.html',status=500)