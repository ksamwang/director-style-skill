---
name: film-creation
description: 从想法到可拍/可生成的电影创作技能。用于发展故事、写 treatment、设计场面调度、写分镜、指导表演、设计声音，或把场景转成 AI 图像/视频提示；内置 6 个创作方法模块与 125 位导演 + 29 位摄影指导的风格约束。
---

# 电影创作技能

不是风格库，是创作工作台。

## 三层

1. **方法层（craft）**：story / visual / staging / performance / sound / production
2. **风格层（style）**：125 位导演 + 29 位摄影指导
3. **输出层（output）**：treatment / scene card / shot list / AI prompt

核心原则：**先有戏，再有风格**。导演风格是约束，不是内容。

## 工作流

### 0. 诊断

先确认：

- 形式：短片 / 长片 / 广告 / MV / AI 视频
- 时长、预算、场景、演员、周期
- 交付物：treatment / 分镜 / 成片 / 图像 / 视频
- 平台：实拍 / Midjourney / SDXL / Runway / Kling / Sora / Veo

### 1. 故事 spine

读 `references/craft/story.md`。

输出：logline、theme、character（want / need / flaw）、structure、scene goal / turn。

### 2. 视觉系统

读 `references/craft/visual.md`。

输出：景别策略、构图、焦段、光线、色彩、材质。

### 3. 调度与表演

读 `references/craft/staging.md` 与 `references/craft/performance.md`。

输出：走位、机位、运动、覆盖、演员 action。

### 4. 声音

读 `references/craft/sound.md`。

输出：环境声、音乐、沉默、旁白。

### 5. 风格层（可选，但推荐）

读 `references/index.md`，选 1 位导演 + 0–1 位摄影指导。

- 导演：`references/directors/<slug>.md` + `references/prompts/<slug>.md`
- 摄影：`references/cinematographers/<slug>.md` + `references/prompts-cinematographers/<slug>.md`
- 规则：导演风格不改变故事 spine；冲突时故事优先。
- 混搭与导演 × 摄影：`references/mixing.md`

### 6. 输出

按需选择模板：

- `templates/treatment.md` — 一页纸
- `templates/scene-card.md` — 单场戏
- `templates/shot-list.md` — 分镜表
- `templates/ai-prompt.md` — AI 提示卡
- `templates/style-brief.md` — 剧本/现场执行卡

### 7. 自检

- 故事：场景是否有目标 / 冲突 / 转折
- 视觉：每个镜头是否有理由
- 调度：轴线、屏幕方向、覆盖是否成立
- 表演：指令是否是可演的 action
- 声音：是否有沉默与画外
- 风格：反向约束是否逐条通过
- 提示：是否残留 `--ar` 或画幅比例（不应有；画幅由用户/平台设定）

## 风格层怎么用

1. **按命题选，不按题材选**：读 `references/index.md` 的一句签名与签名层。
2. **导演决定内容与时间**：命题、人物关系、表演、剪辑结构。
3. **摄影决定光与镜头**：光线、色彩、焦段、运动、格式。
4. **冲突时导演优先**；摄影不改变核心命题。
5. **不要把两位导演的名字堆进 prompt**；用视觉基元，模型更稳。

## 输出原则

- 先写“这场戏要发生什么”，再写“怎么拍”。
- 每条视觉选择都要能回答“为什么这场戏需要它”。
- 提示词里不写画幅；画幅由用户/平台设定。
- AI 提示的图像与视频分开写；视频只给一种运镜。
- 负面提示从导演的反向约束与误读警告转写，不用通用套话。

## 文件导航

- `references/craft/` — 6 个创作方法模块
- `references/index.md` — 125 位导演 + 29 位摄影指导总表
- `references/directors/<slug>.md` — 导演风格档案
- `references/prompts/<slug>.md` — 导演 AI 提示
- `references/cinematographers/<slug>.md` — 摄影指导档案
- `references/prompts-cinematographers/<slug>.md` — 摄影 AI 提示
- `references/taxonomy.md` — 风格族谱与近亲替代
- `references/mixing.md` — 风格混搭 + 导演 × 摄影
- `references/prompting.md` — 从档案到 prompt 的转换规则
- `templates/` — treatment / scene card / shot list / AI prompt / style brief
- `../../../DESIGN.md` — 设计说明
