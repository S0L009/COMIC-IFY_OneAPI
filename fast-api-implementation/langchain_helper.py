from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
import json
import base64
from pypdf import PdfReader 
from PIL import Image
import io
from api_loader import OPENAI_API, GEMINI_API

# imported modules
from image_gen_helper import inference_image_jsonb64
from gemini_helper import inference_gemini_chain, invoke_chains_and_inference_output

# for testing the output
from pdf_helper import read_n_return_pages
from image_gen_helper import decode_and_save_image

# initializing openAI client ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
client = OpenAI(api_key=OPENAI_API)


# loading the endpoint for gemini ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API)


# chains for generation ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# chain 1 - for generating prompt to inference an image
img_gen_chain = inference_gemini_chain(llm, """
You are a world class prompt writer, your task is to write a prompt for generating image explaining the features in a very clear and specific way in your own in a creative way for a given context delimited by triple back ticks. 
When crafting your prompts, it's essential to be as descriptive and specific as possible. Provide details about the subject, setting, style, composition, and any other relevant aspects you want the AI to consider. And make sure that the prompt generated is safe for inferencing.

context: Hippopotamus
generated-prompt: A massive hippopotamus, A large, semi-aquatic mammal with a barrel-shaped body, short legs, and a huge mouth, Partially submerged in a calm river or pond, surrounded by lush vegetation and trees, Realistic and highly detailed, with a focus on capturing the texture of the hippo's thick, wrinkled skin and the reflections in the water, Include water droplets or splashes around the hippo, and perhaps a few small fish or aquatic plants in the water.

context: Leopard
generated-prompt: A powerful and majestic leopard. A large and muscular feline predator with a sleek, spotted coat of intricate patterns, intense yellow-green eyes, and sharp claws. Crouched on a thick, gnarled tree branch in a dense tropical forest, surrounded by lush vegetation and dappled sunlight filtering through the canopy. Highly realistic and detailed, with a focus on capturing the texture of the leopard's fur, the play of light and shadow, and the intricate patterns of the spotted coat. A low-angle shot, with the leopard's head and upper body in the foreground, taking up a significant portion of the frame, and its tail trailing off towards the background. The leopard's ears should be perked up, and its gaze should be fixed intently on something off-camera, conveying a sense of stealth and predatory instinct, with perhaps a glimpse of potential prey in the distance

context: Marvel Avengers
generated-prompt: The Marvel Avengers team, including Iron Man in his iconic red and gold armor, Captain America with his vibranium shield, Thor wielding Mjolnir, the incredibly muscular green Hulk, the skilled Black Widow, and the archer Hawkeye. A group of iconic superheroes standing together in heroic poses, ready for battle. In the streets of New York City, with recognizable landmarks like the Avengers Tower in the background. In a dynamic, comic book-inspired art style with vibrant colors, bold outlines, and dramatic lighting and visual effects. A wide-angle shot from a low angle, capturing the full team in action poses, with energy blasts, rubble, and debris adding a sense of intensity. Iron Man's repulsor beams should be visible, Captain America's shield should be in a defensive position, Thor's cape should be billowing, and the Hulk should be in a powerful stance, with Widow and Hawkeye ready for combat

context: Harry Potter
generated-prompt: Harry Potter, Hermione Granger, and Ron Weasley. Harry with his messy black hair, round glasses, and a lightning bolt scar on his forehead, wearing his Gryffindor robes and holding his wand. Hermione with bushy brown hair, holding a book, and Ron with his red hair and freckles, clutching his wand. In the Great Hall of Hogwarts, with long tables and floating candles, the enchanted ceiling reflecting the night sky. In a realistic, cinematic style, with intricate details and lighting reminiscent of the Harry Potter movies. Include magical elements such as floating books, spells being cast, or perhaps a house elf or owl in the background.

context: Mr.Bean
generated-prompt: Mr. Bean (Rowan Atkinson), the beloved comedic character. A middle-aged man with a round, expressive face, a distinctively large nose, and short, straight brown hair. He is wearing his iconic outfit – a brown tweed jacket, a red tie, and a white shirt. His expression should capture his trademark exaggerated and comical facial expressions, such as a raised eyebrow, a pursed lip, or a squinting, quizzical look. A simple living room setting, with a couch or chair in the background, keeping the focus on Mr. Bean.  Highly realistic and detailed, with a focus on capturing the likeness of Rowan Atkinson as Mr. Bean, as well as the textures and folds of his clothing and the subtleties of his facial expressions. A close-up shot, with Mr. Bean's face and upper body taking up a significant portion of the frame, allowing for his iconic expressions and body language to be clearly visible. Include Mr. Bean holding or interacting with an everyday object, such as a TV remote or a household item, in an unconventional or comical way, perhaps with a small mishap or mess in the background, capturing his clumsy and quirky nature.                                                                              

context: ```{context_to_generate}```
generated-prompt:
""")

# chain 2 - for fanatasizing and draw parallels b/w given text chunks and fantasy theme
chunk_fantasy_chain = inference_gemini_chain(llm, """
You are a World Class story writer, your task is to analyse the text chunk given delimited by triple backticks and extract essential ideas and concepts from it, and explain those ideas and concepts using "{inspiring_theme}" ideas and concepts. Be creative, take your time and make the content interesting and fun to read.  The output should be a descriptive paragraph with having no more than {word_count} words

chunk: {text_chunk}
generated-output:
""")

