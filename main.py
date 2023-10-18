from typing import Optional

from fastapi import FastAPI, Query, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from src.service_weather import Weather


############## BACKEN  API  ##############

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Coordenadas(BaseModel):
    latitud: str
    longitud: str


@app.get("/api/EPOC/information/weather")
def weather_information():
    return {"answer": 'hola'}


@app.post("/api/EPOC/dowload_information")
def download_information(
                        coordenadas: Coordenadas = Body(..., 
     
                                                        description='It is necesary latitud and longitud to get information')):
    weather = Weather()
    answer = weather.sent_information(coordenadas = dict(coordenadas))
    return {"answer": answer}