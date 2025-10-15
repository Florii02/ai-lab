# Day 5: FastAPI + Docker Deployment - Deep Dive

## Learning Objectives

This guide will teach you:
1. **FastAPI** - Modern Python web framework
2. **Docker** - Containerization technology
3. **Deployment** - Getting your app on the internet
4. **DevOps basics** - Professional deployment practices

---

## Part 1: Understanding FastAPI (`app.py`)

### What is FastAPI?

FastAPI is a modern, high-performance Python web framework for building APIs. Think of it as a way to create web services that other programs (or frontends) can talk to.

### Code Breakdown: `app.py`

```python
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="EU AI App", version="1.0.0")
```

**What's happening:**
- `FastAPI()` creates your web application instance
- `title` and `version` are metadata (shows up in auto-generated docs)
- `app` is the main object that handles all incoming web requests

---

### Endpoint 1: Root Route

```python
@app.get("/")
def read_root():
    return {
        "message": "Hello from EU AI App",
        "timestamp": datetime.now().isoformat(),
        "region": "EU-hosted"
    }
```

**Concepts:**

1. **`@app.get("/")`** - This is a **decorator**
   - It tells FastAPI: "When someone visits the root URL (`/`), run this function"
   - `get` means HTTP GET request (the most common type - used when you load a webpage)

2. **Function returns a dictionary**
   - FastAPI automatically converts Python dicts to JSON (the standard format for web APIs)
   - JSON is like Python dict but text-based, so it can travel over the internet

3. **What you get when you visit `http://your-server/`:**
   ```json
   {
     "message": "Hello from EU AI App",
     "timestamp": "2025-09-30T14:32:10.123456",
     "region": "EU-hosted"
   }
   ```

---

### Endpoint 2: Health Check

```python
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FastAPI"}
```

**Why this matters:**
- Production apps need health checks
- Monitoring tools ping `/health` to ensure your service is alive
- Load balancers use this to know if they should route traffic to your server

**Real-world analogy:** Like checking if a store is open before sending customers there.

---

### Endpoint 3: Dynamic Route with Parameters

```python
@app.get("/api/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}! Welcome to the EU AI platform."}
```

**Key concepts:**

1. **Path parameter:** `{name}` in the URL becomes a variable
   - Visit: `http://your-server/api/greet/Alice`
   - The function receives: `name = "Alice"`

2. **Type hints:** `name: str`
   - Tells FastAPI to expect a string
   - FastAPI automatically validates this (rejects invalid data)

3. **Why this pattern is powerful:**
   - One function handles infinite variations
   - `/api/greet/Alice`, `/api/greet/Bob`, `/api/greet/Neo` all work

---

## Part 2: Understanding Docker (`Dockerfile`)

### What Problem Does Docker Solve?

**The "Works on My Machine" Problem:**
- Your code works on your laptop (Python 3.11, specific libraries installed)
- Your friend tries to run it: doesn't work (different Python version, missing libraries)
- Your production server: also different environment

**Docker's Solution:**
Package your app + its entire environment into a **container** - a standardized, portable box that runs identically everywhere.

---

### Dockerfile Line-by-Line

```dockerfile
FROM python:3.11-slim
```

**What it means:**
- Start with an official Python 3.11 image (pre-built by Docker community)
- `slim` = smaller version (includes only essentials)
- This is your **base layer** - like the foundation of a house

---

```dockerfile
WORKDIR /app
```

**Sets the working directory inside the container:**
- All subsequent commands happen in `/app`
- Like doing `cd /app` before running commands

---

```dockerfile
COPY requirements.txt .
```

**Copy the requirements file from your computer into the container:**
- `.` means "current directory" (which is `/app` because of WORKDIR)
- **Why copy requirements first?** Docker caching optimization (explained below)

---

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

