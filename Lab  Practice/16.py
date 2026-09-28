# Activity Selection for Meeting Scheduling

def select_meeting_activities(activities):
    acts = sorted(activities, key=lambda a: (int(a[2]), int(a[1]), str(a[0])))

    selected = []
    last_finish = None

    for a in acts:
      aid, start, finish = a[0], int(a[1]), int(a[2])

      if last_finish is None:
        selected.append((aid, start, finish, "Selected first because it finishes earliest"))
        last_finish = finish
      elif start >= last_finish:
        selected.append((aid, start, finish, "Selected because start time is compatible"))
        last_finish = finish

    print("Activity Selection Report")
    print("Selected Activities")
    print("Activity Start Finish Reason")
    for aid, start, finish, reason in selected:
      print(aid, start, finish, reason)
    print("Total Selected:", len(selected))
    print("Justification: Greedy selection by earliest finish time maximizes compatible activities")

    return []