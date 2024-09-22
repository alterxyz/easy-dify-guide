---
title: 'Cookbook Index'
weight: 1
---

`Hello, Dify!`

> {{% badge style="red" icon="user-secret" %}}Hack{{% /badge %}}
> are some hack solution that may help you better use Dify.
>
> And they **might** be supported by Dify officially in the future.

---

## Quick Guide

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Instructions{{% /badge %}}

### How to download the DSL file?

![How_to_download_from_GitHub](https://raw.githubusercontent.com/alterxyz/easy-dify-guide/main/static/images/how_download.gif)

### How to copy the prompt?

![How_to_copy_prompt](https://raw.githubusercontent.com/alterxyz/easy-dify-guide/main/static/images/copy_prompt.gif)

---

## Checklist

{{% badge style="red" icon="user-secret" %}}Hack{{% /badge %}}
**You can leave some unused blocks without preventing you publish the app.**

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Checklist](https://github.com/alterxyz/easy-dify-cookbook/blob/main/hack/checklist.md)

---

## Conversation Variables

{{% badge style="red" icon="user-secret" %}}Hack{{% /badge %}}
**Allow you assign constant to the “Conversation Variable”.**

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Conversation Variable with Constant](https://github.com/alterxyz/easy-dify-cookbook/blob/main/hack/conversation%20variable%20with%20constant.md)

---

## Code block

{{% badge style="green" icon="bookmark" title="Level" %}}Beginner{{% /badge %}}
**Write or generate Python code in Dify !**

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Code block](https://github.com/alterxyz/easy-dify-cookbook/blob/main/example/001_code_block.md)

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Extra{{% /badge %}}
[Python Debug](https://github.com/alterxyz/easy-dify-cookbook/blob/main/example/001.1_code_block_python_debug.md)

{{% badge style="gray" icon="book-open" title="Cookbook" %}}DSL File{{% /badge %}}
[DSL](https://github.com/alterxyz/easy-dify-cookbook/blob/main/DSL/Your%20Code~.yml)

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Prompt{{% /badge %}}
[Prompt](https://github.com/alterxyz/easy-dify-cookbook/blob/main/prompt/code_generator.md)

{{% badge style="orange" icon="hand-sparkles" title="Demo" %}}Helper{{% /badge %}} [Code Generator](/demo/code_generator/)

---

## Code block with API

{{% badge style="blue" icon="bookmark" title="Level" %}}Intermediate{{% /badge %}}
**Alternative way to call your favorite API, Not "HTTP Request" or "Tools-Custom". More flexibility.**

### Code example

```python
# Python & Dify
import httpx
def main(auth_bearer: str) -> dict:
    url = "https://api.cloudflare.com/client/v4/accounts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_bearer}"
    }
    with httpx.Client() as client:
        response = client.get(url, headers=headers)

    data = response.json()
    result = []

    if data["success"] and "result" in data:
        for account in data["result"]:
            result.append({
                "id": account["id"],
                "name": account["name"]
            })

    return {"result": result}
```

---

## Dify Agent inside Chatflow or Workflow

{{% badge style="red" icon="user-secret" %}}Hack{{% /badge %}}
**Allow you to use Dify Agent inside Chatflow or Workflow, just like the "Workflow as tool" feature.**

This is a hack solution, not a official feature. Offical feature is coming soon.

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Dify Agent inside Chatflow or Workflow](https://github.com/alterxyz/easy-dify-cookbook/blob/main/hack/agent_in_workflow.md)

{{% badge style="tip" %}}Requirement{{% /badge %}}

I implemented with one-shot agent, so no history. I also implemented this with 1 input variable, you can either remove it, or use it, or add more of it.

**So modify code is required.**. However, you can try to use the code generator with the prompt I provided above, bring my code and the prompt, chat with some smart LLM like GPT-4o or Claude 3.5 Sonnet that help you modify the code.

![image](https://github.com/user-attachments/assets/2c80f051-4fe3-4ea8-a2a6-b3ad7be86088)

---

## Cloudflare KV for Persistent Storage

{{% badge style="blue" icon="bookmark" title="Level" %}}Intermediate{{% /badge %}}
**Example of using Cloudflare KV for persistent storage.**

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Cloudflare KV for Persistent Storage](https://github.com/alterxyz/easy-dify-cookbook/blob/main/example/002_cf_kv.md)

{{% badge style="gray" icon="book-open" title="Cookbook" %}}DSL File{{% /badge %}}
[DSL](https://github.com/alterxyz/easy-dify-cookbook/blob/main/DSL/Your%20Cloudflare%20KV.yml)

{{% badge style="orange" icon="hand-sparkles" title="Demo" %}}Helper{{% /badge %}}
[Get account_id by Cloudflare API](cookbook/demo/#code-generator)

---

## Better Personalized Memory Assistant

{{% badge style="red" icon="exclamation" title="Level" %}}Advance{{% /badge %}}

{{% badge style="gray" icon="book-open" title="Cookbook" %}}Detail{{% /badge %}}
[Personalized Memory Assistant](https://github.com/alterxyz/easy-dify-cookbook/blob/main/example/003_Real_Personalized%20Memory%20Assistant.md)

{{% badge style="gray" icon="book-open" title="Cookbook" %}}DSL File{{% /badge %}}
[DSL](https://github.com/alterxyz/easy-dify-cookbook/blob/main/DSL/Personalized%20Memory%20Assistant.yml)

{{% badge style="orange" icon="hand-sparkles" title="Demo" %}}Try this{{% /badge %}}
[Personalized Memory Assistant](/demo/better-personalized-memory-assistant/)

{{% badge style="red" icon="user-secret" %}}Hack{{% /badge %}}
**2024-09-22 Out of date, conversation variable can greatly reduce the complexity of this example.**

{{% badge style="tip" %}}Requirement{{% /badge %}}

- You will need an Cloudflare account.
- You must finished the [Cloudflare KV for Persistent Storage](cookbook/#cloudflare-kv-for-persistent-storage) first.

