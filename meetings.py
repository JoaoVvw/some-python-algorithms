a = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
a_limit = ["9:00", "20:00"]
b = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
b_limit = ["10:00", "18:30"]
ab_limit = []
busy = []
available = []
both_available = []
both_available2 = []
starts = []
ends = []
temp_compiled1 = []
compiled = []


def compare_a_b():
    def time_adder(list_of_meetings, lists, is_limit):
        for meetings in list_of_meetings:
            temp_lists = []
            if not is_limit:
                if meetings[0] not in starts:
                    ends.append(meetings[0])
                else:
                    lists.append(meetings[0])
                if meetings[1] not in ends:
                    starts.append(meetings[1])
                else:
                    lists.append(meetings[1])
                meeting_start = meetings[0]
                meeting_end = meetings[1]
                hour1 = int(meeting_start.split(":")[0])
                minute1 = int(meeting_start.split(":")[1])
                hour2 = int(meeting_end.split(":")[0])
                minute2 = int(meeting_end.split(":")[1])
            else:
                lists.append(list_of_meetings[0])
                hour1 = int(list_of_meetings[0].split(":")[0])
                minute1 = int(list_of_meetings[0].split(":")[1])
                hour2 = int(list_of_meetings[1].split(":")[0])
                minute2 = int(list_of_meetings[1].split(":")[1])
            while hour1 != hour2 or minute1 != minute2:
                if hour2 > hour1:
                    while minute1 < 59:
                        minute1 += 1
                        temp_time1 = [str(hour1), ":", str(minute1)]
                        temp_time2 = "".join(temp_time1)
                        if temp_time2 not in temp_lists:
                            temp_lists.append(temp_time2)
                if minute1 == 59:
                    hour1 += 1
                    minute1 = 0
                    temp_time1 = [str(hour1), ":", str(minute1)]
                    temp_time2 = "".join(temp_time1)
                    if temp_time2 not in temp_lists:
                        temp_lists.append(temp_time2)
                if hour1 == hour2:
                    while minute1 != minute2:
                        minute1 += 1
                        temp_time1 = [str(hour1), ":", str(minute1)]
                        temp_time2 = "".join(temp_time1)
                        if temp_time2 not in temp_lists:
                            temp_lists.append(temp_time2)
            if not is_limit:
                temp_lists.pop(-1)
            for values in temp_lists:
                if values not in lists:
                    lists.append(values)

    def limit_setter():
        earlier_hour_end = 0
        earlier_minute_end = 0
        meeting_start2 = a_limit[0]
        meeting_end2 = a_limit[1]
        a_hour1 = int(meeting_start2.split(":")[0])
        a_minute1 = int(meeting_start2.split(":")[1])
        a_hour2 = int(meeting_end2.split(":")[0])
        a_minute2 = int(meeting_end2.split(":")[1])
        meeting_start2 = b_limit[0]
        meeting_end2 = b_limit[1]
        b_hour1 = int(meeting_start2.split(":")[0])
        b_minute1 = int(meeting_start2.split(":")[1])
        b_hour2 = int(meeting_end2.split(":")[0])
        b_minute2 = int(meeting_end2.split(":")[1])
        if a_hour1 > b_hour1:
            later_hour_start = a_hour1
            later_minute_start = a_minute1
        elif a_hour1 < b_hour1:
            later_hour_start = b_hour1
            later_minute_start = b_minute1
        else:
            if a_minute1 > b_minute1:
                later_hour_start = a_hour1
                later_minute_start = a_minute1
            else:
                later_hour_start = b_hour1
                later_minute_start = b_minute1
        if a_hour2 < b_hour2:
            earlier_hour_end = a_hour2
            earlier_minute_end = a_minute2
        elif a_hour2 > b_hour2:
            earlier_hour_end = b_hour2
            earlier_minute_end = b_minute2
        else:
            if a_minute2 < b_minute2:
                later_hour_start = a_hour1
                later_minute_start = a_minute1
            else:
                earlier_hour_end = b_hour2
                earlier_minute_end = b_minute2
        temp_start1 = [str(later_hour_start), ":", str(later_minute_start)]
        temp_start2 = "".join(temp_start1)
        temp_end1 = [str(earlier_hour_end), ":", str(earlier_minute_end)]
        temp_end2 = "".join(temp_end1)
        ab_limit.append(temp_start2)
        ab_limit.append(temp_end2)
        time_adder(ab_limit, available, True)

    def both_available_setter():
        for times1 in available:
            if times1 not in busy and times1 not in both_available:
                both_available.append(times1)

    def compiler(temp_compiled):
        counter = -1
        both_available2.append(both_available[0])
        while counter < len(both_available) - 2:
            counter += 1
            c_hour1 = int(both_available[counter].split(":")[0])
            c_minute1 = int(both_available[counter].split(":")[1])
            c_hour2 = int(both_available[counter + 1].split(":")[0])
            c_minute2 = int(both_available[counter + 1].split(":")[1])
            if c_hour1 != c_hour2 and c_minute1 + 1 != c_minute2 and c_hour1 + 1 != c_hour2 and c_minute1 - 59 != 0:
                temp_time3 = [str(c_hour1), ":", str(c_minute1)]
                temp_time4 = "".join(temp_time3)
                temp_time5 = [str(c_hour2), ":", str(c_minute2)]
                temp_time6 = "".join(temp_time5)
                both_available2.append(temp_time4)
                both_available2.append(temp_time6)
        both_available2.append(both_available[-1])
        for values in both_available2:
            temp_compiled.append(values)
            if len(temp_compiled) == 2:
                compiled.append(temp_compiled)
                temp_compiled = []
    time_adder(a, busy, False)
    time_adder(b, busy, False)
    limit_setter()
    both_available_setter()
    compiler(temp_compiled1)


compare_a_b()
print(compiled)


