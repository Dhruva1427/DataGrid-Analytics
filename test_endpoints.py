"""
Endpoint Status Checker
=======================
Checks availability and response codes for core system endpoints.
"""
import requests

service_endpoints = [
    '/api/kpis',
    '/api/data-quality/kpis',
    '/api/data-quality/trend',
    '/api/data-quality/checks',
    '/api/revenue/timeseries?granularity=daily',
]

for endpoint_path in service_endpoints:
    try:
        resp = requests.get(f'http://localhost:8000{endpoint_path}', headers={'X-User-Role': 'admin'})
        print(f'{endpoint_path}: status {resp.status_code}')
        if resp.status_code != 200:
            print(f'  Error output: {resp.text[:200]}')
    except Exception as err:
        print(f'{endpoint_path}: Exception encountered - {err}')

