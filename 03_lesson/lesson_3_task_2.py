from Smartphone import Smartphone 

catalog = [
Smartphone ("iPhone", "13Pro", "+71234567"), 
Smartphone ("Honor", "13Pro", "+71234567"), 
Smartphone ("Fly", "13Pro", "+71234567"), 
Smartphone ("Redme", "13Pro", "+71234567"), 
Smartphone ("Samsung", "13Pro", "+71234567") 
]

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
