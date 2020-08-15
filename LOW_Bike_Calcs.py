from math import floor


def adjust_times(mins_in, secs_in, ratio):
    mins_adj = [ratio*x for x in mins_in]
    secs_adj = [ratio*x for x in secs_in]
    mins_final = []
    secs_final = []

    for min_time, sec_time in zip(mins_adj, secs_adj):
        extra_secs = min_time - floor(min_time)
        min_time = floor(min_time)
        sec_time += extra_secs*60

        while sec_time >= 60:
            sec_time -= 60
            min_time += 1

        mins_final.append(min_time)
        secs_final.append(sec_time)
    secs_final = readjust_secs(secs_final)

    return mins_final, secs_final


def readjust_secs(secs_in):
    # Take leftover decimals from seconds and add it to the final entry.
    leftover_decimals = 0
    for c, sec in enumerate(secs_in):
        extra_decs = sec - floor(sec)
        secs_in[c] = floor(secs_in[c])
        leftover_decimals += extra_decs
    secs_in[-1] += leftover_decimals
    secs_in[-1] = floor(secs_in[-1])

    return secs_in


def print_time_splits(mins_in, secs_in, time_name):
    print("\n\n", time_name, " Times: \n")
    for counter in range(len(mins_in)):
        sec_string = str(secs_in[counter]) if secs_in[counter]>9 else "0"+str(secs_in[counter])
        temp_time = str(mins_in[counter])+":"+sec_string
        print(temp_time)


def print_time_splits_names(mins_in, secs_in, time_name, split_names):
    print("\n\n", time_name, " Times: \n")
    for counter in range(len(split_names)):
        sec_string = str(secs_in[counter]) if secs_in[counter]>9 else "0"+str(secs_in[counter])
        temp_time = str(mins_in[counter])+":"+sec_string
        print(temp_time, "\t", split_names[counter])


def write_time_splits_names(mins_in, secs_in, split_names, file_name):
    file_name = file_name+".txt"
    with open(file_name, 'w') as f:

        f.write(file_name+": \n\n")
        f.write("Time\tSplit Name\n")
        f.write("================\n")

        for counter in range(len(split_names)):
            sec_string = str(secs_in[counter]) if secs_in[counter]>9 else "0"+str(secs_in[counter])
            temp_time = str(mins_in[counter])+":"+sec_string
            f.write(temp_time+"\t"+split_names[counter])
            f.write("\n")


def get_mins_secs_total(mins_in, secs_in):
    total_mins = sum(mins_in)
    total_secs = sum(secs_in)
    while total_secs >= 60:
        total_secs -= 60
        total_mins += 1
    return total_mins, total_secs


def print_time_total(mins_in, secs_in, time_name):
    total_mins, total_secs = get_mins_secs_total(mins_in, secs_in)
    total_secs = str(total_secs) if total_secs>9 else "0"+str(total_secs)
    print("\n\nTotal ", time_name, " Time: ", total_mins, ":", total_secs)


def get_decimal_times(mins_in, secs_in):
    decimal_times = [x+(y/60) for x, y in zip(mins_in, secs_in)]
    return decimal_times


def get_ratio_of_split_times(mins_in1, secs_in1, mins_in2, secs_in2):
    time_list_1 = get_decimal_times(mins_in1, secs_in1)
    time_list_2 = get_decimal_times(mins_in2, secs_in2)
    ratio_list = [one/two for one, two in zip(time_list_1, time_list_2)]
    return ratio_list


