from fastapi import FastAPI, HTTPException
import re

app = FastAPI()

patterns = [
    re.compile(r"(?P<asset_name>(?P<client_code>[^-]{5})-(?P<asset_category>[^-]+)-(?P<environment>[^-]{1})-(?P<suffixes>[\S-]+))"),
    re.compile(r"(?P<asset_name>(?P<client_code>[^-]{5})-(?P<environment>[^-]{1})(?P<platform_nature>[^-]{1})(?P<os_type>[^-]{1})(?P<role>[^\d-]{3})(?P<id>[\d-]{3}))")
]

@app.get("/validate/{asset_name}")
async def validate(asset_name: str):
    for pattern in patterns:
        match = pattern.match(asset_name)
        if match:
            decomposition = match.groupdict()
            return {asset_name: decomposition}

    raise HTTPException(status_code=400, detail="Invalid asset name format")
