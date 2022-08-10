'''
An example of how to get deta From Json and add to Dummy 
'''

import pymxs
from pymxs import runtime as rt
#from pymxs import runtime as mxs
import json
from unicodedata import name

with open('Data\Data.json', 'r') as f:
  Data_JSON = json.loads(f.read())

# Output: {'name': 'Bob'}
Name = (Data_JSON)
# Name = (Data_JSON[0]['name'])
iman = int(Name[2]['price'])

for iman in Name:
#      print(iman)
#     print(iman['name'])
      print(iman['price'])
#      total= iman

#      print(total)

#print(Name)


custAttribute = rt.execute(f'''
global attrib
attrib = attributes Custom_Attributes 
version:0
(    
  Parameters main1 rollout:params
  (  
    _Price Type:#integer UI:price_UI
    _data Type:#integer UI:data_UI
    _Name Type:#string UI:name_UI
  )    
  
  Rollout Params "Attributes"
  (  
    spinner price_UI "Price: " Align:#left Type:#integer autoDisplay:true 
    spinner data_UI "Data: " Align:#left Type:#integer autoDisplay:true 
    editText name_UI "Name: " Align:#left Type:#string
  )
)
''')

def make_dummy():
        for iman in Name:
            dummy= rt.dummy()
            dummy.name = iman['name']
            dataset= rt.EmptyModifier(name='Data set') 
            rt.custAttributes.add(dataset, rt.attrib)
            dataset._Name = iman['name']
            dataset._Price = iman['price']
            dataset._data = 0
            rt.addModifier(dummy, dataset)
            
        
def make_sphere():
    for iman in Name:
        node=rt.Sphere(name= iman['name'],radius= iman['price'], segments= 32)
        
         
         
  
def apply_bend_to_mesh(): 
    for iman in Name:
        bend= rt.bend(name='Bend iman')
        bend.bendAngle = 0
        rt.addModifier(node, bend)
            
          
make_dummy()
#make_sphere()
