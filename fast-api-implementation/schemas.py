from pydantic import BaseModel

class Image(BaseModel):
    theme: str 

class Chunk:
    theme: str
    word_limit: str
    chunk_content: str