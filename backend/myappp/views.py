from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from graphene_file_upload.decorators import file_upload

@file_upload
def graphql_view(request):
    if request.method == 'POST':
        data = request.POST
    else:
        data = request.GET

    return render(request, 'graphql.html', {'data': data})