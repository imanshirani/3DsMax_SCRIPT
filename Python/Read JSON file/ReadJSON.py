'''
An example of how to get deta From Json and add to Dummy By iman shirani
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



custAttribute = rt.execute(f'''
global attrib
attrib = attributes Custom_Attributes 
version:0
(    
  Parameters main1 rollout:params
  (  
    _Price Type:#integer UI:price_UI
    _date Type:#string UI:date_UI
    _Name Type:#string UI:name_UI
  )    
  
  Rollout Params "Attributes"
  (  
    spinner price_UI "Price: " range:[0, 100000000, 0] Align:#left Type:#integer autoDisplay:true 
    editText date_UI "Date: "  Align:#left Type:#string autoDisplay:true
    editText name_UI "Name: " Align:#left Type:#string
  )
)
''')

def make_dummy():
        for iman in Name:
            dummy= rt.dummy()
            dummy.name = iman['name']
            dataset= rt.EmptyModifier(name='Data set') 
            rt.custAttributes.add(dataset, rt.attrib,)
            dataset._Name = iman['name']
            dataset._Price = iman['price']            
            dataset._date =  iman['date'] 
            rt.addModifier(dummy, dataset)
            
        
def make_sphere():
    for iman in Name:
        node=rt.Sphere(name= iman['name'],radius= iman['price'], segments= 32)
        print(node)
               
 
def make_text():
    for iman in Name:
        textp = rt.text()
        textp.name= iman['name']
        textp.text= iman['name']
        
        dataset= rt.EmptyModifier(name='Data set') 
        rt.custAttributes.add(dataset, rt.attrib,)
        dataset._Name = iman['name']
        dataset._Price = iman['price']            
        dataset._date =  iman['date'] 
        rt.addModifier(textp, dataset)  
        
        Bevel= rt.Bevel_Profile()
        Bevel.ExtrudeAmount = dataset._Price
        Bevel.Extrudesegments= 10
        
        rt.addModifier(textp, Bevel)
	
    
    
make_text()    


#make_dummy()
#make_sphere()
