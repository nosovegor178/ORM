from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .general_functions import get_duration_of_one_man_visit


def is_visit_suspicious(visit, minutes=60):
    seconds = minutes*minutes
    long_visit = visit.seconds > seconds
    return long_visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    visits_by_this_person = Visit.objects.filter(passcard = passcard)
    for visit in visits_by_this_person:
        duration = get_duration_of_one_man_visit(visit)
        visit_suspicion = is_visit_suspicious(duration)
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': visit_suspicion
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
