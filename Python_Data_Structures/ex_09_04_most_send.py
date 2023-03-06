name = input('Enter file:')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
senders = dict()
for line in handle:
    if line.strip().startswith('From:'):
        sender = line.split()[1]
        senders[sender] = senders.get(sender, 0) + 1

best_sender = None
best_count = None
for sender, count in senders.items():
    if best_count is None or count > best_count:
        best_sender = sender
        best_count = count
print(best_sender, best_count)
