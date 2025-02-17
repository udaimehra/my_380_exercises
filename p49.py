is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
unique_id = is_clicked.symmetric_difference(is_bought)
print(unique_id)
