with open('./api_keys/OPENAI_API.txt') as jammer, open('./api_keys/GEMINI_API.txt') as lammer:
    OPENAI_API = jammer.read()
    GEMINI_API = lammer.read()


if __name__ == "__main__":
    print(OPENAI_API, GEMINI_API)