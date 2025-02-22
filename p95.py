indexes = [
    "BOVESPA",
    "DOW JONES COMP",
    "DOW JONES INDU",
    "DOW JONES TRANS",
    "DOW JONES UTIL",
    "IPC",
    "IPSA",
    "MERVAL",
    "NASDAQ COMP",
    "NASDAQ100",
    "S&P500",
    "S&P/TSX COMP",
]
a = 'DOW'
b = "S&P"
for i in indexes:
    if i.startswith(a) or i.startswith(b):
        print(i)
    if 'DOW' in i or 'S&P' in i:
        print(i)
