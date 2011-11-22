from weather.events.models import WxEvent, EventType
from django.shortcuts import render_to_response

def homepage(request):
    weather=WxEvent.objects.order_by('event_type')
    return render_to_response('homepage.html',{
        'weather':weather,
})

def detail(request, weather_id):
    weather = WxEvent.objects.get(id=weather_id)

    return render_to_response('detail.html',{
        'weather':weather,
})


def event_type_list(request):
    types=EventType.objects.order_by('event_type')
    return render_to_response('eventtypelist.html',{
        'types':types,
})

def event_type_detail(request, type_id):
    wxtype = EventType.objects.get(id=type_id)
    weather = WxEvent.objects.filter(event_type=wxtype)
    return render_to_response('eventtypedetail.html',{
        'weather':weather,
        'wxtype': wxtype,
})

