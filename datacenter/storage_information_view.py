from django.shortcuts import render
from datacenter.models import Visit
from django.utils.timezone import localtime
from .helpers import get_duration, format_duration, is_visit_long, SUSPICIOUS_VISIT_MINUTES


def storage_information_view(request):
    """Основная view для отображения активных посещений"""
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    
    non_closed_visits = []
    for visit in active_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': formatted_duration,
            'is_strange': is_visit_long(visit, minutes=SUSPICIOUS_VISIT_MINUTES)
        })
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)