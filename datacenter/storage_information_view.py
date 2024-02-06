from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .general_functions import get_duration_of_one_man_visit


def storage_information_view(request):
    def get_formating_time(time):
        total_seconds = time.seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f'{hours}:{minutes}:{seconds}'
    peoples_that_now_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for one_man in peoples_that_now_in_storage:
        duration = get_duration_of_one_man_visit(one_man)
        entry_local_time = localtime(one_man.entered_at)
        visit_time = get_formating_time(duration)
        one_man_name = one_man.passcard.owner_name
        one_man_visit = {
            'who_entered': one_man_name,
            'entered_at': entry_local_time,
            'duration': visit_time,
        }
        non_closed_visits.append(one_man_visit)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
