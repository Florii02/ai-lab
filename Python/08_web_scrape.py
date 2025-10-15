# ============================================================================
# 8. WEB SCRAPING BASICS
# ============================================================================
# WHAT: Extract data from websites using requests and BeautifulSoup
# WHY: Collect data from web pages, monitor prices, gather information
# WHEN: Need data from websites without APIs, research, price monitoring
# NOTE: Requires: pip install requests beautifulsoup4

print("="*60)
print("WEB SCRAPING - REQUESTS + BEAUTIFULSOUP + SELENIUM")
print("="*60)

# ============================================================================
# BASIC WEB SCRAPING (REQUESTS + BEAUTIFULSOUP)
# ============================================================================

print("\n1. BASIC WEB SCRAPING:")
print("NOTE: Install with: pip install requests beautifulsoup4")

try:
    import requests
    from bs4 import BeautifulSoup

    # Fetch web page
    url = "https://example.com"
    print(f"Fetching: {url}")

    response = requests.get(url)
    html = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract data
    print(f"✓ Page title: {soup.title.string if soup.title else 'No title'}")

    # Extract all links
    links = soup.find_all('a')
    print(f"✓ Found {len(links)} links")

    # Extract all paragraphs
    paragraphs = soup.find_all('p')
    if paragraphs:
        print(f"✓ First paragraph: {paragraphs[0].text[:100]}...")

    print("""
    💡 Use Cases for Requests + BeautifulSoup:
    - Static websites (no JavaScript)
    - Price monitoring
    - News aggregation
    - Extract structured data (tables, lists)
    - Fast and lightweight
    """)

except ImportError as e:
    print(f"✗ Missing library: {e}")
    print("Install with: pip install requests beautifulsoup4")

# ============================================================================
# ADVANCED WEB SCRAPING (SELENIUM)
# ============================================================================

print("\n" + "="*60)
print("2. SELENIUM - BROWSER AUTOMATION")
print("="*60)

print("""
💡 Why Selenium?
- Handles JavaScript-heavy sites
- Can click buttons, fill forms
- Wait for dynamic content to load
- Simulate real user behavior
- Screenshot capabilities

Install: pip install selenium
Also need: Chrome/Firefox WebDriver

Use Cases:
- Login to websites
- Fill and submit forms
- Navigate multi-page flows
- Scrape JavaScript-rendered content
- Automated testing
""")

print("\nExample Selenium Code (requires setup):")
print('''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
driver = webdriver.Chrome()  # or Firefox()

# Navigate to page
driver.get("https://example.com")

# Wait for element to load
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

# Click button
element.click()

# Fill form
input_field = driver.find_element(By.NAME, "username")
input_field.send_keys("myusername")

# Get page content after JavaScript execution
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Close browser
driver.quit()
''')

# ============================================================================
# WHEN TO USE WHICH?
# ============================================================================

print("\n" + "="*60)
print("WHEN TO USE WHICH TOOL?")
print("="*60)

print("""
✅ Use Requests + BeautifulSoup when:
   - Website is static (no JavaScript)
   - Speed is important
   - Simple data extraction
   - Low resource usage needed

✅ Use Selenium when:
   - Content loaded via JavaScript
   - Need to interact with page (click, type, scroll)
   - Login required
   - Multi-step navigation
   - Dynamic content (React, Vue, Angular sites)

💡 Pro Tip: Start with Requests + BeautifulSoup (faster, simpler)
            Only use Selenium if needed (slower, more complex)
""")

# ============================================================================
# PRACTICAL AUTOMATION IDEAS
# ============================================================================

print("\n" + "="*60)
print("AUTOMATION IDEAS (FROM ATBS)")
print("="*60)

print("""
1. Price Monitor Bot
   - Track product prices daily
   - Alert when price drops

2. Job Listing Scraper
   - Monitor job boards
   - Filter by keywords
   - Save to CSV/Excel

3. News Aggregator
   - Collect articles from multiple sites
   - Summarize headlines

4. Real Estate Tracker
   - Monitor new listings
   - Filter by price/location

5. Social Media Automation
   - Auto-post to platforms
   - Schedule posts (with Selenium)

6. Form Auto-fill
   - Automate repetitive form submissions
   - Survey completion

💡 Combine with:
   - Schedule (run daily/hourly)
   - Email alerts (notify on changes)
   - Database storage (track history)
   - APIs (enrich scraped data)
""")