# chain 3 - for generating headings for chunks
# for figuring headings for each chunk
heading_chain = inference_gemini_chain(llm, """
You are a World Class Heading Writer, your task is to analyse the given context, delimited by triple backticks. Then assign an small heading of 4-6 words for the chunk, make sure the heading is creative, interesting, easy to understand and eye catchy
IMPORTANT: DONT USE AN FORMATTING FOR THE GENERATED TEXT

chunk: {fantasy_chunk}
generated-heading:
""")

chunk_imp_info_chain = inference_gemini_chain(llm, """
You are a World Class Text Analyser, your task is to analyse the text chunk given delimited by triple backticks and extract essential ideas and concepts from it. then make sure to list out all those important points, preserve info as much as possible and give point wise output with a bit of description

IMPORTANT: dont generate more than {word_count} words, dont use formatting like '**'

output-format:
  <3 line description>
  <detailed point-wise info>

chunk: {text_chunk}
generated-output:
   """)



# final function for generating images ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def final_wrapper_for_gen_image(chain, context_of_image): # returns the jb64 format of image being generated
  while True:
    try:
      img_prompt = invoke_chains_and_inference_output(chain, context_to_generate = context_of_image)
      inferenced_jb64_output = inference_image_jsonb64(img_prompt, client, model='dall-e-3')
    except:
      print("Some Bad 400 response with image generation, Retrying it Babbbbyyy")
    else:
      break
  # decode_and_save_image(inferenced_jb64_output, image_name_2_save)
  return inferenced_jb64_output


# final function for inferencing interactive text-chunks ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def final_wrapper_for_chunk_fantasization(chain, theme, word_limit, chunk):
  while True:
    try:
      fantasized_output = invoke_chains_and_inference_output(chain, inspiring_theme= theme ,
        word_count= word_limit,
        text_chunk= chunk)
    except:
      print("Oppsy text generation went wrong man, redoing it again")
    else:
      break

  return fantasized_output

def final_wrapper_for_heading_generation(chain, chunk):
  while True:
    try:
      heading = invoke_chains_and_inference_output(chain, fantasy_chunk=chunk)
    except:
      print("Oppsy heading generation went wrong man, redoing it again")
    else:
      break
  
  return heading

def final_wrapper_for_imp_info_deep_dive(chain, word_cnt, chunk):
  while True:
    try:
      imp_info = invoke_chains_and_inference_output(chain, word_count=word_cnt, text_chunk=chunk)
    except:
        print("Oppsy deep dive info generation went wrong man, redoing it again")
    else:
      break
  
  return imp_info


if __name__ == "__main__":
  # sample prompt: Pokemon - try out different pokemons every single time
  # decode_and_save_image(final_wrapper_for_gen_image(img_gen_chain, "Hot Women by"), 'mr_bean')
  # print(final_wrapper_for_heading_generation(heading_chain, "In the Avengers realm, linear combinations assemble diverse heroes like Iron Man's tech, Thor's lightning, and Captain America's shield into a formidable force. Each hero brings a unique scalar, representing their power level, to the combination. The Avengers, like a matrix, combine these scalars with their abilities, forming a synergistic vector that defeats foes. From Hulk's brute strength to Black Widow's agility, each scalar enhances the overall team, showcasing the power of linear combinations to create extraordinary results."))
  print(final_wrapper_for_imp_info_deep_dive(chunk_imp_info_chain, 200, """
In linear algebra, Singular Value Decomposition (SVD) is a factorization technique for any real or complex matrix **A** (m x n). It decomposes **A** into three matrices:

* **U** (m x m): An orthogonal matrix containing the left singular vectors of **A**. These vectors capture the directions of greatest variance in the data represented by **A**.
* **Σ** (m x n): A diagonal matrix containing the singular values of **A** on its main diagonal. These non-negative values represent the scaling factors along the principal components identified by the left singular vectors.
* **V** (n x n)**:  An orthogonal (or unitary for complex matrices) matrix containing the right singular vectors of **A**. These vectors represent the basis for the range of **A**.

The decomposition is expressed as:

**A = U * Σ * Vᵀ**

where **Vᵀ** denotes the transpose of **V**.

**Technical aspects:**

* The number of non-zero singular values in **Σ** equals the rank of matrix **A**.
* The singular vectors corresponding to non-zero singular values form an orthonormal basis for the range of **A**. 
* The singular vectors corresponding to zero singular values span the null space of **A**.

SVD offers several advantages:

* **Dimensionality reduction:** By keeping only the top k singular values (where k represents the most significant components), we can obtain a lower-dimensional approximation of the original data in **A**. This is useful for tasks like image compression and dimensionality reduction algorithms like PCA.
* **Pseudoinverse calculation:** The SVD facilitates the computation of the Moore-Penrose pseudoinverse, which is helpful in solving ill-conditioned linear systems of equations (where the coefficient matrix **A** is close to singular).
* **Analysis of linear transformations:** SVD reveals the geometric interpretation of a linear transformation represented by **A**. It decomposes the transformation into rotations, scaling along principal components, and another rotation.

Understanding SVD requires a solid foundation in linear algebra concepts like matrices, vector spaces, orthogonality, and eigenvalues/eigenvectors. 
"""))
