# 从档案到 token

> 档案是给人看的；token 是给模型看的。这一层只做转换。

## 输出顺序

```text
选导演/摄影 → 提取视觉 token → 组合资产 token → 镜头提示 → 视频提示
```

## token 块

```text
STYLE: ...
SUBJECT: {{character_token}} | {{action}}
ENVIRONMENT: {{scene_token}} | {{time}} | {{weather}}
SHOT: {{size}} | {{angle}} | {{lens}} | {{composition}}
LIGHT: ...
COLOR: ...
TEXTURE: ...
MOTION: ...
NEGATIVE: ...
```

## 从档案映射

| 档案字段 | 进入哪一块 |
|---|---|
| 视觉规则 | LIGHT / COLOR / TEXTURE / SHOT |
| 镜头语法 | SHOT / MOTION |
| 视觉配方 | STYLE / LIGHT / COLOR / TEXTURE |
| 反向约束 | NEGATIVE |
| 误读警告 | NEGATIVE 的第一行 |
| 核心命题 | 不进 prompt；用于选导演 |
| 同族差异 | 用于区分两位导演的 token |

## 组合规则

1. **一个提示一个主语**：人物、场景、物品分开生成。
2. **资产 token 逐字复用**：同一角色/场景不改写。
3. **文字只写变化**：动作、景别、机位、光线变化；身份和场景不重复。
4. **图像与运动分离**：视频提示只写运动。
5. **不写画幅**：画幅由用户/工具设定。
6. **不写导演名**：用视觉基元。

## 检查

见 `references/aigc/prompt-syntax.md` 的「出图前检查」。
