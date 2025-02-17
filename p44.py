url = (
    "https://e-smartdata.teachable.com/p/"
    "sciezka-data-scientist-machine-learning-engineer"
)
url_arr=url.split('/')
last_string= url_arr[len(url_arr)-1]
print(last_string.replace('-', ' '))
