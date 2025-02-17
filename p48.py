ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
unique_id = set()
for i in ad1_id:
    if i not in ad2_id:
        unique_id.add(i)
for i in ad2_id:
    if i not in ad1_id:
        unique_id.add(i)
print(f'Selected ID: {unique_id}')
