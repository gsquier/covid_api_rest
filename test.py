import requests

BASE = "http://127.0.0.1:5000/"

# Test 1:
query = {'country':'DK'}
print("The Test 1 request is:", str(query))
input("Press Enter to continue Test 1...")
response = requests.get(BASE + "country_tests_done", json=query)
print(response.json())
print('\n')

# Test 2:
query = {'country':''}
print("The Test 2 request is:", str(query))
input("Press Enter to continue Test 2...")
response = requests.get(BASE + "country_tests_done", json=query)
print(response.json())
print('\n')

# Test 3:
query = {'cou':'ES'}
print("The Test 3 request is:", str(query))
input("Press Enter to continue Test 3...")
response = requests.get(BASE + "country_tests_done", json=query)
print(response.json())
print('\n')

# Test 4:
query = {'date':'2020-12'}
print("The Test 4 request is:", str(query))
input("Press Enter to continue Test 4...")
response = requests.get(BASE + "date_tests_done", json=query)
print(response.json())