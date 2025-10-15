## Day 6: Automation Platforms (Make.com, n8n)

### Platform Comparison Table

| Feature | Make (Integromat) | n8n | Zapier | Relay | Latenode |
|---------|-------------------|-----|--------|-------|----------|
| **Pricing Model** | Operations/month | Executions (cloud) / Free (self-host CE) | Tasks/month | Predictable pricing (vendor) | Credit-time based |
| **Free Tier** | 1k ops/mo | 2.5k executions (cloud) / Unlimited (self-host) | 100 tasks/mo | Custom | Custom |
| **Paid Start** | ~$9/mo (10k ops) | ~EUR9/mo (2.5k exec) | $19.99/mo (750 tasks) | Custom | Credit-based |
| **Self-Hosting** | No | Yes (Community Edition) | No | No | No |
| **EU Data Residency** | SaaS (check terms) | Frankfurt (cloud) / Your VPS (self-host) | SaaS (check terms) | US-based | Verify per vendor |
| **App Integrations** | 1,500+ | 400+ (growing) | 7,000+ | Moderate | AI-native focus |
| **Visual Builder** | Advanced (routers, filters) | Advanced (IF, Switch, loops) | Simple (paths, filters) | Collaboration-focused | AI-native |
| **Code/Custom Logic** | Limited | Full JS/Python nodes | Limited (Code by Zapier) | Limited | AI-integrated |
| **AI Features** | AI Assistant (marketing) | AI nodes + agents | AI builder, chatbots | Strong AI emphasis | Strong AI + headless browser |
| **Best For** | Visual logic, mid-scale value | EU self-host, dev control, complex flows | Easiest UX, largest catalog | Human-in-the-loop + AI collab | Predictable AI workflows |
| **Scaling Cost** | Operations multiply in loops | Predictable per-execution (cloud) / Infra only (self-host) | Expensive at scale | Vendor-stated predictable | Credit model |
| **Advanced Features** | Routers, iterators, error handlers | Queue/workers, Git version control, Split batches | Sub-Zaps, delay, looping | Human approvals, collaboration | Headless browser, managed AI |

### Pricing Model Deep-Dive

**Why pricing structure matters:**

- **Zapier (Tasks)**: Each action step = 1 task. A 5-step workflow consumes 5 tasks per run. Simple flows are affordable; complex multi-step automations become expensive fast.

- **Make (Operations)**: Each module execution = 1 operation. Loops and batch processing multiply operations. Example: Processing 100 items in a loop = 100+ operations. Often cheaper than Zapier at low-to-mid complexity.

- **n8n (Executions)**: 1 workflow run = 1 execution, regardless of steps inside. Unlimited steps per execution gives massive value. Self-hosted Community Edition = unlimited executions (you only pay infrastructure costs).

- **Relay/Latenode**: Vendor-specific models focused on AI and predictable billing; evaluate against your actual usage patterns.

**Cost Example** (processing 1,000 webhook events/month with 5-step workflow):
- Zapier: 5,000 tasks/month = ~$29-49/mo
- Make: 5,000 operations = ~$9/mo
- n8n Cloud: 1,000 executions = Free tier (2.5k)
- n8n Self-host: Unlimited = VPS cost only (~$5-10/mo)

---

## Part A: Make.com Quick Overview

### What is Make?
Visual automation platform (formerly Integromat) with powerful logic operators. Think Zapier with more control.

### Key Strengths
- Visual scenario builder with drag-and-drop modules
- Routers (branching), Filters (conditions), Iterators (loops)
- 1,500+ app integrations
- Template library for common workflows
- Better value than Zapier at comparable complexity

### Quick Start Flow

**Scenario: Gmail → Google Sheets → Slack**

1. **Trigger**: Gmail - Watch emails (filter: subject contains "Invoice")
2. **Action 1**: Google Sheets - Add a row (extract sender, subject, date)
3. **Action 2**: Slack - Send message to #finance channel

**Steps in Make:**
1. Create new scenario
2. Add Gmail module → Watch emails → Set filter
3. Add Google Sheets module → Add a row → Map fields (sender, subject, timestamp)
4. Add Slack module → Send channel message → Format message with data
5. Test → Activate

**Advanced: Add Router Logic**
- After Gmail trigger, add Router
- Path 1: If amount > $1000 → Alert manager on Slack
- Path 2: If amount < $1000 → Log to Sheets only

### Connecting to Your FastAPI

