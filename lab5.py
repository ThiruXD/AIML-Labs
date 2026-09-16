# Super short version – just shows final Version Space

S = {('MP', '?', '?', '?', 'Online')}
G = {
    ('MP', '?', '?', '?', '?'),
    ('?', '?', '?', 'Employed', '?'),
    ('?', '?', 'Bachelor', '?', '?'),
    ('?', '?', 'College', '?', '?'),
    ('?', 'NA', '?', '?', '?'),
    ('?', 'Savings', '?', '?', '?')
}

unseen = ('MP', 'Current', 'Bachelor', 'Unemployed', 'Online')

def covers(h, x):
    return all(a == '?' or a == b for a, b in zip(h, x))

print("Specific boundary S:")
for h in S: print(" ", h)

print("\nGeneral boundary G:")
for h in G: print(" ", h)

print("\nUnseen:", unseen)
print("Decision:", "Y (Approve Loan)" if all(covers(h, unseen) for h in S|G) else "N")
