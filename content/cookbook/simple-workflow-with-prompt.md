---
title: 'Simple Workflow with Prompt engineering'
---

Video: [Simple Workflow with Prompt engineering](https://youtu.be/oLHmUPYkDGI)

## Important

### Model Selection

Llama need more prompt engineering, such as more examples.

In real using, I replace `Llama` with `command-r-plus`. Also if you would like to spend a little more money, you can try `Claude 3.5 Sonnect`.

### Length

Context length is not the only thing you need to consider. The `Max Tokens` refers to the max lenght LLM can speak.

In chat or chatflow, we can say "continue", but in workflow we can't.

We better set both input variables to 1800:

> input1 + input2 + prompt <= 4096 (command-r-plus)

## Key concepts

### RESTful API

The key part is "stateless". LLM won't know who you are, or whatever you said before.

So everytime what Dify does send out all your chat history again and again whenever you use LLM.

**Don't worry, it's automatic handled by Dify.**

### Context Length

"context length" is the amount that limit the total length of that "chat history".

For workflow, it can be more strightforward:

My content has 3 parts:

- prompt
- eng_content
- zh_content

The model has 1 information we need, such as:

- Llama-3.1-70b-versatile LLM CHAT `131K`
- command-r-plus LLM CHAT `128K`

"K" stands for "thousand".

So it turns out simpily:

`prompt + eng_content + zh_content <= 131,000`

So I picked both input variables to 50000.

However that is not a good practice, see [Important](#important).

### Max Tokens

Refers to the max lenght LLM can speak.

In chat or chatflow, we can say "continue", but in workflow we can't.

---

**Basiclly that's all!**

Congrats you know what the `context length` / `context window` / `context size` is.
