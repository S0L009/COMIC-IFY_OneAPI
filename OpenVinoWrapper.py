from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline

model_id = "Macromrit/Lexicon"

def call_model(model_id, task, prompt=None, text=None, target_lang=None):
  """
  Wrapper function to call various NLP models using transformers and OpenVINO.

  Args:
      model_id (str): Hugging Face model identifier.
      task (str): NLP task to perform (e.g., "generate", "translate", "classify").
      prompt (str, optional): Text prompt for generation task. Defaults to None.
      text (str, optional): Text for translation or classification tasks. Defaults to None.
      target_lang (str, optional): Target language for translation task. Defaults to None.

  Returns:
      object: Output from the NLP task (e.g., generated text, translation, classification label).

  Raises:
      ValueError: If an unsupported task is provided.
  """
  # Load model with OpenVINO optimizations
  model = OVModelForCausalLM.from_pretrained(model_id, export=True)
  tokenizer = AutoTokenizer.from_pretrained(model_id)

  # Perform task-specific actions
  if task == "generate":
    if prompt is None:
      raise ValueError("Prompt is required for generation task.")
    output = llm.generate_text(prompt=prompt)  # Assuming llm is defined elsewhere
  elif task == "translate":
    if text is None:
      raise ValueError("Text is required for translation task.")
    output = pipeline("translation", model=model, tokenizer=tokenizer)(text, target_lang=target_lang)
  elif task == "classify":
    if text is None:
      raise ValueError("Text is required for classification task.")
    # Implement classification logic using transformers pipeline or custom approach
    output = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)(text)  # Example for sentiment analysis
  else:
    raise ValueError(f"Unsupported task: {task}")

  return output
