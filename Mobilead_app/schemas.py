
# from typing import List, Optional
# from bson.objectid import ObjectId
from datetime import datetime
# #from odmantic import Model, ObjectId, Field
# from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from bson.objectid import ObjectId



# User Schema
async def userEntity(item) -> dict:
    item_id = item["_id"]
    if hasattr(item_id, "wait"):
        item_id = await item_id
    return {
        "id": str(item_id),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

async def usersEntity(entity) -> list:
    if hasattr(entity, "to_list"):
        entity = await entity.to_list(length=None)
    return [await userEntity(item) for item in entity]

# device schema
async def deviceEntity(item) -> dict:
    item_id = item["_id"]
    if hasattr(item_id, "wait"):
        item_id = await item_id
    return{
        "device_id":str(item_id),
        "age": item["age"],
        "gender": item["gender"],
        "location": item["location"],
        "language": item["language"],
        "device_type": item["device_type"],
        "device_OS": item["device_OS"],
        "interest": item["interest"],
        "purchase_history": item["purchase_history"],
        "social_media": item["social_media"],
        "created_at": item.get("created_at", datetime.utcnow()),
        "updated_at": item.get("updated_at", datetime.utcnow())
    }

# devices schema
async def devicesEntity(entity) -> list:
    if hasattr(entity, "to_list"):
        entity = await entity.to_list(length=None)
    return [await deviceEntity(item) for item in entity]   


# company schema
async def companyEntity(item) -> dict:
    item_id = item["_id"]
    if hasattr(item_id, "wait"):
        item_id = await item_id
    return{
        "comp_id": str(item_id),
        "comp_name": item["comp_name"],
        "comp_details": item["comp_details"],
        "contact_details": item["contact_details"],
        "campaigns": item["campaigns"]
    }

# companies schema 
async def companiesEntity(entity) -> list:
    if hasattr(entity, "to_list"):
        entity = await entity.to_list(length=None)
    return [await companyEntity(item) for item in entity]   

# campaign schema
async def campaignEntity(item) -> dict:
    item_id = item["_id"]
    if hasattr(item_id, "wait"):
        item_id = await item_id
    return{
        "camp_id": str(item_id),
        "name": item["name"],
        "start_date": item["start_date"],
        "end_date": item["end_date"],
        "budget": item["budget"],
        "imp_rate": item["imp_rate"],
        "click_rate": item["click_rate"],
        "purchase_rate": item["purchase_rate"]
    }

# campaign schema
async def campaignsEntity(entity) -> list:
    if hasattr(entity, "to_list"):
        entity = await entity.to_list(length=None)
    return [await campaignEntity(item) for item in entity]  
     

# impression schema
async def impressionEntity(item) -> dict:
    item_id = item["_id"]
    if hasattr(item_id, "wait"):
        item_id = await item_id
    return{
        "imp_id": str(item_id),
        "camp_id": item["camp_id"],
        "datetime": item["datetime"],
        "click_on": item["click_on"],
        "click_through": item["click_through"],
        "purchase": item["purchase"],
        "device_id": item["device_id"]
    }

# impressions schema
async def impressionsEntity(entity) -> list:
    if hasattr(entity, "to_list"):
        entity = await entity.to_list(length=None)
    return [await impressionEntity(item) for item in entity]  
    