from django.utils.timezone import localtime


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
SUSPICIOUS_VISIT_MINUTES = 60


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = localtime() - visit.entered_at
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f"{hours:02}:{minutes:02}"


def is_visit_long(visit, minutes=SUSPICIOUS_VISIT_MINUTES):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * SECONDS_IN_MINUTE