def main():
    # First, the Recorded Splits - 10 around the lake
    split_names = ["Dead Indian", "West Side Entry", "1st Peak West",
                   "2nd Peak (MacDonnel)", "Camp McLoughlin", "Aspen Point",
                   "Resort Entry Road", "Sunset Boat Launch", "Top of Sunset",
                   "East Side Homeowners"]

    #  Tommy's real 41:55 timing
    tommy_real_mins = [2, 3, 4, 3, 4, 8, 4, 6, 2, 2]
    tommy_real_secs = [32, 54, 9, 48, 19, 4, 2, 41, 19, 7]
    print_time_total(tommy_real_mins, tommy_real_secs, "Tommy")

    #  Tommy's (approximated) 42:45 timing
    tommy_approx_mins = [2, 4, 4, 4, 4, 8, 4, 6, 2, 2]
    tommy_approx_secs = [35, 0, 10, 0, 20, 10, 0, 45, 30, 15]
    # tommy_approx = [x+(y/60) for x, y in zip(tommy_approx_mins, tommy_approx_secs)]

    # print_time_splits_names(tommy_real_mins, tommy_real_secs, "Tommy Real", split_names)

    # Lauren's real timing
    lauren_real_mins = [3, 5, 6, 5, 6, 13, 5, 9, 3, 4]
    lauren_real_secs = [41, 49, 32, 46, 24, 20, 34, 50, 7, 32]

    # Lauren's approx 1:04 timing
    lauren_approx_mins = [3, 5, 6, 5, 6, 13, 5, 9, 3, 4]
    lauren_approx_secs = [40, 50, 30, 45, 30, 20, 35, 50, 0, 30]


    # print_time_splits(lauren_real_mins, lauren_real_secs, "Lauren Real")
    # print_time_splits(lauren_approx_mins, lauren_approx_secs, "Lauren Approx")


    """
    Hypothetical Times: Gold (45 mins), Silver, (60 mins), Bronze (75 mins)
    All based off Tommy's 42:01
    """
    mins = tommy_real_mins
    secs = tommy_real_secs

    gold_mins, gold_secs = adjust_times(mins, secs, 45/41.9166666666666)
    print_time_splits_names(gold_mins, gold_secs, "Gold", split_names)
    write_time_splits_names(gold_mins, gold_secs, split_names, "Gold Times")

    # print_time_total(gold_mins, gold_secs, "Gold")


    silver_mins, silver_secs = adjust_times(mins, secs, 60/41.9166666666666)
    print_time_splits_names(silver_mins, silver_secs, "Silver", split_names)
    write_time_splits_names(silver_mins, silver_secs, split_names, "Silver Times")

    # print_time_total(silver_mins, silver_secs, "Silver")

    bronze_mins, bronze_secs = adjust_times(mins, secs, 75/41.9166666666666)
    print_time_splits_names(bronze_mins, bronze_secs, "Bronze", split_names)
    write_time_splits_names(bronze_mins, bronze_secs, split_names, "Bronze Times")

    # print_time_total(bronze_mins, bronze_secs, "Bronze")


    """
    Challenge Times: Gold (40 mins), Silver, (50 mins), Bronze (60 mins)
    """


    gold_challenge_mins, gold_challenge_secs = adjust_times(mins, secs, 40/41.9166666666666)
    print_time_splits_names(gold_challenge_mins, gold_challenge_secs, "Gold", split_names)
    write_time_splits_names(gold_mins, gold_secs, split_names, "Gold Challenge Times")
    # print_time_total(gold_challenge_mins, gold_challenge_secs, "Gold")


    silver_challenge_mins, silver_challenge_secs = adjust_times(mins, secs, 50/41.9166666666666)
    print_time_splits_names(silver_challenge_mins, silver_challenge_secs, "Silver", split_names)
    write_time_splits_names(silver_mins, silver_secs, split_names, "Silver Challenge Times")
    # print_time_total(silver_challenge_mins, silver_challenge_secs, "Silver")

    bronze_challenge_mins, bronze_challenge_secs = adjust_times(mins, secs, 60/41.9166666666666)
    print_time_splits_names(bronze_challenge_mins, bronze_challenge_secs, "Bronze", split_names)
    write_time_splits_names(bronze_mins, bronze_secs, split_names, "Bronze Challenge Times")

    # print_time_total(bronze_challenge_mins, bronze_challenge_secs, "Bronze")


    print("\n\n")


if __name__ == "__main__":
    main()
