is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
unique_id = is_clicked.intersection(is_bought)
print(f'Customer ID: {unique_id}')