**Install Python dependencies:**
- `RUN` executes a command during image build
- `--no-cache-dir` saves space (doesn't store downloaded packages)
- This creates a layer with all your dependencies installed

**Docker Layer Caching:**
- If `requirements.txt` doesn't change, Docker reuses this layer
- Makes rebuilds MUCH faster
- That's why we copy requirements before code (code changes more often)

---

```dockerfile
COPY app.py .
```

**Copy your application code:**
- Done after installing dependencies (cache optimization)
- Now your app exists inside the container

---

```dockerfile
EXPOSE 8000
```

**Document that the app uses port 8000:**
- This is **documentation only** (doesn't actually open the port)
- The `-p 8000:8000` flag when running the container actually maps the port

---

```dockerfile
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**The command to run when container starts:**

- `uvicorn` = ASGI server (runs FastAPI apps)
- `app:app` = "in file `app.py`, use the `app` object"
- `--host 0.0.0.0` = listen on all network interfaces (allows external access)
- `--port 8000` = listen on port 8000

**Without `0.0.0.0`:**
- App would only be accessible inside the container (useless!)
- `0.0.0.0` makes it accessible from outside

---

## Part 3: Docker Compose (`docker-compose.yml`)

### What is Docker Compose?

Docker Compose is a tool for defining and running multi-container applications using a YAML configuration file.

**Without Compose:**
```bash
docker build -t eu-ai-app .
docker run -d -p 8000:8000 --name fastapi-app \
  -e ENV=production --restart unless-stopped eu-ai-app
```

**With Compose:**
```bash
docker-compose up -d
```

Much simpler! Compose remembers all the settings.

---

### docker-compose.yml Breakdown

```yaml
version: '3.8'
```
- Specifies the Compose file format version
- `3.8` is modern and widely supported

---

```yaml
services:
  fastapi-app:
```
- `services` = containers to run
- `fastapi-app` = name of this service (you choose this)

---

```yaml
    build: .
```
- Build the Docker image from the current directory (`.`)
- Looks for `Dockerfile` automatically

---

```yaml
    ports:
      - "8000:8000"
```
**Port mapping:**
- Format: `"HOST:CONTAINER"`
- Left side (8000) = port on your computer/server
- Right side (8000) = port inside the container
- This makes `localhost:8000` on your machine route to port 8000 in the container

**Example:** If you used `"3000:8000"`:
- Visit `localhost:3000` on your browser
- Goes to port 8000 inside the container

---

```yaml
    environment:
      - ENV=production
```
**Environment variables:**
- Sets `ENV` variable inside the container
- Your app can read this: `os.getenv("ENV")`
- Useful for config (development vs. production)

---

```yaml
    restart: unless-stopped
```
**Automatic restart policy:**
- If container crashes → automatically restart
- If you manually stop it → don't restart
- Essential for production (keeps your app running 24/7)

---

## Part 4: .dockerignore

```
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.git
.gitignore
*.md
```

**What it does:**
Like `.gitignore` but for Docker - tells Docker what NOT to copy into the image.

**Why it matters:**
- Keeps images small
- Faster builds
- No sensitive data accidentally copied
- No unnecessary files (compiled Python bytecode, virtual environments, docs)

---

## Part 5: Testing Script (`test_local.sh`)

```bash
#!/bin/bash
# Test FastAPI endpoints...

curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/api/greet/Alice
```

**What this does:**
- `curl` = command-line tool to make HTTP requests
- Tests all your endpoints automatically
- Should be run after starting the app locally

**How to use:**
```bash
chmod +x test_local.sh  # Make executable (one time)
./test_local.sh          # Run tests
```

---

## < Part 6: Deployment Concepts

### The Deployment Stack

```
Internet → VPS Firewall → Nginx (reverse proxy) → Docker Container → FastAPI
```

**Each layer explained:**

1. **VPS (Virtual Private Server):**
   - Your own virtual computer in a datacenter
   - Always online, connected to the internet
   - You have full control (like root access)

2. **Firewall (UFW):**
   - Blocks unwanted traffic
   - Only allows ports 22 (SSH), 80 (HTTP), 443 (HTTPS), 8000 (your app)

3. **Nginx (Reverse Proxy):**
   - Sits in front of your app
   - Handles HTTPS/SSL certificates
   - Can serve multiple apps on one server
   - Buffers requests (protects your app from slow clients)

4. **Docker Container:**
   - Isolated environment running your app
   - Can be easily replaced/updated without affecting the host

5. **FastAPI:**
   - Your actual application code

---

### Why Use Nginx Instead of Exposing FastAPI Directly?

**Without Nginx:**
```
User → FastAPI:8000
```

**Problems:**
- No HTTPS (data sent in plain text)
- FastAPI handles static files poorly
- Can't easily run multiple apps
- No caching
- Vulnerable to slow clients (Slowloris attacks)

**With Nginx:**
```
User → Nginx:443 (HTTPS) → FastAPI:8000
```

**Benefits:**
-  Free HTTPS with Let's Encrypt
-  Better performance (Nginx is optimized for this)
-  Can run multiple apps (different domains/paths → different backends)
-  Caching, rate limiting, load balancing
-  Professional-grade security

---

## Part 7: Hosting Options Comparison

### Hostinger VPS (Recommended for learning)

**Pros:**
- EU-based (GDPR compliant)
- Full control (root access)
- Affordable (€4-8/month)
- Learn real server management

**Cons:**
- You manage everything (updates, security, etc.)
- No automatic scaling

**When to choose:** You want to learn DevOps, need full control, EU data residency important.

---

### HuggingFace Spaces (Easiest)

**Pros:**
- Free tier
- Zero server management
- Git-push to deploy
- Built-in HTTPS

**Cons:**
- Limited resources (CPU-only on free tier)
- Public by default
- Less control

**When to choose:** Quick demos, proof of concepts, learning Docker basics.

---

### Hetzner (Best value for production)

**Pros:**
- German company (strong privacy)
- Best price/performance in EU
- Excellent network

**Cons:**
- Same as any VPS (you manage it)

**When to choose:** Production apps, need reliability + good price.

---

## Part 8: Security Best Practices (From the Scripts)

### 1. **Non-root User**
```bash
adduser deploy
usermod -aG sudo deploy
usermod -aG docker deploy
```

**Why:**
- Running as `root` is dangerous (one mistake = full system compromise)
- `deploy` user has limited permissions
- Can still use `sudo` when needed

---

### 2. **Firewall (UFW)**
```bash
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
sudo ufw enable
```

**Why:**
- Blocks all ports except those explicitly allowed
- Prevents hackers from accessing unused services

---

### 3. **HTTPS with Let's Encrypt**
```bash
sudo certbot --nginx -d yourdomain.com
```

**Why:**
- Encrypts traffic (passwords, API keys can't be intercepted)
- Modern browsers warn users about non-HTTPS sites
- Free with Let's Encrypt

---

### 4. **Docker Security**
- Running app as non-root user inside container
- `restart: unless-stopped` (not `always` - allows manual stops)
- `.dockerignore` prevents sensitive files from being copied

---

## =� Part 9: Common Commands Explained

### Docker Commands

```bash
# Build an image from Dockerfile
docker build -t eu-ai-app .
```
- `-t eu-ai-app` = tag (name) the image
- `.` = build context (current directory)

---

```bash
# Run a container
docker run -d -p 8000:8000 --name fastapi-app eu-ai-app
```
- `-d` = detached mode (runs in background)
- `-p 8000:8000` = port mapping (host:container)
- `--name fastapi-app` = name the container (easier to reference)
- `eu-ai-app` = image to use

---

```bash
# View running containers
docker ps
```

```bash
# View logs
docker logs fastapi-app
docker logs -f fastapi-app  # -f = follow (live logs)
```

```bash
# Stop and remove container
docker stop fastapi-app
docker rm fastapi-app
```

---

### Docker Compose Commands

```bash
# Start services (build if needed)
docker-compose up -d
```
- `-d` = detached (background)

---

```bash
# Stop services (containers still exist)
docker-compose stop

# Stop and remove containers
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

---

```bash
# View logs
docker-compose logs -f
```

---

## Part 10: The Complete Flow

### Local Development
1. Write code (`app.py`)
2. Test without Docker: `uvicorn app:app --reload`
3. Visit `http://localhost:8000/docs` (auto-generated API docs!)
4. Test with Docker: `docker-compose up`
5. Run tests: `./test_local.sh`

### Deployment
1. Get VPS (Hostinger/Hetzner)
2. SSH into server: `ssh root@YOUR_VPS_IP`
3. Install Docker
4. Upload code (Git or SCP)
5. Run: `docker-compose up -d`
6. Configure Nginx (reverse proxy)
7. Add HTTPS (Let's Encrypt)
8. Test from internet

---

## What You've Learned

### Core Technologies
- **FastAPI** - Modern Python web framework (faster than Flask)
- **Uvicorn** - ASGI server (runs FastAPI)
- **Docker** - Containerization (package app + dependencies)
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Reverse proxy (HTTPS, performance, security)

### DevOps Concepts
- **Deployment** - Getting code from laptop → internet
- **Containerization** - "Works on my machine" → "Works everywhere"
- **Reverse Proxy** - Nginx sits between users and your app
- **Port Mapping** - Connecting host ports to container ports
- **Health Checks** - Monitoring if your service is alive
- **Environment Variables** - Configuration without hardcoding

### Best Practices
- Layer caching in Docker (copy requirements before code)
- `.dockerignore` (keep images small)
- Non-root users (security)
- Firewall configuration (UFW)
- HTTPS with Let's Encrypt (encryption)
- Automatic restarts (`restart: unless-stopped`)

---

## Next Steps

1. **Run the script** - Create all files and test locally
2. **Experiment** - Add new endpoints to `app.py`
3. **Deploy** - Get a Hostinger VPS and deploy for real
4. **Monitor** - Add logging, set up uptime monitoring
5. **Scale** - Add database, authentication, multiple services

---

## Key Insights

### Why This Stack?

**Python + FastAPI:**
- Great for AI/ML (most ML libraries are Python)
- Fast performance (comparable to Node.js)
- Auto-generated API docs (saves time)

**Docker:**
- Consistent environments (dev, staging, production identical)
- Easy rollbacks (keep old images)
- Scalable (can run 1 or 1000 containers)

**VPS (vs. serverless):**
- Full control
- Learn real server management
- Fixed costs (no surprise bills)
- Good for always-on services

---

## FAQ

### Q: Why not just run Python directly on the server?
**A:** Docker gives you:
- Reproducible environments
- Easy updates (replace container)
- Isolation (your app can't break system packages)
- Portability (move to any cloud provider)

### Q: Why Nginx when FastAPI can serve HTTP directly?
**A:** Nginx is battle-tested for:
- HTTPS/SSL termination
- Static file serving
- Request buffering (protects against slow clients)
- Load balancing (if you scale to multiple containers)

### Q: What's the difference between `docker run` and `docker-compose`?
**A:**
- `docker run` - Manually specify all options each time
- `docker-compose` - Configuration file (infrastructure as code)
- Compose is better for anything beyond toy projects

### Q: Why `0.0.0.0` instead of `localhost`?
**A:** Inside Docker:
- `localhost` = only inside the container
- `0.0.0.0` = all network interfaces (allows external access)

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Docker Documentation](https://docs.docker.com)
- [Nginx Reverse Proxy Guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- [Let's Encrypt](https://letsencrypt.org)
- [Hostinger VPS](https://www.hostinger.com/vps-hosting)

---

**You now understand every part of this deployment stack!**

The beauty of this approach: each component (FastAPI, Docker, Nginx) is industry-standard and used by companies like Uber, Netflix, and Spotify.