# Infor WMS API Notes

## Overview
Bloem uses Infor WMS to manage its warehouse operations. Our application will connect to Infor WMS through the Infor ION API Gateway to retrieve shipment and load information.

For now, we're focusing on read-only API requests.

## How the Connection Works
1. Our FastAPI backend sends client credentials to Infor SSO.
2. Infor SSO returns an access token.
3. The backend sends requests to the ION API Gateway using the token and a required Username header.
4. The gateway forwards the request to Infor WMS.
5. WMS returns the requested data in JSON format.

## Main API Endpoints

### Shipment List
POST bodlist/showshipmentorderlist

Retrieves outbound orders along with shipment information, including dates, carriers, load IDs, and order lines.

### Shipment Details
GET shipments/{orderkey}

Retrieves detailed information about a specific outbound order.

### Load Details
GET loads/loadhdr/{loadid}

Retrieves load information such as carrier, shipment status, weight, and shipping dates.

### External Order Lookup
GET shipments/externalorderkey/{externalorderkey}

Allows us to look up an order using its external order number.

These endpoints were tested by Bloem in its training environment.

## Authentication Requirements
To connect to Infor WMS, we'll need:
- OAuth client ID and client secret
- Dedicated WMS service account username
- Access token from Infor SSO
- Correct tenant and warehouse path

Credentials will need to be provided securely by Bloem IT.

## Important Notes
- Infor uses "shipment" to refer to an outbound order. Truckloads are called "loads."
- Shipment lists use serialkey-based pagination.
- Access tokens should be reused until shortly before expiration.
- Some API responses may take several seconds.
- A 404 response containing "No records found" can mean there are no matching records.
- We should test in Bloem's training environment before attempting production integration.

## Warehouse Options
Bloem has five warehouse environments listed in the API documentation:

- WM01 - Apopka
- WM04 - CustomPak
- WM07 - Iceberg
- WM08 - Kentcity
- WM09 - Hol Special Delivery

The training environment (TRN) paths are already provided in Marcus's PDF. We just need Bloem to confirm which warehouse we should use for initial testing.

## Shipment Filtering Limitations
The shipment list endpoint (`bodlist/showshipmentorderlist`) does not support filtering by date, status, or carrier.

Because of this, we'll need to handle filtering through our own backend or database instead of relying on Infor WMS to filter the results.

The endpoint also uses serialkey-based pagination, so we'll need to keep track of the last serialkey when retrieving additional records.

## Existing Order Updates
One thing that still needs clarification is how we'll detect changes to existing shipment orders.

The API documentation explains how to retrieve newer orders using serialkey pagination, but it hasn't been confirmed whether this also captures updates to existing orders.

We'll need to follow up with Bloem about this before deciding how to keep shipment information updated.

## Questions for Bloem
1. Can we get the OAuth credentials and service account for the training environment?
2. Which warehouse should we use for initial testing?
3. Can Bloem provide sample shipment data and status code definitions?
4. How should we detect updates to existing orders?
5. How often should shipment information be refreshed?

## Next Steps
- Agree on the shipment data format with CK and Emmit.
- Develop initial FastAPI shipment endpoints.
- Prepare the Infor API connection and authentication.
- Test the connection once Bloem provides credentials.
