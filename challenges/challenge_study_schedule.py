def study_schedule(permanence_period, target_time):
    qnt = 0
    for period in permanence_period:
        if target_time is None or period[0] is None or period[1] is None:
            return None
    for period in permanence_period:
        if period[0] <= target_time <= period[1]:
            qnt += 1

    return qnt
