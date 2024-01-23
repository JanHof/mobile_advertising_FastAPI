from fastapi import APIRouter, HTTPException, Depends, status
from models import User, Device, Company, Campaign, Impression 
from config import conn 
from schemas import usersEntity, userEntity, deviceEntity, devicesEntity, companyEntity,companiesEntity, campaignsEntity, campaignEntity, impressionsEntity, impressionEntity
from bson.objectid import ObjectId
from services import hash_password, verify_password, generate_token, verify_token, login_user_service
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from uuid import uuid4


 
devices = APIRouter()
companies = APIRouter()
campaigns = APIRouter()
impressions = APIRouter()
user = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@user.get('/')
async def find_all_users(token: str = Depends(oauth2_scheme)):
    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    return await usersEntity(conn["azul"]["user"].find())

@user.get('/users/{id}')
async def find_one_user(id, token: str = Depends(oauth2_scheme)):
    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await conn["azul"]["user"].find_one({"_id": ObjectId(id)})
    if user:
        return await userEntity(user)
    return None

@user.post('/users')
async def create_user(user: User, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user.password = hash_password(user.password)
    await conn["azul"]["user"].insert_one(dict(user))
    return await usersEntity(conn["azul"]["user"].find())

@user.put('/users/{id}')
async def update_user(id, user: User, token: str = Depends(oauth2_scheme)):

    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    # Hash the password if provided
    if user.password:
        user.password = hash_password(user.password)
    await conn["azul"]["user"].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)}
    )
    updated_user = await conn["azul"]["user"].find_one({"_id": ObjectId(id)})
    return await userEntity(updated_user)

@user.delete('/users/{id}')
async def delete_user(id, token: str = Depends(oauth2_scheme)):
    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    deleted_user = await conn["azul"]["user"].find_one_and_delete({"_id": ObjectId(id)})
    if deleted_user:
        return await userEntity(deleted_user)
    return None



@user.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await login_user_service(form_data)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": user, "token_type": "bearer"}

# devices crud
 
# return all devices
@devices.get('/devices', tags=["devices"])
async def find_all_devices(token: str = Depends(oauth2_scheme)):
    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    return await devicesEntity(conn["azul"]["devices"].find())


# return a specific device
@devices.get('/devices/{device_id}', tags=["devices"])
async def find_one_device(device_id, token: str = Depends(oauth2_scheme)):
    # Verify token and authenticate user
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    device = await conn["azul"]["devices"].find_one({"_id": ObjectId(device_id)})
    if device:
        return await deviceEntity(device)
    return None


