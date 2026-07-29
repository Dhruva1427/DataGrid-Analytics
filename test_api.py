"""
API Route Sanity Suite
=======================
Executes sanity requests against key REST API routes.
"""
import requests

API_HOST = "http://localhost:8000/api"
REQUEST_HEADERS = {"X-User-Role": "admin"}

print("Executing API route verification suite...")
print("=" * 50)

target_routes = [
    ("GET", "/kpis", {}),
    ("GET", "/revenue/timeseries?granularity=daily", {}),
    ("GET", "/sales/city", {}),
    ("GET", "/products/top", {}),
    ("GET", "/stream/status", {}),
]

for http_method, route_path, payload in target_routes:
    target_url = f"{API_HOST}{route_path}"
    try:
        if http_method == "GET":
            response = requests.get(target_url, headers=REQUEST_HEADERS, timeout=5)
        else:
            response = requests.post(target_url, headers=REQUEST_HEADERS, json=payload, timeout=5)
        
        print(f"\n{http_method} {route_path}")
        print(f"Status Code: {response.status_code}")
        if response.status_code != 200:
            print(f"Response Error: {response.text[:200]}")
        else:
            print(f"Response Success: {str(response.json())[:100]}")
    except Exception as exc:
        print(f"\n{http_method} {route_path}")
        print(f"FAILED: {str(exc)}")

