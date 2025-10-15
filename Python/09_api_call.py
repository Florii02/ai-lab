# ============================================================================
# 9. API CALLS - WORKING WITH WEB APIS
# ============================================================================
# WHAT: Fetch data from web services using HTTP requests
# WHY: Access real-time data, integrate with services, build connected apps
# WHEN: Need live data (weather, stocks, news), integrate external services

try:
    import requests

    print("API Call Example: Bitcoin Price")
    print("="*50)

    # Make GET request to API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        btc_price = data["bpi"]["USD"]["rate"]
        print(f"Current BTC Price (USD): ${btc_price}")

        # Access nested data
        print(f"Updated: {data['time']['updated']}")
    else:
        print(f"API call failed with status: {response.status_code}")

    print("\n# WHY USE APIs:")
    print("# - Get real-time data (weather, stock prices, news)")
    print("# - Integrate services (payment, maps, social media)")
    print("# - Build connected applications")
    print("# - Automate workflows across platforms")

except ImportError:
    print("requests library not installed")
    print("Install with: pip install requests")
except Exception as e:
    print(f"Error: {e}")
