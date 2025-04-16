from openai import OpenAI
client = OpenAI()

def get_sentiment(text: list) -> list:
    """
    Takes a list of customer review strings and returns a list of sentiment labels
    using the gpt-4o-mini model. Each label will be one of:
    "positive", "neutral", "negative", or "irrelevant".

    Returns "Wrong input. text must be an array of strings." if the input is invalid.
    """
    
    # Check if text is not a list, is empty, or has anything that’s not a string
    if not text or type(text) != list or any(type(item) != str for item in text):
        return "Wrong input. text must be an array of strings."

    # Join the reviews with new lines
    formatted_text = "\n".join(text)
    
    system_prompt = """
    You are an expert in interpreting human sentiment across cultures.
    Label each of the following product reviews with one word:
    positive, neutral, negative, or irrelevant.
    Only one word per line, matching the order of the reviews.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {formatted_text}
    """
    # Call the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    # Get the response text and clean it
    response_text = completion.choices[0].message.content.strip()

    # Convert the response to a list by splitting at new lines and stripping spaces
    sentiments = [line.strip() for line in response_text.split("\n") if line.strip()]

    return sentiments

