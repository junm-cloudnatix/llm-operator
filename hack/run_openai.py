from openai import OpenAI

dummy_api_key = "<key>"

client = OpenAI(
  base_url="http://localhost:8082/v1",
  api_key=dummy_api_key
)

completion = client.chat.completions.create(
  model="gemma:2b",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)
print(completion.choices[0].message)


client = OpenAI(
  base_url="http://localhost:8080/v1",
  api_key=dummy_api_key
)

print ('Creating a fine-tuning job...')
client.fine_tuning.jobs.create(
  training_file="file-abc123",
  model="gemma:2b",
)

resp = client.fine_tuning.jobs.list()
print(resp)

# Run again with the fine-tuned model
client = OpenAI(
  base_url="http://localhost:8082/v1",
  api_key=dummy_api_key
)

completion = client.chat.completions.create(
  model="gemma:2b-fine-tuned",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)
print(completion.choices[0].message)
