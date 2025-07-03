from django.shortcuts import render

def produtos_list(request):
    return render(request, 'produtos/produtos_list.html')
    