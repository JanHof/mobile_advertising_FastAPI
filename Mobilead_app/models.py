# from pydantic import BaseModel
# from motor.motor_asyncio import AsyncIOMotorCollection
# from odmantic import Model, Field, ObjectId
from datetime import datetime
# from bson.objectid import ObjectId
from typing import List, Optional
# from schemas import DeviceBase


from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Device(BaseModel):
    age: int
    gender: str
    location: List[str]
    language: str
    device_type: str
    device_OS: str
    interest: List[str]
    purchase_history: List[str]
    social_media: List[str]
    created_at: datetime
    updated_at: datetime


class Company(BaseModel):
    comp_name: str
    comp_details: str
    contact_details: str
    campaigns: List[str]



class Campaign(BaseModel):
    name: str
    start_date: str
    end_date: str
    budget: float
    imp_rate: float
    click_rate: float
    purchase_rate: float


class Impression(BaseModel):
    camp_id: str
    datetime: str
    click_on: bool
    click_through: bool
    purchase: bool
    device_id: str
