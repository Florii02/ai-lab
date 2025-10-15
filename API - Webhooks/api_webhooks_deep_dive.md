# APIs & Webhooks: Deep Dive Documentation

## Table of Contents
1. [Understanding APIs](#understanding-apis)
2. [REST API Fundamentals](#rest-api-fundamentals)
3. [HTTP Methods Deep Dive](#http-methods-deep-dive)
4. [Authentication & Security](#authentication--security)
5. [Webhooks Explained](#webhooks-explained)
6. [API vs Webhook: When to Use What](#api-vs-webhook-when-to-use-what)
7. [Real-World Integration Patterns](#real-world-integration-patterns)
8. [Error Handling & Best Practices](#error-handling--best-practices)
9. [EU/GDPR Considerations](#eugdpr-considerations)

---

## Understanding APIs

### What is an API?
An **Application Programming Interface (API)** is a contract between two software systems that defines how they communicate. Think of it as a waiter in a restaurant:
- You (client) ask the waiter for food
- The waiter takes your order to the kitchen (server)
- The kitchen prepares the food and returns it via the waiter
- You receive your meal (response)

### Types of APIs
1. **REST APIs** (this guide's focus) - Uses HTTP protocols
2. **GraphQL** - Query language for APIs
3. **SOAP** - XML-based protocol (legacy)
4. **gRPC** - High-performance RPC framework

### Why REST?
- **Simple**: Uses standard HTTP methods
- **Stateless**: Each request is independent
- **Cacheable**: Responses can be cached
- **Universal**: Works across all platforms

---

## REST API Fundamentals

### The Request-Response Cycle

```
CLIENT                          SERVER
   |                               |
   |  1. HTTP Request              |
   |  (Method, URL, Headers, Body) |
   |------------------------------>|
   |                               |
   |                          2. Process
   |                               |
   |  3. HTTP Response             |
   |  (Status, Headers, Body)      |
   |<------------------------------|
   |                               |
```

### Anatomy of an HTTP Request

```http
POST /api/v1/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

**Components:**
1. **Method**: `POST` (what action to perform)
2. **Path**: `/api/v1/users` (what resource)
3. **Headers**: Metadata about the request
4. **Body**: Data being sent (for POST/PUT/PATCH)

### Anatomy of an HTTP Response

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/users/42

{
  "id": 42,
  "name": "Alice",
  "email": "alice@example.com",
  "created_at": "2025-09-30T12:00:00Z"
}
```

**Components:**
1. **Status Code**: `201` (outcome of request)
2. **Headers**: Metadata about the response
3. **Body**: Data being returned

---

## HTTP Methods Deep Dive

### GET - Retrieve Data
**Purpose**: Fetch resource(s) without changing server state

```python
import requests

# Fetch single resource
response = requests.get("https://api.example.com/users/42")
user = response.json()

# Fetch collection with filters
response = requests.get(
    "https://api.example.com/users",
    params={"role": "admin", "active": True}
)
# URL becomes: https://api.example.com/users?role=admin&active=true
```

**Characteristics:**
- Idempotent (same request = same result)
- Can be cached
- Parameters in URL query string
- Should never modify data

---

### POST - Create New Resource
**Purpose**: Submit new data to the server

```python
import requests

response = requests.post(
    "https://api.example.com/users",
    json={
        "name": "Bob",
        "email": "bob@example.com",
        "role": "user"
    },
    headers={"Content-Type": "application/json"}
)

if response.status_code == 201:
    new_user = response.json()
    print(f"Created user ID: {new_user['id']}")
```

**Characteristics:**
- NOT idempotent (multiple calls = multiple resources)
- Returns `201 Created` on success
- Usually returns the created resource
- Body contains the data

---

### PUT - Replace Entire Resource
**Purpose**: Update by replacing the complete resource

```python
# PUT replaces the ENTIRE resource
response = requests.put(
    "https://api.example.com/users/42",
    json={
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "role": "admin"
    }
)
```

**Characteristics:**
- Idempotent (same request = same result)
- Must send complete resource
- Creates resource if doesn't exist (sometimes)

---

### PATCH - Partial Update
**Purpose**: Update only specific fields

```python
# PATCH updates only specified fields
response = requests.patch(
    "https://api.example.com/users/42",
    json={"role": "admin"}  # Only update role
)
```

**Characteristics:**
- Idempotent
- Only send fields to update
- More efficient than PUT

---

### DELETE - Remove Resource
**Purpose**: Delete a resource

```python
response = requests.delete("https://api.example.com/users/42")

if response.status_code == 204:
    print("User deleted successfully")
```

**Characteristics:**
- Idempotent
- Usually returns `204 No Content`
- May return `200 OK` with deletion details

---

## HTTP Status Codes

### Success (2xx)
- **200 OK**: Request succeeded
- **201 Created**: Resource created successfully
- **204 No Content**: Success, but no data to return

### Client Errors (4xx)
- **400 Bad Request**: Invalid request format
- **401 Unauthorized**: Missing or invalid authentication
- **403 Forbidden**: Authenticated but not allowed
- **404 Not Found**: Resource doesn't exist
- **429 Too Many Requests**: Rate limit exceeded

### Server Errors (5xx)
- **500 Internal Server Error**: Server crashed
- **502 Bad Gateway**: Upstream server issue
- **503 Service Unavailable**: Server temporarily down

---

## Authentication & Security

### 1. API Keys
**Simple but less secure**

```python
headers = {
    "X-API-Key": "sk_live_abc123xyz789"
}
response = requests.get("https://api.example.com/data", headers=headers)
```

**Pros**: Simple to implement
**Cons**: No expiration, hard to rotate

---

### 2. Bearer Tokens (Most Common)
**Used by OAuth 2.0, JWT**

```python
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
response = requests.get("https://api.example.com/data", headers=headers)
```

**Pros**: Can expire, can contain claims (JWT)
**Cons**: Must be stored securely

---

### 3. Basic Authentication
**Username + Password (Base64 encoded)**

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/data",
    auth=HTTPBasicAuth("username", "password")
)
```

**Pros**: Simple, standard
**Cons**: Credentials in every request (use HTTPS!)

---

### 4. OAuth 2.0 Flow
**Industry standard for delegated access**

```python
# Step 1: Get authorization code (user logs in via browser)
auth_url = "https://provider.com/oauth/authorize"
params = {
    "client_id": "your_client_id",
    "redirect_uri": "https://yourapp.com/callback",
    "scope": "read write",
    "response_type": "code"
}

# Step 2: Exchange code for token
token_response = requests.post(
    "https://provider.com/oauth/token",
    data={
        "grant_type": "authorization_code",
        "code": "AUTH_CODE_FROM_STEP_1",
        "client_id": "your_client_id",
        "client_secret": "your_client_secret"
    }
)

access_token = token_response.json()["access_token"]

# Step 3: Use token
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get("https://api.example.com/data", headers=headers)
```

---

### Security Best Practices

```python
import os
from dotenv import load_dotenv

# ✅ DO: Store secrets in environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# ❌ DON'T: Hardcode secrets
API_KEY = "sk_live_abc123xyz789"  # NEVER DO THIS!

# ✅ DO: Use HTTPS
url = "https://api.example.com/data"

# ❌ DON'T: Use HTTP for sensitive data
url = "http://api.example.com/data"

# ✅ DO: Validate SSL certificates
response = requests.get(url, verify=True)

# ❌ DON'T: Disable SSL verification
response = requests.get(url, verify=False)
```

---

## Headers Deep Dive

### Common Request Headers

```python
headers = {
    # Authentication
    "Authorization": "Bearer token123",

    # Content type of body
    "Content-Type": "application/json",

    # Expected response format
    "Accept": "application/json",

    # User agent identification
    "User-Agent": "MyApp/1.0",

    # Rate limiting info
    "X-RateLimit-Remaining": "99",

    # Custom headers (usually prefixed with X-)
    "X-Request-ID": "uuid-1234-5678"
}
```

### Common Response Headers

```python
# Check response headers
response = requests.get(url)

print(response.headers["Content-Type"])  # application/json
print(response.headers["X-RateLimit-Limit"])  # 100
print(response.headers["X-RateLimit-Remaining"])  # 95
print(response.headers["X-RateLimit-Reset"])  # 1633024800
```

---

## Webhooks Explained

### What is a Webhook?
A webhook is a **"reverse API"** - instead of you requesting data, the server sends data to you when an event occurs.

**Traditional API (Pull):**
```
You: "Hey server, any new orders?"
Server: "No"
[5 minutes later]
You: "Hey server, any new orders?"
Server: "No"
[5 minutes later]
You: "Hey server, any new orders?"
Server: "Yes! Here's order #123"
```

**Webhook (Push):**
```
[You register your webhook URL once]
You: "Send new orders to https://myapp.com/webhook"
[Server sends data when event happens]
Server: "New order #123 just came in!" -> POST to your URL
```

---

### Webhook Architecture

```
EVENT SOURCE                     YOUR SERVER
(GitHub, Stripe, etc)            (Listening at /webhook)
     |                                |
     |  Event happens                 |
     |  (e.g., new order)             |
     |                                |
     |  HTTP POST                     |
     |  to https://yourapp.com/webhook|
     |------------------------------->|
     |                                |
     |                           Process event
     |                                |
     |  200 OK                        |
     |<-------------------------------|
```

---

### Webhook vs API

| Aspect | API (Pull) | Webhook (Push) |
|--------|-----------|----------------|
| **Initiative** | Client initiates | Server initiates |
| **Timing** | You decide when | Real-time |
| **Efficiency** | Wastes calls (polling) | Only when needed |
| **Setup** | Easy (just call) | Requires endpoint |
| **Use Case** | Get data on demand | React to events |

---

### Setting Up a Webhook Receiver

#### Option 1: Python Flask Server

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get data from webhook
    data = request.json

    print(f"Received webhook: {data}")

    # Process the data
    if data.get('event') == 'order.created':
        order_id = data['order']['id']
        print(f"New order: {order_id}")
        # TODO: Save to database, send email, etc.

    # IMPORTANT: Always return 200 OK quickly
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

**Testing locally with ngrok:**
```bash
# Terminal 1: Run Flask app
python webhook_receiver.py

# Terminal 2: Expose to internet
ngrok http 5000
# You get: https://abc123.ngrok.io
# Webhook URL: https://abc123.ngrok.io/webhook
```

---

#### Option 2: Make.com (No-Code)

**Advantages:**
- No server needed
- Visual workflow builder
- Built-in integrations (Sheets, Slack, etc.)

**Setup:**
1. Create scenario in Make.com
2. Add "Webhooks > Custom Webhook" module
3. Copy webhook URL (e.g., `https://hook.eu1.make.com/abc123`)
4. Configure actions (write to Sheets, send email, etc.)
5. Send POST requests to the URL

**Example: Send data to Make.com**
```python
import requests

webhook_url = "https://hook.eu1.make.com/your_webhook_id"

payload = {
    "event": "new_signup",
    "user": {
        "name": "Alice",
        "email": "alice@example.com"
    },
    "timestamp": "2025-09-30T12:00:00Z"
}

response = requests.post(webhook_url, json=payload)
print(f"Webhook delivered: {response.status_code}")
```

---

### Webhook Security

#### 1. Signature Verification
**Most services send a signature to prove authenticity**

```python
import hmac
import hashlib
from flask import Flask, request, abort

app = Flask(__name__)
WEBHOOK_SECRET = "your_secret_key"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get signature from headers
    signature = request.headers.get('X-Webhook-Signature')

    # Calculate expected signature
    body = request.get_data()
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    # Verify
    if not hmac.compare_digest(signature, expected):
        abort(401)  # Unauthorized

    # Process webhook
    data = request.json
    # ... handle data ...

    return {"status": "ok"}, 200
```

#### 2. IP Whitelisting
```python
ALLOWED_IPS = ["192.168.1.100", "10.0.0.50"]

@app.route('/webhook', methods=['POST'])
def webhook():
    client_ip = request.remote_addr
    if client_ip not in ALLOWED_IPS:
        abort(403)  # Forbidden
    # ... process webhook ...
```

#### 3. HTTPS Only
Always use HTTPS for webhook URLs to prevent man-in-the-middle attacks.

---

## Real-World Integration Patterns

### Pattern 1: API → Process → Storage

```python
import requests
import pandas as pd
from datetime import datetime

def fetch_and_store_weather():
    # 1. Fetch from API
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 52.52,
            "longitude": 13.41,
            "current_weather": True
        }
    )

    # 2. Process data
    weather = response.json()["current_weather"]
    processed = {
        "timestamp": datetime.now().isoformat(),
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "location": "Berlin"
    }

    # 3. Store in CSV
    df = pd.DataFrame([processed])
    df.to_csv("weather_log.csv", mode='a', header=False, index=False)

    print(f"✅ Logged: {processed['temperature']}°C at {processed['timestamp']}")

# Run every hour
import schedule
schedule.every().hour.do(fetch_and_store_weather)
```

---

### Pattern 2: Webhook → Process → API

```python
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_order():
    # 1. Receive webhook from e-commerce platform
    order = request.json

    # 2. Process data
    total = sum(item['price'] * item['quantity'] for item in order['items'])

    # 3. Send to accounting API
    response = requests.post(
        "https://accounting.example.com/api/invoices",
        json={
            "order_id": order['id'],
            "customer": order['customer']['email'],
            "total": total,
            "currency": "EUR"
        },
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )

    if response.status_code == 201:
        print(f"✅ Invoice created for order {order['id']}")

    return {"status": "processed"}, 200
```

---

### Pattern 3: Scheduled API → Webhook

```python
import requests
import schedule
import time

def check_and_notify():
    # 1. Poll API for changes
    response = requests.get(
        "https://api.example.com/status",
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )

    status = response.json()

    # 2. If condition met, trigger webhook
    if status['cpu_usage'] > 80:
        requests.post(
            "https://hook.eu1.make.com/YOUR_WEBHOOK",
            json={
                "alert": "high_cpu",
                "value": status['cpu_usage'],
                "server": status['server_id']
            }
        )
        print(f"⚠️ Alert sent: CPU at {status['cpu_usage']}%")

# Run every 5 minutes
schedule.every(5).minutes.do(check_and_notify)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## Error Handling & Best Practices

### Robust API Call Pattern

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time

def make_api_call_with_retry(url, max_retries=3):
    # Configure retry strategy
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=1,  # Wait 1, 2, 4 seconds between retries
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for 4xx/5xx
        return response.json()

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code}")
        print(f"Response: {e.response.text}")
        return None

    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not reach server")
        return None

    except requests.exceptions.Timeout:
        print("❌ Timeout: Server took too long to respond")
        return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

# Usage
data = make_api_call_with_retry("https://api.example.com/data")
if data:
    print(f"✅ Success: {data}")
```

---

### Rate Limiting Handling

```python
import time
import requests

def api_call_with_rate_limit(url, headers):
    response = requests.get(url, headers=headers)

    # Check rate limit headers
    limit = int(response.headers.get('X-RateLimit-Limit', 100))
    remaining = int(response.headers.get('X-RateLimit-Remaining', 100))
    reset_time = int(response.headers.get('X-RateLimit-Reset', 0))

    print(f"Rate limit: {remaining}/{limit} remaining")

    # If rate limited
    if response.status_code == 429:
        wait_time = reset_time - time.time()
        print(f"⏳ Rate limited. Waiting {wait_time:.0f} seconds...")
        time.sleep(wait_time + 1)
        return api_call_with_rate_limit(url, headers)  # Retry

    return response.json()
```

---

### Webhook Retry Logic

```python
from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

def send_to_processing_queue(data):
    """Send to message queue for async processing"""
    # This ensures webhook responds quickly (< 5 seconds)
    # Actual processing happens asynchronously
    pass

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json

        # Validate payload
        if not data.get('event'):
            return {"error": "Missing event field"}, 400

        # Quick processing only
        send_to_processing_queue(data)

        # ALWAYS respond quickly (< 5 seconds)
        # Most webhook senders will retry if no response
        return {"status": "received", "timestamp": datetime.utcnow().isoformat()}, 200

    except Exception as e:
        print(f"❌ Webhook error: {e}")
        # Return 200 anyway to prevent retries for bad data
        return {"status": "error", "message": str(e)}, 200
```

---

## EU/GDPR Considerations

### 1. Data Residency
```python
# ✅ Use EU-based APIs when possible
EU_WEATHER_API = "https://api.open-meteo.com"  # EU servers

# ⚠️ Check data location for US services
# - Where is data stored?
# - Is there a Standard Contractual Clause (SCC)?
```

### 2. Personal Data in APIs
```python
import requests

# ❌ DON'T: Send personal data in URL (logged in server logs)
url = "https://api.example.com/users?email=alice@example.com"

# ✅ DO: Send personal data in request body (encrypted via HTTPS)
response = requests.post(
    "https://api.example.com/users/search",
    json={"email": "alice@example.com"}
)
```

### 3. API Keys vs User Data
```python
# API keys are NOT personal data (they identify the app, not user)
# User tokens ARE personal data (they identify the user)

# ✅ OK to log API keys (but keep secret)
print(f"Using API key: {API_KEY}")

# ❌ DON'T log user tokens
print(f"User token: {user_token}")  # GDPR violation if stored
```

### 4. Webhook Data Retention
```python
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Process immediately
    process_order(data)

    # ❌ DON'T: Store raw webhook data indefinitely
    # save_to_database(data)  # May contain personal data

    # ✅ DO: Only store what's needed, with retention policy
    save_order_summary({
        "order_id": data['id'],
        "total": data['total'],
        # Omit customer details if not needed
    })

    return {"status": "ok"}, 200
```

### 5. Third-Party Services Checklist
When using services like Make.com, Zapier:
- ✅ Check if they have EU servers
- ✅ Review their Data Processing Agreement (DPA)
- ✅ Ensure they're GDPR-compliant
- ✅ Minimize personal data sent through automation

---

## Practical Exercise: Complete Workflow

### Goal: Monitor website uptime → Alert via webhook

```python
# uptime_monitor.py
import requests
import schedule
import time
from datetime import datetime

WEBSITES = [
    "https://example.com",
    "https://myapp.com"
]

WEBHOOK_URL = "https://hook.eu1.make.com/YOUR_WEBHOOK"

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status = "UP" if response.status_code == 200 else "DOWN"
        return {
            "url": url,
            "status": status,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "timestamp": datetime.utcnow().isoformat()
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status": "DOWN",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

def monitor_and_alert():
    for website in WEBSITES:
        result = check_website(website)

        print(f"{result['timestamp']} | {result['url']} | {result['status']}")

        # Alert if down
        if result['status'] == "DOWN":
            requests.post(WEBHOOK_URL, json={
                "alert_type": "website_down",
                "website": result['url'],
                "error": result.get('error', 'Unknown'),
                "timestamp": result['timestamp']
            })
            print(f"🚨 Alert sent for {result['url']}")

# Run every 5 minutes
schedule.every(5).minutes.do(monitor_and_alert)

print("🔍 Uptime monitor started...")
while True:
    schedule.run_pending()
    time.sleep(1)
```

**Make.com Scenario:**
1. Webhook receives alert
2. Filter: Only if `alert_type == "website_down"`
3. Google Sheets: Log incident
4. Slack/Email: Send notification
5. (Optional) HTTP request: Trigger incident in PagerDuty

---

## Debugging Tips

### 1. Inspect API Requests
```python
import requests
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

response = requests.get("https://api.example.com/data")
```

### 2. Use Request Inspector Services
- **RequestBin**: https://requestbin.com (inspect webhooks)
- **Webhook.site**: https://webhook.site (test webhook payloads)
- **Postman**: Desktop app for API testing

### 3. Pretty Print JSON Responses
```python
import json

response = requests.get("https://api.example.com/data")
print(json.dumps(response.json(), indent=2))
```

### 4. Test Webhooks Locally
```bash
# Use ngrok to expose local server
ngrok http 5000

# Or use Make.com webhook (no local server needed)
```

---

## Resources & Further Reading

### APIs
- **REST API Tutorial**: https://restfulapi.net
- **HTTP Status Codes**: https://httpstatuses.com
- **Public APIs for Testing**: https://jsonplaceholder.typicode.com

### Webhooks
- **Webhook Guide**: https://webhooks.fyi
- **Make.com Docs**: https://www.make.com/en/help/webhooks

### Python Libraries
- **requests**: https://requests.readthedocs.io
- **Flask**: https://flask.palletsprojects.com (webhook receivers)
- **httpx**: https://www.python-httpx.org (async alternative)

### EU/GDPR
- **EU GDPR Portal**: https://gdpr.eu
- **Standard Contractual Clauses**: https://commission.europa.eu/scc

---

## Quick Reference

### Common requests Patterns
```python
import requests

# GET with query params
requests.get(url, params={"key": "value"})

# POST with JSON
requests.post(url, json={"key": "value"})

# With headers
requests.get(url, headers={"Authorization": "Bearer token"})

# With timeout
requests.get(url, timeout=10)

# With custom user agent
requests.get(url, headers={"User-Agent": "MyApp/1.0"})

# Download file
response = requests.get(url, stream=True)
with open("file.zip", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

### HTTP Status Codes Cheatsheet
- **2xx**: Success ✅
- **3xx**: Redirect ↪️
- **4xx**: Client error (your fault) ❌
- **5xx**: Server error (their fault) 💥

### Webhook Security Checklist
- [ ] Verify signature/HMAC
- [ ] Use HTTPS only
- [ ] Validate payload structure
- [ ] Respond quickly (< 5 seconds)
- [ ] Implement retry logic
- [ ] Log all webhook events
- [ ] Rate limit incoming requests

---

**Last Updated**: 2025-09-30
**Author**: AI Lab Notes
**Version**: 1.0