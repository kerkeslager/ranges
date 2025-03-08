import json

r = {}

RANKS = 'AKQJT98765432'

for i in range(len(RANKS)):
    for j in range(len(RANKS)):
        if i < j:
            r[RANKS[i] + RANKS[j] + 's'] = 7
        elif i > j:
            r[RANKS[j] + RANKS[i] + 'o'] = 7
        else:
            r[RANKS[i] + RANKS[j]] = 7

struct = {
    'range': r,
}

print(json.dumps(struct, indent=2))

