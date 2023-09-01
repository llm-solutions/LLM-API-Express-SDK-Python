from . import LlmApi, ModelType

api_token = "YOUR_TOKEN"
llm_api = LlmApi(api_token=api_token)


# Get full response as a single object
response = llm_api.generate("What is deep learning, in one sentence?", ModelType.WIZARDLM_UNCENSORED_LLAMA_V2_13B)
if "error" in response:
    # Handle error
    print(response["error"])
else:
    # Handle generated text
    print(response["generated_text"])

# Get response as a stream
response_streaming = llm_api.generate_stream("What is deep learning, in one sentence?", ModelType.WIZARDLM_UNCENSORED_LLAMA_V2_13B)
for line in response_streaming:
    if "error" in line:
        # Handle error
        print(line["error"])
    else:
        # Handle generated text
        print(line["token"]["text"])