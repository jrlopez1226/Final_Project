import openai
import fetchnew

# New OpenAI client usage (v1+)
client = openai.OpenAI(api_key="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")

def summarize_articles(articles):
    summaries = []

    for i, article in enumerate(articles):
        prompt = f"Summarize the following article in 3-4 concise bullet points suitable for a daily news email:\n\n{article}"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )

        summary = response.choices[0].message.content
        summaries.append(summary)

    return summaries

if __name__ == "__main__":
    raw_articles = fetchnew.fetch_news()
    summarized = summarize_articles(raw_articles)

    for i, summary in enumerate(summarized, 1):
        print(f"\n📌 Summary {i}:\n{summary}")
