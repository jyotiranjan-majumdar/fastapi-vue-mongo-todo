from pydantic import BaseModel


class createPost(BaseModel):
    title : str
    content : str=None

class returnPost(BaseModel):
    id: str
    message : str

class updatepost(BaseModel):
    title : str
    content : str=None
