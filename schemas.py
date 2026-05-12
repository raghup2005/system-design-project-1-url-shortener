from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    short_url: str