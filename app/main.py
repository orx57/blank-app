from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import re

app = FastAPI()

patterns = [
    re.compile(r"(?P<asset_name>(?P<client_code>[^-]{5})-(?P<asset_category>[^-]+)-(?P<environment>[^-]{1})-(?P<suffixes>[\S-]+))"),
    re.compile(r"(?P<asset_name>(?P<client_code>[^-]{5})-(?P<environment>[^-]{1})(?P<platform_nature>[^-]{1})(?P<os_type>[^-]{1})(?P<role>[^\d-]{3})(?P<id>[\d-]{3}))")
]

def validate_asset_name(asset_name: str):
    for pattern in patterns:
        match = pattern.match(asset_name)
        if match:
            return match.groupdict(), True
    return {"asset_name": asset_name}, False

@app.get("/validate/{asset_name}")
async def validate(asset_name: str):
    asset, is_valid = validate_asset_name(asset_name)
    if is_valid:
        return {
            "asset": asset,
            "changed": False,
            "failed": False,
            "is_valid": True,
            "msg": "Asset name checked successfully"
        }

    return JSONResponse(
        status_code=400,
        content={
                "asset": asset,
                "changed": False,
                "failed": False,
                "is_valid": False,
                "msg": "Invalid asset name format"
            },
    )
