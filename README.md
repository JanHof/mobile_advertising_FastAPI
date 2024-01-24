# mobile_advertising_FastAPI
CRUD Queries for mobile advertising app in FastAPI
Overview
This project is a FastAPI-based web application that serves as an API for managing user information, devices, companies, campaigns, and impressions. It includes functionality for CRUD (Create, Read, Update, Delete) operations on these entities.

Project Structure:
1. models.py
This module contains the Pydantic models representing the data structures used in the application. These models define the structure of user, device, company, campaign, and impression entities.

2. routes.py
The routes.py file defines the FastAPI routers for different entities. Each router includes endpoints for handling various HTTP operations (GET, POST, PUT, DELETE) related to the corresponding entity.

3. schemas.py
The schemas.py file consists of asynchronous functions that convert MongoDB documents to formatted API response entities. These functions are used to shape the data before sending it as a response.

4. index.py
The main entry point of the application is the index.py file. It creates the FastAPI app, includes the defined routers from routes.py, and configures any necessary settings.


<h4>API Endpoints</h4>
The following API endpoints are available:

Users:

GET /users: Retrieve all users. <br>
GET /users/{id}: Retrieve a specific user by ID. <br>
POST /users: Create a new user. <br>
PUT /users/{id}: Update a user by ID. <br>
DELETE /users/{id}: Delete a user by ID. <br>

Devices:

GET /devices: Retrieve all devices.<br>
GET /devices/{device_id}: Retrieve a specific device by ID.<br>
POST /devices/create: Create a new device.<br>
PUT /devices/{device_id}: Update a device by ID.<br>
DELETE /devices/{device_id}: Delete a device by ID.<br>

Companies:

GET /companies: Retrieve all companies.<br>
GET /companies/{comp_id}: Retrieve a specific company by ID.<br>
POST /companies: Create a new company.<br>
PUT /companies/{comp_id}: Update a company by ID.<br>
DELETE /companies/{comp_id}: Delete a company by ID.<br>

Campaigns:

GET /campaigns: Retrieve all campaigns.<br>
GET /campaigns/{camp_id}: Retrieve a specific campaign by ID.<br>
POST /campaigns: Create a new campaign.<br>
PUT /campaigns/{camp_id}: Update a campaign by ID.<br>
DELETE /campaigns/{camp_id}: Delete a campaign by ID.<br>

Impressions:

GET /impressions: Retrieve all impressions.<br>
GET /impressions/{imp_id}: Retrieve a specific impression by ID.<br>
POST /impressions: Create a new impression.<br>
PUT /impressions/{imp_id}: Update an impression by ID.<br>
DELETE /impressions/{imp_id}: Delete an impression by ID.<br>

Technologies Used:

FastAPI<br>
MongoDB<br>
Motor (Async MongoDB Driver)<br>
Pydantic<br>

Contributors:

Jan Hendrik Hofmeyr

