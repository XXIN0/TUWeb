import requests
r=requests.post("http://localhost:8000/hello_user")
print(r.status_code)
print(r.text)

# 400
# {"errors": {"name": "Required parameter 'name' not supplied", "age": "Required parameter 'age' not supplied"}}

payload={"name":"zhangsan","age":18}
r=requests.post("http://localhost:8000/hello_user",json=payload)
print(r.status_code)
print(r.text)

# 200
# {"zhangsan": "18"}