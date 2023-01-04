from django.shortcuts import render


def view_bag(request):
    ''' View that renders bag content page '''
    
    return render(request, 'bag/bag.html')