1. **HTTP Module** in Make
2. Method: POST
3. URL: `https://your-fastapi-domain.com/api/endpoint`
4. Headers: `Content-Type: application/json`
5. Body: Map Gmail data to JSON payload
6. Parse response → use in next module

**Example Body:**
```json
{
  "sender": "{{1.from}}",
  "subject": "{{1.subject}}",
  "amount": "{{parseNumber(1.text)}}"
}
```

### Practice Task: Make.com
Create this flow:
1. Webhook trigger (test with curl or Postman)
2. HTTP Request to your FastAPI `/api/greet/{name}`
3. Router:
   - If response status 200 → Google Sheets log
   - If error → Slack alert
4. Document the operations consumed

---

## Part B: n8n Deep Dive

### 1. What is n8n?

n8n ("nodemation") is an open-source automation and integration platform. Think Zapier/Make, but:

- **Self-hostable**: Deploy on your VPS (Hostinger/Hetzner/OVH)
- **EU-first/GDPR-friendly**: All data stays in infrastructure you control
- **Customizable**: Extend with JS code, custom nodes, AI integrations
- **Enterprise orchestration**: Loops, branching, queues, retriggers - features commercial SaaS restricts

**Key Advantages:**
- 400+ prebuilt integrations (APIs, SaaS, databases)
- Full REST API, webhook, and AI API support
- Internal datastore for persistent data without external DB
- Configurable flow controls (looping, conditional logic)
- Run on laptop (dev) or VPS (production 24/7)

---

### 2. Self-Hosting n8n (Docker on Hostinger VPS)

For control, compliance, and unlimited runs, self-hosting is the optimal choice.

#### Step 1: VPS Setup (Hostinger KVM)

