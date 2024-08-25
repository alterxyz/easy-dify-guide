---
title: '模型选择'
tags: ['origin','model']
---

## Gemini

感谢慷慨的 Google Cloud Platform, 提供了很大的Gemini使用额度. <https://ai.google.dev/pricing>

对于非专业用户, 建议使用 Google's Gemini model, 而不是 Vertex AI.

> Vertex AI 是个复杂的专业平台, 在本地执行你需要安装 gcloud
>
> 而在 Dify 上使用你需要 Service Account Key in base64 format.
>
> 如果你一定要尝试, 不怕出错, 自己能手动解决, 那欢迎您尝试~
>
> 谷歌会提供给你一个 json 文件, 而 Dify 却要求输入 base64.
>
> 我过去创建了个简单的 python 小脚本用来执行, 欢迎勇敢者借助我做的这个垫脚石勇敢尝试. [tools\key1ToBase64.py](https://github.com/alterxyz/easy-dify-guide/blob/main/tools/key1ToBase64.py)
>
> 欢迎, 但不建议.

## Llama 3.1

Llama 是 Meta 开源的顶级模型. 当你选择它的时候, 可能你会获得一些奇怪的内容.

- 这可能不是 Dify 的问题, 内容的生成是由模型决定的.
- 这可能也不是 Llama 的问题, 这是一个特性.

Llama 像一个婴儿一样, 它什么也不知道, 所以你最好:

- 限定它输出的语言
- 提供明确的要求
- 提供例子
- 或使用 COT - Chain of Thought

换句话说, Llama 3.1 确实很强, 但是它需要 prompt engineering .

> 实际上, 在 Meta 发布关于 Llama 3.1 的论文中的效果和比分中, Llama 团队用了 few-shot learning 和 COT 等技术.

与之相反的, 是目前效果最好的闭源模型 **Claude** 系列, 它可以说是提前就使用了一遍 prompt, **那么效果当然好**. (个人理解)

> "We tried to give Claude traits" [Claude’s Character \ Anthropic](https://www.anthropic.com/news/claude-character)
