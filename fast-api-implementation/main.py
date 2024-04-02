from fastapi import FastAPI
from pydantic import BaseModel
from langchain_helper import final_wrapper_for_gen_image, final_wrapper_for_chunk_fantasization, final_wrapper_for_heading_generation, final_wrapper_for_imp_info_deep_dive, img_gen_chain, chunk_fantasy_chain, heading_chain, chunk_imp_info_chain
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
    word_limit: str # not using integers coz, we dont want to clash with string based templates
    chunk_content: str

class Heading(BaseModel):
    chunk: str

class DeepDiveInfo(BaseModel):
    word_limit: str # not using integers coz, we dont want to clash with string based templates
    chunk: str

@app.post('/gen-image', tags=["Image Generation"]) # just the host's name for routing
def gen_img(img: Image): # giving query parameters "localhost/blog?par1=val&par2=val"
    json_b64_img = final_wrapper_for_gen_image(img_gen_chain, img.theme)
    print("Generated Image")
    return {'json-b64-format-of-image-generated': json_b64_img}

@app.post('/gen-chunk', tags=["Text Fantasization"]) # just the host's name for routing
def gen_chunk(chunk: Chunk): # giving query parameters "localhost/blog?par1=val&par2=val"
    fantasized_chunk = final_wrapper_for_chunk_fantasization(chunk_fantasy_chain, chunk.theme, chunk.word_limit, chunk.chunk_content)
    print("Generated Fantasized Text")
    return {'generated-chunk': fantasized_chunk}

@app.post('/gen-heading', tags=['Text Fantasization']) # this is a route for generating headings
def gen_heading(chunk: Heading):
    generated_heading = final_wrapper_for_heading_generation(heading_chain, chunk.chunk)
    print("Generating Heading")
    return {'generated-heading': generated_heading}

@app.post('/gen-detailed-info', tags=["Detailed Text Description(DeepDive)"])
def gen_detailed_info(chunk: DeepDiveInfo):
    extracted_detailed_info = final_wrapper_for_imp_info_deep_dive(chunk_imp_info_chain, word_cnt = chunk.word_limit, chunk=chunk.chunk)
    print("Detailed Description Generated")
    return {'extracted-detailed-info': extracted_detailed_info}
