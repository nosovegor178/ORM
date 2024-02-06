from django.utils.timezone import localtime
from django.utils import timezone


def get_duration_of_one_man_visit(visit):
    entry_local_time = localtime(visit.entered_at)
    now = localtime(timezone.now())
    if visit.leaved_at != None:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = entry_local_time - now
    return duration