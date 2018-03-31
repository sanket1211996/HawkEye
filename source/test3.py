
import json

data={}
mdata={}
count=1
data['label'] ='person1'
data['confidence']='60'
mdata.update(data)
print(mdata)
data['label'] ='person2'
data['confidence']='50'
mdata.update(data)
print(mdata)
data['label'] ='person3'
data['confidence']='40'
mdata.update(data)

print(mdata)