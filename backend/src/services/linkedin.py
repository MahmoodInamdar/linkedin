import requests

def fetch_linkedin_profile(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    profile_url = "https://api.linkedin.com/v2/me"
    email_url = "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))"
    profile_resp = requests.get(profile_url, headers=headers)
    email_resp = requests.get(email_url, headers=headers)
    if profile_resp.status_code != 200 or email_resp.status_code != 200:
        return None
    profile_data = profile_resp.json()
    email_data = email_resp.json()
    email = email_data.get("elements", [{}])[0].get("handle~", {}).get("emailAddress", "")
    return {
        "id": profile_data.get("id"),
        "firstName": profile_data.get("localizedFirstName"),
        "lastName": profile_data.get("localizedLastName"),
        "email": email,
        "headline": profile_data.get("headline", {}).get("localized", {}).get("en_US", "")
    } 