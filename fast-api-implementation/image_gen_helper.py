from openai import OpenAI
from PIL import Image
import base64
import io


def inference_image_jsonb64(prompt: str, openai_client: OpenAI, size: str = "1024x1024", model: str = "dall-e-2"):
  """
  model:
    -> dall-e-2 (default)
    -> dall-e-3

  size of image:
    -> one of [256x256, 512x512, 1024x1024] for dalle-2
    -> one of [1024x1024, 1792x1024, 1024x1792] for dalle-3
  """
  response = openai_client.images.generate(
  model=model,
  prompt=prompt,
  size=size,
  quality="standard" , # hd would give a lot of attention to detail and recommended to use for texture specific creative and conematic generation
  response_format="b64_json", 
  n=1, # number of images generated -> 1
  )

  return response.data[0].b64_json


def decode_and_save_image(json_content, output_filename): # base64 json content
  """
  Decodes a base64 encoded image from a JSON file and saves it locally.

  Args:
      json_file (str): Path to the JSON file containing the base64 encoded image.
      output_filename (str): Name of the output image file.

  Return:
    str -> output path
  """

  # Decode the base64 data
  decoded_data = base64.b64decode(json_content)

  # Use Pillow to create an image from the decoded data
  image = Image.open(io.BytesIO(decoded_data))

  # output path
  output_path = './generated_images/' + output_filename + '.png' # png extension is added, using png for more crispness

  # Save the image to the specified location
  image.save(
      output_path # !!!!!!!! remove /content while deploying
      )

  return output_path