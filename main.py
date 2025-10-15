from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime, timezone

app = FastAPI(
    title="HNGi13 - GetMe API",
    description="A simple REST API that returns user profile information and a random cat fact."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

CAT_FACT_URL = "https://catfact.ninja/fact"


@app.get("/me", tags=["Profile"])
def get_me():
    try:
        response = requests.get(CAT_FACT_URL, timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "No fact available.")
    except (requests.RequestException, ValueError):
        cat_fact = "Could not fetch a cat fact right now. Please try again later."
    
    timestamp = datetime.now(timezone.utc).isoformat()
    
    data = {
        "status": "success",
        "user": {
            "email": "preciousezeigbo81@gmail.com",
            "name": "Precious Ezeigbo",
            "stack": "Python/FastAPI",
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return JSONResponse(content=data, media_type="application/json", status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)