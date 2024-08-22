---
title: '"工具"'
tags: ['tools']
---

## 关于工具

在 Discord 群中, 很多的问题都是围绕"工具"展开的.

<https://cloud.dify.ai/tools>

我可以透露的是, "工具"正在进行一次格式和生态的调整.

这里有几个建议带给大家:

### 未来

未来可能会有更清晰和更简单的"工具"的开发, 以及可能会有"工具商店"之类的出现.

### 现在

#### 工作流

我们的工作流"发布为工具"是个潜力巨大的功能, 我将在 Cookbook 带头示范 😁.

一些能用 jinjia2, httpx, requests, 以及其他 python3.10 自带库就能解决了的事情, 很建议"工作流发布为工具".

- [ ] 我将做一个 Cookbook, 用工具流实现一个永久存储的功能
- [ ] 我也将讲解 Code Block (主要 python)的一些特性
- [ ] 我将开源一个 prompt, 用于生成 Code Block 里的代码

#### 内置工具

"内置工具"的开发其实比较复杂, 以及官方目前的说明书有些混乱和零散 - 虽然能提供足够的信息, 但是东一榔头, 西一棒子...

这里既是劝退, 也是给有需要的一个简单的指路:

1. 需要你了解工具代码的格式规范 <https://docs.dify.ai/v/zh-hans/guides/gong-ju/quick-tool-integration>
2. 代码完成后, 在 Docker 里启动是不行的, 你需要[本地源码启动](https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted/local-source-code)
    1. 你可以跳过前端页面部署, 改而[直接 docker 前端](https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted/start-the-frontend-docker-container)
3. 提交 PR, 等待审核
4. 在新版本更新时, 你的工具可能会被合并进去.
5. 如果能顺利地合并进 Dify 的主代码仓库中, 那么恭喜! 你的工具终于可以用了.

- 代码是 python
- 你的变量等参数配置要手动选好
- 目前没有给提供详细说明书的渠道.
- 工具提供了丰富的脚手架, 比如 summary. 但是它们可能涉及到调用"系统推理模型".
    - 不同的模型会带来不同的效果, 有时候是不安全的.
    - 比如"系统推理模型"欠费或者被停用了, 这个工具很可能会报错.

下面简单提供一点代码的[示例](https://docs.dify.ai/v/zh-hans/guides/gong-ju/quick-tool-integration#id-4.-zhun-bei-gong-ju-dai-ma):

```python
from core.tools.entities.tool_entities import ToolInvokeMessage, ToolProviderType
from core.tools.tool.tool import Tool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError

from core.tools.provider.builtin.google.tools.google_search import GoogleSearchTool

from typing import Any, Dict

class GoogleProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        try:
            # 1. 此处需要使用 GoogleSearchTool()实例化一个 GoogleSearchTool，它会自动加载 GoogleSearchTool 的 yaml 配置，但是此时它内部没有凭据信息
            # 2. 随后需要使用 fork_tool_runtime 方法，将当前的凭据信息传递给 GoogleSearchTool
            # 3. 最后 invoke 即可，参数需要根据 GoogleSearchTool 的 yaml 中配置的参数规则进行传递
            GoogleSearchTool().fork_tool_runtime(
                meta={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_paramters={
                    "query": "test",
                    "result_type": "link"
                },
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
```

您写出来的代码, 会是这个样子的 👆

---

**如果您需要新的依赖库的安装, 那您确实会仍然需要进行"工具"的开发和代码的提交.**

心动不如行动.
