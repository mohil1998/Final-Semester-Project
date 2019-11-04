from django.shortcuts import render

def index(request):
    return render(request, 'letsChat/index.html', {})

def room(request, room_name):
    return render(request, 'letsChat/room.html', {
        'room_name_json': room_name,
        #'user_name_json': user_name,
    })
