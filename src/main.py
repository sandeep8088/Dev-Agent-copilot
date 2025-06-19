import pandas as pd
from sentence_transformers import SentenceTransformer, util
import openai

# Load data
df = pd.read_csv('data/jira_tickets.csv')

# Embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['summary'].tolist(), convert_to_tensor=True)

# Compute similarities
similarities = util.pytorch_cos_sim(embeddings, embeddings)
duplicates = []

for i in range(len(df)):
    for j in range(i+1, len(df)):
        if similarities[i][j] > 0.85:
            duplicates.append((i, j))

# Summarization
openai.api_key = "your-api-key"
def summarize(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Rewrite the following JIRA ticket in a clean, concise way for developers:
{text}"}]
    )
    return response['choices'][0]['message']['content']

df['summary_cleaned'] = df['summary'].apply(summarize)
df.to_csv('data/triaged_output.csv', index=False)
print("Processed and saved triaged tickets.")
