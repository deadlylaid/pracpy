num=int(input())
room=set([])
for _ in range(num):
    name, status = map(str, input().split())

    if status == 'enter':
        room.add(name)
    else:
        room.remove(name)

room=list(room)
room.sort(reverse=True)
for i in room:
    print(i)
