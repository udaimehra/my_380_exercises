code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f"code1: {not(code1.endswith('-20'))}")
print(f"code2: {not(code2.endswith('-20'))}")

code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')
