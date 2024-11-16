
def main():
    print("Hello from example!")
    import requests

    url = "http://localhost:8080/echo"
    data = {"message": "1212, World!",
            "author": "John Doe",
            
        }
    response = requests.post(url, json=data)
    print(response.json())


if __name__ == "__main__":
    main()
