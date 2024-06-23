import requests
from requests import Response
from pprint import pprint
from pydantic import BaseModel, Field, ValidationError, field_validator, RootModel

class bike(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:int
    total:int
    available_rent_bikes:int
    latitude:int
    longitude:int
    available_return_bikes:int

class Root(RootModel):
    root:list[bike]


youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
res:Response = requests.get(youbike_url)

if res.ok:
    print("下載成功")
else:
    print("下載失敗")

text = res.text

