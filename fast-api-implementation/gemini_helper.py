from langchain.prompts import PromptTemplate

def inference_gemini_chain(llm, prompt_template):
  """
  prompt is expected to have input variables in them aswell
  then the input variables are supposed to be fed with the inputs given by user as key value pairs
  a chain is returned as output
  """

  template = prompt_template

  prompt = PromptTemplate.from_template(template)

  chain = prompt | llm

  return chain

  #print(chain.invoke({"question": question}))


def invoke_chains_and_inference_output(chain, **prompt_inputs):
  return chain.invoke(prompt_inputs)