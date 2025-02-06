n, h = map(int, input().split())
cards = list(map(int, input().split()))

total_damage = 0
count = 0

for card in cards:
    total_damage += card
    count += 1
    if total_damage >= h:
        print(count)
        break
else:
    print(-1)