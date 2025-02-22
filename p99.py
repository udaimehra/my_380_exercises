hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
t = 'True'
try:
  for i in hashtags:
      x=str(type(i))
      tp = x.split(' ')
      ttp=tp[1].rstrip(">")
      #print(ttp)
      if ttp != "'str'":
          t = 'False'
          #print("ABC")
  print(t)
except:
  print("False")
