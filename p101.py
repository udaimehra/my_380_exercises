gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
USDPLN = 4.0
for k,v in gaming.items():
    if v[1] == 'USD':
        v[0] = 4.0*float(v[0])
        v[1] = 'PLN'
print(gaming)
