name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if line.startswith("From "):
        # print(line)
        time = line.split()[5]
        # print(time)
        hour = time.split(":")[0]
        # print(hour)
        hours[hour] = hours.get(hour, 0) + 1
# print(hours)
for k, v in sorted(hours.items()):
    print(k, v)
# sorted_hours = sorted([(v, k) for k, v in hours.items()], reverse=True)
# print(sorted_hours)
