LOW Code OLD



    ratio_tom_lau = get_ratio_of_split_times(tommy_real_mins, tommy_real_secs,
                                             lauren_real_mins, lauren_real_secs)

    """
    print("Ratios of Tommy to Lauren: \n")
    for rat in ratio_tom_lau:
        print(rat)

    ratio_avg = sum(ratio_tom_lau)/len(ratio_tom_lau)
    print("Average: ", ratio_avg)

    print("\n\nDifference from average: \n")
    for rat in ratio_tom_lau:
        print((rat-ratio_avg)*100)
    """

    
"""
# Silver Hypothetical times - 55:00 timing
silver_mins = [3, 5, 6, 5, 5, 10, 4, 7, 3, 2]
silver_secs = [30, 10, 30, 15, 50, 40, 45, 45, 0, 35]

silver = [x+(y/60) for x, y in zip(silver_mins, silver_secs)]
"""
"""
print("Split Silver times:\n\n", silver)

print("\n\nSilver Mins Total: \n", sum(silver_mins))
print("\n\nSilver Secs Total: \n", sum(silver_secs))

print("\n\nSilver Times Total: \n", sum(silver))

print("\n\nRatio to Bronze (55 min to 1 hr 15): ", 75/55)
"""

"""
# Bronze times - 1 hour, 15 mins timing (75 mins)
ratio = 75/55
bronze_mins, bronze_secs = adjust_times(silver_mins, silver_secs, ratio, "Bronze")

bronze_mins_naive = [(75/55)*x for x in silver_mins]

print_time_total(bronze_mins, bronze_secs, "Bronze")

ratio_bronze_to_silver = [b/s for b, s in zip (bronze, silver)]
print("\n\nRatio of Bronze to Silver: \n", ratio_bronze_to_silver)

get_ratio_of_split_times(mins_in1, secs_in1, mins_in2, secs_in2)
"""

proposed_bronze_mins = [4, 7, 9, 7, 8, 14, 6, 10, 4, 3]
proposed_bronze_secs = [45, 0, 0, 0, 0, 30, 30, 45, 0, 30]
proposed_bronze = [x+(y/60) for x, y in zip(proposed_bronze_mins, proposed_bronze_secs)]
# print("\n\nProposed Bronze Times Total: \n", sum(proposed_bronze))

total_time_mins = 0
total_time_secs = 0
for counter in range(len(proposed_bronze_mins)):

    total_time_mins += proposed_bronze_mins[counter]
    total_time_secs += proposed_bronze_secs[counter]

    while total_time_secs >= 60:
        total_time_secs -= 60
        total_time_mins += 1

    # print("Time:  ", total_time_mins, ":", total_time_secs)
