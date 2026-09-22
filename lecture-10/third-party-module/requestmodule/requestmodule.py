import requests
response = requests.get('https://api.github.com/users/s6906022510156')

if response.status_code == 200:
    user_data = response.json()

    print(f"username: {user_data['login']}")
    print(f"name: {user_data['name']}")
    print(f"bio: {user_data['bio']}")
    print(f"public repos:{user_data['public_repos']}")
    print(f"followers: {user_data['followers']}")
    print(f"fillowing: {user_data['following']}")
else:
    print("failed to retrive data.")