import requests
import json
import sys

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    print(f"Fetching data for '{username}'...")
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print("\n--- GitHub Profile Info ---")
            print(f"Name: {data.get('name', 'N/A')}")
            print(f"Bio: {data.get('bio', 'N/A')}")
            print(f"Public Repos: {data.get('public_repos')}")
            print(f"Followers: {data.get('followers')}")
            print(f"Following: {data.get('following')}")
            print(f"Profile URL: {data.get('html_url')}")
            print("---------------------------\n")
        elif response.status_code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"Error: Could not fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetcher.py <github_username>")
    else:
        user = sys.argv[1]
        get_github_profile(user)
