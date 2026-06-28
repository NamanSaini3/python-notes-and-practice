import  requests

# def fectch_random_ user_freeapi():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data = response.json()
    
#     if data["success"] and "data" in data:
#         user_data = data["data"]
#         username = user_data["login"]["username"]
#         country = user_data["location"]["country"]
#         return username, country
#     else:
#         raise Exception("failed to fetch user data")
    
    
    
# def main():
#     try:
#          username, country = fectch_random_user_freeapi()
#          print(f"Username: {username} \n country : {country}")
#     except Exception as e:
#         print(str(e))
        
# if __name__ == "__main__":
#         main()



def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]

        first = user_data["name"]["first"]
        last = user_data["name"]["last"]
        full_name = first + " " + last

        gender = user_data["gender"]
        phone_number = user_data["phone"]
        city = user_data["location"]["city"]

        return full_name, gender, phone_number, city
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:    # try catch mai rep kiya kar carece  na ho
        full_name, gender, phone_number, city = fetch_random_user()

        print(f"Full Name: {full_name}")
        print(f"Gender: {gender}")
        print(f"Phone Number: {phone_number}")
        print(f"City: {city}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()

    
    
         
         
         
         
         
        