# create a device
@devices.post('/devices/create', tags=["devices"])
async def create_device(device: Device, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = await conn["azul"]["devices"].insert_one(dict(device))
    created_device = await conn["azul"]["devices"].find_one({"_id": result.inserted_id})
    if created_device:
        return await deviceEntity(created_device)
    return None
    



# update an existing device
@devices.put('/devices/{device_id}', tags=["devices"])
async def update_device(device_id, device: Device, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    await conn["azul"]["devices"].find_one_and_update(
        {"_id":ObjectId(device_id)}, 
        {"$set": dict(device)}
    )
    updated_device = await conn["azul"]["devices"].find_one({"_id": ObjectId(device_id)})
    return await deviceEntity(updated_device)

# delete a device
@devices.delete('/devices/{device_id}', tags=["devices"])
async def delete_device(device_id, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    deleted_device = await conn["azul"]["devices"].find_one_and_delete({"_id":ObjectId(device_id)})
    if deleted_device:
        return await deviceEntity(deleted_device)
    return None

# companies crud

# return all companies
@companies.get('/companies')
async def find_all_companies(token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return await companiesEntity(conn["azul"]["companies"].find())

# return specific comapny
@companies.get('/companies/{company_id}')
async def find_one_company(company_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    company = await conn["azul"]["companies"].find_one({"_id": ObjectId(company_id)})
    if company:
        return await companyEntity(company)
    return None

# create a company
@companies.post('/companies')
async def create_company(company: Company, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = await conn["azul"]["companies"].insert_one(dict(company))
    created_company = await conn["azul"]["companies"].find_one({"_id": result.inserted_id})
    if created_company:
        return await companyEntity(created_company)
    return None


# updqte an existing company
@companies.put('/companies/{company_id}')
async def update_company(company_id: str, company: Company, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    await conn["azul"]["companies"].find_one_and_update(
        {"_id": ObjectId(company_id)},
        {"$set": dict(company)}
    )
    updated_company = await conn["azul"]["companies"].find_one({"_id": ObjectId(company_id)})
    return await companyEntity(updated_company)

# delete a company
@companies.delete('/companies/{company_id}')
async def delete_company(company_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    
    deleted_company = await conn["azul"]["companies"].find_one_and_delete({"_id": ObjectId(company_id)})
    return await companyEntity(deleted_company)

# campaigns crud

# return all campaigns
@campaigns.get('/campaigns')
async def find_all_campaigns(token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return await campaignsEntity(conn["azul"]["campaigns"].find())

# return one campaign
@campaigns.get('/campaigns/{camp_id}')
async def find_one_campaign(camp_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    campaign = await conn["azul"]["campaigns"].find_one({"_id": ObjectId(camp_id)})
    if campaign:
        return await campaignEntity(campaign)
    return None

# create a campaign
@campaigns.post('/campaigns')
async def create_campaign(campaign: Campaign, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = await conn["azul"]["campaigns"].insert_one(dict(campaign))
    created_campaign = await conn["azul"]["campaigns"].find_one({"_id": result.inserted_id})
    if created_campaign:
        return await campaignEntity(created_campaign)
    return None
    
# update an existing campaign
@campaigns.put('/campaigns/{camp_id}')
async def update_campaign(camp_id: str, campaign: Campaign, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    await conn["azul"]["campaigns"].find_one_and_update(
        {"_id": ObjectId(camp_id)},
        {"$set": dict(campaign)}
    )
    updated_campaign = await conn["azul"]["campaigns"].find_one({"_id": ObjectId(camp_id)})
    return await campaignEntity(updated_campaign)

# delete a campaign
@campaigns.delete('/campaigns/{camp_id}')
async def delete_campaign(camp_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    deleted_campaign = await conn["azul"]["campaigns"].find_one_and_delete({"_id": ObjectId(camp_id)})
    return await campaignEntity(deleted_campaign)

#impressions crud

# return all impressions
@impressions.get('/impressions')
async def find_all_impressions(token: str = Depends(oauth2_scheme)):     
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    return await impressionsEntity(conn["azul"]["impressions"].find())

# return a specific impression
@impressions.get('/impressions/{imp_id}')
async def find_one_impression(imp_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    impression = await conn["azul"]["impressions"].find_one({"_id": ObjectId(imp_id)})
    if impression:
        return await impressionEntity(impression)
    return None

# create an impression
@impressions.post('/impressions')
async def create_impression(impression: Impression, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = await conn["azul"]["impressions"].insert_one(dict(impression))
    created_impression = await conn["azul"]["impressions"].find_one({"_id": result.inserted_id})
    if created_impression:
        return await impressionEntity(created_impression)
    return None

# update an existing impression
@impressions.put('/impressions/{imp_id}')
async def update_impression(imp_id: str, impression: Impression, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    await conn["azul"]["impressions"].find_one_and_update(
        {"_id": ObjectId(imp_id)},
        {"$set": dict(impression)}
    )
    updated_impression = await conn["azul"]["impressions"].find_one({"_id": ObjectId(imp_id)})
    return await impressionEntity(updated_impression)

# delete an impression
@impressions.delete('/impressions/{imp_id}')
async def delete_impression(imp_id: str, token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    deleted_impression = await conn["azul"]["impressions"].find_one_and_delete({"_id": ObjectId(imp_id)})
    return await impressionEntity(deleted_impression)









