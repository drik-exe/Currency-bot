from fastapi import FastAPI
import requests
import uvicorn
from typing import Optional

app = FastAPI()


@app.get("/national_bank/{currency}/{date}")
async def national_bank( currency: str, date: str) -> float:
    if currency == "USD":
        currency = 431
    elif currency == "EUR":
        currency = 451
    elif currency == "GPB":
        currency = 429
    elif currency == "JPY":
        currency = 508
        
    response = None
    
    if date != "0":
        request = requests.get(f"https://api.nbrb.by/exrates/rates/{currency}?ondate={date}")
        response = request.json()
        return response["Cur_OfficialRate"]
    elif date == "0":
        request = requests.get(f"https://api.nbrb.by/exrates/rates/{currency}")
        response = request.json()
        return response["Cur_OfficialRate"]
    
    

app.get("/belarus_bank/{currency}/{date}")
async def belarus_bank():
    request = requests.get("https://belarusbank.by/api/kursExchange")
    response = request.json()
    print(response)
        
    

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)