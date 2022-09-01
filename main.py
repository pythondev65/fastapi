

from asyncio import sleep
import asyncio
from typing import Union
from fastapi.responses import JSONResponse
from fastapi import Body, FastAPI, status
from fastapi import FastAPI
import logging


app = FastAPI()


@app.get("/valid/")
async def read_item(is_valid_input):
    print(type(is_valid_input))
    print("data=>", is_valid_input.isdigit())
    if is_valid_input.isdigit():
           return JSONResponse(status_code=400, content="Integer is not allowed")
    elif is_valid_input.islower():
        return {"Success"}
    elif is_valid_input.isupper():
        return {"Fail"}
    else:
        return JSONResponse(status_code=501, content="data type float is not allowed")
    
    
@app.post("/process/")
async def read_item(x):
        data=x
        print(f'asyncio message worker 2 Hello!')
        await asyncio.sleep(180)
        query="INSERT INTO dataset(input) VALUES(data)"
        return {"Success"}
        
    
    


            
           

        
        