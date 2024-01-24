# mobile_advertising_FastAPI
CRUD Queries for mobile advertising app in FastAPI
Overview
This project is a FastAPI-based web application that serves as an API for managing user information, devices, companies, campaigns, and impressions. It includes functionality for CRUD (Create, Read, Update, Delete) operations on these entities.

Project Structure
1. models.py
This module contains the Pydantic models representing the data structures used in the application. These models define the structure of user, device, company, campaign, and impression entities.

2. routes.py
The routes.py file defines the FastAPI routers for different entities. Each router includes endpoints for handling various HTTP operations (GET, POST, PUT, DELETE) related to the corresponding entity.

3. schemas.py
The schemas.py file consists of asynchronous functions that convert MongoDB documents to formatted API response entities. These functions are used to shape the data before sending it as a response.

4. index.py
The main entry point of the application is the index.py file. It creates the FastAPI app, includes the defined routers from routes.py, and configures any necessary settings.


<h4>API Endpoints</h4>
<l>The following API endpoints are available:</l>

Users:

GET /users: Retrieve all users.
GET /users/{id}: Retrieve a specific user by ID.
POST /users: Create a new user.
PUT /users/{id}: Update a user by ID.
DELETE /users/{id}: Delete a user by ID.
Devices:

GET /devices: Retrieve all devices.
GET /devices/{device_id}: Retrieve a specific device by ID.
POST /devices/create: Create a new device.
PUT /devices/{device_id}: Update a device by ID.
DELETE /devices/{device_id}: Delete a device by ID.
Companies:

GET /companies: Retrieve all companies.
GET /companies/{comp_id}: Retrieve a specific company by ID.
POST /companies: Create a new company.
PUT /companies/{comp_id}: Update a company by ID.
DELETE /companies/{comp_id}: Delete a company by ID.
Campaigns:

GET /campaigns: Retrieve all campaigns.
GET /campaigns/{camp_id}: Retrieve a specific campaign by ID.
POST /campaigns: Create a new campaign.
PUT /campaigns/{camp_id}: Update a campaign by ID.
DELETE /campaigns/{camp_id}: Delete a campaign by ID.
Impressions:

GET /impressions: Retrieve all impressions.
GET /impressions/{imp_id}: Retrieve a specific impression by ID.
POST /impressions: Create a new impression.
PUT /impressions/{imp_id}: Update an impression by ID.
DELETE /impressions/{imp_id}: Delete an impression by ID.
Technologies Used
FastAPI
MongoDB
Motor (Async MongoDB Driver)
Pydantic

Contributors
Jan Hendrik Hofmeyr

