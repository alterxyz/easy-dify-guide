---
title: 'Dify API Key'
tags: ['original', 'api']
---

## Summary

Dify API Keys are uniquely assigned to individual applications (APPs), not to your Dify account or LLM models.

## Key Points

{{% notice style="cyan" title="Key Point 1" icon="book-open" %}}
**If you have 10 Dify APPs and use the API for all of them, you will need at least 10 distinct Dify API Keys.**
{{% /notice %}}

{{% notice style="cyan" title="Key Point 2" icon="book-open" %}}
**An API Key generated for APP-X will not work for APP-Y, even if they are under the same Dify account.**
{{% /notice %}}

## Detailed Explanation and Analogy

{{% expand title="View details..." %}}

Consider this scenario:

You're using OpenAI and obtain your API Key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).

You set up two different SYSTEM prompts in the [**PLAYGROUND**](https://platform.openai.com/playground/chat?lang=python&models=gpt-4o):

1. One that instructs GPT to act like a cat
2. Another that instructs GPT to act like a dog

By clicking the {{% icon code %}}, you receive two Python code snippets - one for the cat behavior and one for the dog behavior.

A sample code might look like this:

```python
from openai import OpenAI
client = OpenAI(api_key="your_api_key_here")

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "I need you to reply like a cat"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)
```

You create two local Python files: `cat_simulator.py` and `dog_simulator.py`.

You can run these files in the terminal using `python cat_simulator.py` and `python dog_simulator.py`, or execute them in your preferred environment.

### Key Components

This project has three crucial elements:

1. "your_api_key_here" - The API Key that grants access to the models.
2. "cat_simulator" - Represents a Dify APP "A".
3. "dog_simulator" - Represents a Dify APP "B".

A Dify APP is constructed using both your LLM provider's model and your custom workflow, creating a combination like: `cat_simulator&your_api_key_here`.

After clicking `Create new Secret Key`, you receive an "API Secret key", let's call it `Dify-API-Key-A`.

Similarly, you can have `dog_simulator&your_api_key_here`, and `Dify-API-Key-B`.

### {{% icon circle-question %}} When using the API with "Dify-API-Key-A", will it interact with the "dog_simulator"?

{{% notice style="cyan" title="Answer" icon="magnifying-glass" %}}
No, it will not.

To access APP "B" for dog-like responses, you must use "Dify-API-Key-B", which requires a **separate** Dify API Key.
{{% /notice %}}

{{% /expand %}}