1. **Buy VPS**: [Hostinger VPS Plans](https://www.hostinger.com/vps-hosting)
   - KVM 1: 1 vCPU, 4GB RAM, 50GB NVMe SSD (~EUR5/mo)
   - Choose **Netherlands** or **Lithuania** datacenter (EU)

2. **SSH into VPS:**
```bash
ssh root@YOUR_VPS_IP
```

3. **Update system:**
```bash
apt update && apt upgrade -y
```

#### Step 2: Install Docker + Docker Compose

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh

# Verify
docker --version

# Install Docker Compose
apt install docker-compose -y
```

#### Step 3: n8n Docker Compose Setup

1. **Create project folder:**
```bash
mkdir ~/n8n-docker && cd ~/n8n-docker
```

2. **Create `docker-compose.yml`:**
```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=SuperStrongPassword!
      - N8N_HOST=your-vps-ip-or-domain
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - WEBHOOK_URL=http://YOUR_VPS_IP:5678/
    volumes:
      - ./n8n_data:/home/node/.n8n
```

#### Step 4: Run It

```bash
docker-compose up -d
```

n8n will be accessible at: `http://YOUR_VPS_IP:5678`

**Production tip**: Later, put it behind Nginx + HTTPS with Let's Encrypt (see Day 5 process).

#### Step 5: First Login

- Username: `admin` (from `N8N_BASIC_AUTH_USER`)
- Password: `SuperStrongPassword!`
- UI: Clean, drag-and-drop workflow builder

---

### 3. Core Concepts in n8n

#### Triggers (How Workflows Start)

**Webhook Trigger:**
- Exposes endpoint like `https://your-vps.com/webhook/test`
- Any POST/GET JSON or form-data launches workflow
- Use case: Send data from your FastAPI (Day 5) to n8n instantly

**Cron Trigger:**
- Schedule execution (every X minutes, daily at midnight, cron syntax)
- Use case: ETL job pulling API data every morning

**App Triggers:**
- Gmail new email, Slack message, GitHub PR, etc.
- Note: Most require API credential configuration

#### Nodes (Building Blocks)

Each workflow = chain of nodes. Each node = a tool or action (HTTP request, Transform, AI model, Slack message). Each passes JSON forward.

**Example Node Chain:**
```
Webhook → HTTP Request (API) → Set (rename fields) → IF > condition → Slack
```

#### Credentials (Secrets Management)

- All API keys stored securely as **Credentials** in n8n's vault
- Stored encrypted in `~/.n8n/config` (local)
- Example: Configure OpenAI API key once → every AI node can use it

#### Data Flow (JSON Everywhere)

- Each node outputs JSON objects
- View in **Execution preview**
- Transform with:
  - **Set Node**: Pick fields you need
  - **Function Node**: JS code to transform objects
  - **Item Lists Node**: Map, reduce, filter arrays

#### Checkpoint Practice

In n8n UI:
1. Create new workflow
2. Add **Webhook Trigger** (URL appears)
3. Add **HTTP Request** node: `GET https://jsonplaceholder.typicode.com/todos/1`
4. Execute → inspect JSON payload in preview
5. Add **IF Node**: Condition `id > 1`
6. Add **Slack** or **Execute Command** node (log to console)

You've now created: trigger → API call → conditional branch in n8n.

---

### 4. Advanced Capabilities in n8n

#### Flow Control Nodes

These enable logic and orchestration like a programming language inside your workflow.

**IF Node:**
- Branch to 2 paths (True / False)
- Example: If `[amount] > 1000` → HighValue path; else Normal path

**Switch Node:**
- Multi-case branching (like switch-case in code)
- Example: Select action by `[country]` → DE = German CRM, FR = French CRM

**Merge / Combine:**
- Join 2 branches back together
- Mode = "Wait" (wait for both inputs) or "Pass Through" (continue whichever finishes first)

**Split In Batches:**
- Take array of items, process N at a time
- Example: Loop over 100 leads → send to FastAPI in batches of 10

**Wait / Delay:**
- Pause until condition or time
- Example: Pause until tomorrow → then continue sending report

#### Tools Modules (Utility Nodes)

**HTTP Request:**
- Call ANY API endpoint (including your FastAPI)
- Options:
  - Method: GET, POST, PUT, DELETE
  - Auth: Header key, Basic, OAuth2
  - Send JSON or form-data

**Function:**
- Write custom JavaScript to manipulate incoming JSON
```javascript
return items.map(item => {
  item.json.fullName = item.json.firstName + " " + item.json.lastName;
  return item;
});
```

**Item Lists:**
- Manipulate arrays: filter, aggregate, sort, reduce

**Set:**
- Keep only certain fields + rename them
- Example: Input `{id, name, email, timestamp}` → Output `{customer_name, customer_email}`

**Edit Fields:**
- Mass-rename or delete JSON keys

Together, Tools nodes = lightweight pandas, but visual.

#### AI Agents

n8n has nodes for OpenAI, HuggingFace, GPT4All, etc.

**Capabilities:**
- Summarize text
- Classify sentiment
- Extract structured data
- Chain multiple prompts = mini "agent"

**Example Flow:**
```
Webhook → Function (extract email text) → OpenAI Node (summarize) →
IF (negative tone) → Slack alert
```

#### Datastores

Internal persistence mechanism - store structured data without external DB.

**CRUD operations:**
- **Insert**: Add records
- **Query**: Retrieve by field
- **Update / Delete**

**Use cases:**
- Save API logs / AI outputs
- Cache previous results
- Store "state" between executions

#### Keys & Credentials

Instead of hardcoding secrets → store in **n8n's Credentials Manager**:
- OpenAI API key
- Google OAuth
- Slack token

Encrypted, not in plain text in workflow JSON.

#### Data Structures

n8n passes objects as JSON. Each node receives `items[]`, each containing `json` payload.

**Manipulation tools:**
- **Set**: Create new fields
- **Function**: JS logic
- **Move Binary Data**: Convert file ↔ JSON

#### Custom Apps

- Write your own nodes in JS (`n8n-node-dev` CLI)
- Or wrap your FastAPI into a reusable internal app node
- Power flexibility: In Make, you're limited to existing modules → in n8n you build your own

---

### 5. Example Advanced Workflow

**Scenario:** AI-powered lead scoring with datastore

**Flow:**

1. **Webhook Trigger**
   - Receives: `{"name":"Alice","email":"a@example.com","message":"Interested in AI automation","budget":2500}`

2. **IF Node**
   - If `budget > 2000` → mark "HighValue"

3. **OpenAI Node**
   - Summarize message → classify as intent ("Lead" / "Spam" / "Support")

4. **Switch Node**
   - Case = "Lead" → send to CRM
   - Case = "Support" → send to Support Slack

5. **Datastore Node**
   - Save lead with classification + budget + timestamp

6. **Google Sheets Node**
   - Log for easy viewing

**Visual Graph:**
```
[Webhook] → [IF budget >2000]
         ├─ True → [OpenAI classify] → [Switch] → CRM/Slack
         └─ False → [Datastore: insert + Sheets log]
```

---

### 6. End-to-End EU-Safe Hosting with n8n

**Setup:**
1. Deploy n8n on Hostinger VPS (KVM) with Docker Compose (section 2)
2. Harden it:
   - UFW firewall
   - Nginx reverse proxy → HTTPS with Let's Encrypt
   - Strong password
3. Use internal Datastore for logs
4. Connect to your FastAPI from Day 5 (via HTTP Request node)
   - Example: Use `/api/greet/{name}`

**Result:** 100% self-hosted automation (GDPR-safe)

---

### 7. Practice Tasks (Hands-On)

#### Task A: Flow Control

Create workflow:
1. **Webhook Trigger**
2. **IF Node**: Condition `amount > 100`
   - True → HTTP Request to your FastAPI `/api/greet/Alice`
   - False → Record to Google Sheets

#### Task B: Tools Practice

1. Add **Function Node**: Combine `firstName` + `lastName`
2. Add **Item Lists Node**: Sort by `amount`
3. Add **Set Node**: Reduce fields to only `name`, `amount`, `status`

#### Task C: AI Agent

1. Send message text to **OpenAI Node**
2. Ask model: "Classify message as Lead/Spam/Support"
3. Route via **Switch Node** accordingly

#### Task D: Datastore

1. Create datastore `lead_records`
2. When webhook fires → **Insert** record
3. Add **Query** node → retrieve last 5 leads
4. Connect to **Slack** → "Daily 5 latest leads"

**Documentation:**
Document in `day06_n8n/notes.md`:
- Which Flow Control nodes you used
- Output JSON snapshots
- Differences vs Make.com

---

### 8. FastAPI Integration Example

**Connect n8n to your Day 5 FastAPI**

**In n8n workflow:**

1. **Add HTTP Request Node**
   - Method: POST
   - URL: `https://your-fastapi-domain.com/api/data`
   - Authentication: None (or add Bearer token if secured)
   - Headers: `Content-Type: application/json`
   - Body (JSON):
```json
{
  "name": "{{ $json.name }}",
  "email": "{{ $json.email }}",
  "amount": "{{ $json.amount }}"
}
```

2. **Parse Response**
   - Add **Set Node** to extract response fields
   - Or **Function Node** for complex parsing

3. **Error Handling**
   - Add **IF Node** after HTTP Request
   - Condition: `{{ $json.status }} === 200`
   - True → Continue flow
   - False → Send error to Slack/logging

**Example Full Flow:**
```
[Webhook] → [HTTP Request to FastAPI] → [IF status=200]
                                      ├─ True → [Datastore log success]
                                      └─ False → [Slack error alert]
```

---

### 9. n8n vs Make.com: Key Differences

| Aspect | n8n | Make.com |
|--------|-----|----------|
| **Hosting** | Self-host or cloud | Cloud only |
| **Pricing** | Execution-based (cloud) / Unlimited (self-host) | Operations-based |
| **Customization** | Full JS/Python code nodes | Limited custom code |
| **EU Compliance** | Full control (self-host) | SaaS terms |
| **Learning Curve** | Moderate (more technical) | Easier (visual-first) |
| **Integrations** | 400+ | 1,500+ |
| **Advanced Logic** | IF, Switch, Split, Function | Routers, Filters, Iterators |
| **Best For** | Devs wanting control & compliance | Non-technical users, rapid setup |

---

### 10. Production Checklist

Before going live with n8n:

- [ ] Enable HTTPS (Nginx + Let's Encrypt)
- [ ] Set strong authentication (change default password)
- [ ] Configure UFW firewall (allow only 80, 443, 22)
- [ ] Set up automated backups of `./n8n_data`
- [ ] Configure webhook URLs with proper domain
- [ ] Test all credentials (API keys, OAuth tokens)
- [ ] Set up monitoring (uptime checks, error alerts)
- [ ] Document all workflows in version control
- [ ] Configure queue mode for high-volume workflows
- [ ] Set execution timeout limits
- [ ] Configure retry logic for critical workflows

---

### Summary

**Make.com**: Best for quick visual automations with extensive app library. Great for non-technical users and rapid prototyping.

**n8n**: Best for developers wanting full control, EU compliance, unlimited executions, and complex logic with code. Self-hosting eliminates vendor lock-in and provides true GDPR compliance.

**Next Steps:**
1. Set up both platforms (Make SaaS trial + n8n self-hosted)
2. Build the same workflow on both platforms
3. Compare: ease of use, features, cost, flexibility
4. Document: Which fits your use case better
5. Connect both to your FastAPI from Day 5
6. Create one end-to-end flow: Webhook → FastAPI → Database → Notification
