from fastapi import FastAPI
from pydantic import BaseModel
from langchain_helper import final_wrapper_for_gen_image, final_wrapper_for_chunk_fantasization, img_gen_chain, chunk_fantasy_chain
import uvicorn
from schemas import Image, Chunk


app = FastAPI()


# ''''''''''''''''''''
# Schemas
from pydantic import BaseModel

class Image(BaseModel):
    theme: str 

class Chunk(BaseModel):
    theme: str
    word_limit: str
    chunk_content: str


@app.post('/gen-image') # just the host's name for routing
def gen_img(img: Image): # giving query parameters "localhost/blog?par1=val&par2=val"
    json_b64_img = final_wrapper_for_gen_image(img_gen_chain, img.theme)
    return {'json-b64-format-of-image-generated': json_b64_img}

@app.post('/gen-chunk') # just the host's name for routing
def gen_chunk(chunk: Chunk): # giving query parameters "localhost/blog?par1=val&par2=val"
    fantasized_chunk = final_wrapper_for_chunk_fantasization(chunk_fantasy_chain, chunk.theme, chunk.word_limit, chunk.chunk_content)
    print("Im here")
    return {'generated-chunk': fantasized_chunk}