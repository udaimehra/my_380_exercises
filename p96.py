gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for k,v in gaming.items():
    #print(k, gaming[k])
    if float(gaming[k]) >100.0:
        print(k)
