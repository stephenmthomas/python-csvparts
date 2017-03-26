import csv
import operator

part_list = csv.reader(open('parts.csv','r'),delimiter=',')

running_val = 0
cumulative_val = 0
tot_parts = 0
run_parts = 0
b_printed = 0
c_printed = 0

parts = sorted(part_list, key=lambda x:float(x[3]), reverse=True)


#Calculate the cumulative dollar volume upfront, and number of parts
for part in parts:
    cumulative_val = cumulative_val + float(part[3])
    tot_parts = tot_parts + 1

print "Part #   Price   Yr.Dmnd   Dlr Vol   Cumulative Volume"

print "\nA LIST(85% of value):"

#Iterate thru the list, calculating the cumulative percentage and parts percentage
for part in parts:
    running_val = running_val + float(part[3])
    run_parts = run_parts + 1

    item_bin = running_val / cumulative_val
    part_percentage = run_parts / tot_parts

    if item_bin > 0.85:
        if b_printed < 1:
            print "\nB LIST(10% of value):"
            b_printed = 1

    if item_bin > 0.9:
        if c_printed < 1:
            print "\nC LIST(5% of value):"
            c_printed = 1
    print part[0].ljust(9) +  part[1].ljust(8) +  part[2].ljust(10) +  part[3].ljust(10) + str(running_val)


