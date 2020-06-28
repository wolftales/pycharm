opponent = int(input())

if opponent < 1:
    print('no army')
elif 1 <= opponent < 10:
    print('few')
elif 10 <= opponent < 50:
    print('pack')
elif 50 <= opponent < 500:
    print('horde')
elif 500 <= opponent < 1000:
    print('swarm')
elif 1000 <= opponent:
    print('legion')
