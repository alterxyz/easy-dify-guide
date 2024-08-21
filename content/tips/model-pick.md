---
title: 'About Model Selection'
---

## Gemini

Thanks to the generous Google Cloud Platform, which provides a large usage quota.

Please note that for non-professional users, it's recommended to use Google's Gemini model rather than Vertex AI.

> Vertex AI is a complex professional platform. For local execution, you even need to install gcloud, and to use it on Dify, you need a Service Account Key in base64 format.
>
> If you really want to try it and aren't afraid of errors or can manually resolve issues, then you're welcome to experiment!
>
> Google will provide you with a json file, but Dify requires input in base64 format.
>
> I previously created a simple Python script to execute this conversion. Brave souls are welcome to use this stepping stone I've created to boldly try. [tools\key1ToBase64.py](https://github.com/alterxyz/easy-dify-guide/blob/main/tools/key1ToBase64.py)

## Llama 3.1

Llama is a top-tier open-source model from Meta. When you choose it, you might get some strange content.

- This is not Dify's problem; content generation is determined by the model.
- It's also not Llama's problem; this is a feature.

Llama is like a baby, it knows nothing, so it's best to:

- Specify the output language
- Provide clear requirements
- Provide examples
- Or use COT - Chain of Thought

In other words, Llama 3.1 is indeed very powerful, but it almost certainly needs prompt engineering.

> In fact, in the paper published by Meta about Llama 3.1's effects and scores, the Llama team used techniques like few-shot learning and COT.

In contrast, the currently best-performing closed-source model series is **Claude**, which can be said to have used prompts in advance, **so of course the results are good**. (personal understanding)

> "We tried to give Claude traits" [Claude's Character \ Anthropic](https://www.anthropic.com/news/claude-character)
