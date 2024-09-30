d = {1:'hii',2:'how',3:'are',4:'you',5:'naresh'}
dt = {x:y for x,y in d.items() if len(y) > 3}
print(dt)

d1 = ['    hii','10','tree','type','   naresh']
dt = {i.strip():len(i) for i in d1 if i.isalpha() or i.isspace()}
print(dt)