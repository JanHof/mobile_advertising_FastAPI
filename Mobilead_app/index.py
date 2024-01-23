from fastapi import FastAPI
from routes import user, devices, companies, campaigns, impressions 
app = FastAPI()

app.include_router(devices)
app.include_router(companies)
app.include_router(campaigns)
app.include_router(impressions)
app.include_router(user)

