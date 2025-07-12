from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from backend.utils.config import LINKEDIN_CLIENT_ID, LINKEDIN_REDIRECT_URI, LINKEDIN_CLIENT_SECRET
import requests

router = APIRouter()

@router.get("/auth/linkedin")
def linkedin_login():
    linkedin_auth_url = (
        "https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code"
        f"&client_id={LINKEDIN_CLIENT_ID}"
        f"&redirect_uri={LINKEDIN_REDIRECT_URI}"
        f"&scope=r_liteprofile%20r_emailaddress%20w_member_social"
    )
    return RedirectResponse(linkedin_auth_url)

@router.get("/auth/callback")
def linkedin_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)
    # Exchange code for access token
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": LINKEDIN_REDIRECT_URI,
        "client_id": LINKEDIN_CLIENT_ID,
        "client_secret": LINKEDIN_CLIENT_SECRET,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(token_url, data=data, headers=headers)
    if resp.status_code != 200:
        return JSONResponse({"error": "Failed to get access token", "details": resp.text}, status_code=400)
    access_token = resp.json().get("access_token")
    # For now, just return the token (in production, store it and fetch profile)
    return {"access_token": access_token} 