from pydantic import BaseModel

class JobPost(BaseModel):
    title: str
    