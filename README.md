# 导演风格技能包

100 位导演的可执行风格约束，主用途是 **AI 图像 / 视频生成**。它不是影评库，而是把“某位导演的画面”拆成模型能执行的 prompt、镜头运动和负面约束。

## 快速开始

在 Claude Code 里直接说：

- 「用王家卫的风格生成一张雨夜便利店的中景」
- 「布列松 × 塔可夫斯基，写一段 5 秒视频提示：一个人走过走廊」
- 「这段画面太像通用赛博朋克，用杜琪峰的站位和冷蓝改一版」
- 「给我三个适合这段材料的导演，说明画面差异」

技能入口：`.claude/skills/director-style/SKILL.md`

## 每位导演的三层内容

### 1. 八节风格约束

1. 核心命题：他反复拍什么矛盾？不是题材，是他对人的基本看法。
2. 人物关系：主角是谁、想要什么、与家庭/社会/权力是什么关系。
3. 视觉规则：景别、构图、空间、色彩、光线、材质怎么选。
4. 镜头语法：摄影机何时静止、移动、靠近、保持距离；谁被跟、谁被留在画外。
5. 表演与对白：外放还是克制；对白自然、文学化还是碎片化。
6. 时间与剪辑：长镜头还是快切；跳时、重复、分章；哪里停顿。
7. 声音规则：音乐、环境声、沉默、旁白各承担什么。
8. 反向约束：哪些做法会破坏这个风格；哪些刻板印象必须避免。

### 2. 视觉配方

画幅、镜头/焦段、机位与运动、色彩、光线、材质/美术、构图。每项都是具体参数或选择，不是形容词。

### 3. AI 提示文件

`references/prompts/<slug>.md`：

- 风格锚点（英文，40–80 词）
- 图像提示基元（主体、景别、构图、镜头、光线、色彩、材质、画幅）
- 视频提示基元（镜头运动、主体运动、时长、帧率、运动模糊）
- 负面提示（从「反向约束」逐条转成英文）
- 一致性锚点（色彩、镜头、光线、构图、材质 + 禁止漂移）
- 平台备注（Midjourney / SDXL / ComfyUI / Runway / Kling / Sora / Veo）

## 目录结构

```
.claude/skills/director-style/
  SKILL.md                  触发条件 + AI-first 工作流 + 自检
  references/
    index.md                100 人总表（地域/风格族/签名层/一句签名/提示入口）
    taxonomy.md             12 个风格族 + 近亲替代规则
    mixing.md               混搭协议
    prompting.md            从档案到 prompt 的转换规则与平台适配
    directors/<slug>.md     100 份风格档案
    prompts/<slug>.md       100 份 AI 提示基元
  templates/
    ai-prompt.md            AI 生成提示卡
    style-brief.md          剧本/分镜执行卡
    director-entry.md       新增导演的空白模板
DESIGN.md                   设计说明与写作标准
AGENT_BRIEF.md              批量写作简报
VISUAL_BRIEF.md             视觉扩写简报
REVIEW_BRIEF.md             审校清单
tools/                      索引生成、结构/视觉/重复度检查、规范化
```

## AI 生成工作流

1. **明确镜头**：主体、场景、动作、景别、画幅、时长、平台、是否需要跨镜头一致性。
2. **选主风格**：按核心命题 + 视觉族选，不按题材选。
3. **读两份文件**：`directors/<slug>.md` 与 `prompts/<slug>.md`。
4. **写提示卡**：风格锚点 → 图像提示 → 视频提示 → 负面提示 → 一致性锚点 → 平台备注。
5. **自检**：是否只写了导演名字？是否有只属于该导演的约束？图像与视频是否分开？负面提示是否来自反向约束？跨镜头是否锁住色彩/镜头/光线/构图/材质？

完整转换规则见 `references/prompting.md`，输出模板见 `templates/ai-prompt.md`。

## 剧本 / 分镜用法

1. 按核心命题选主风格，读对应档案。
2. 按 `templates/style-brief.md` 填：机位、运动、剪辑点、声音、表演调度。
3. 自检：命题是否落地；反向约束是否逐条通过。

## 混搭

1. **命题唯一**：主风格的世界观不让；副风格只提供形式策略。
2. **签名层不让**：每条档案标注 1–2 个签名层，副风格只能改非签名层。
3. **最多借两层**：并写明为什么这两层不打架。

完整规则见 `references/mixing.md`；在 prompt 里，冲突会表现为矛盾的光线、色彩或运动，按主风格签名层优先。

## 质量原则

- 先命题，后视觉。没有命题的视觉只是滤镜。
- 一个签名，不是一套符号。
- 反向约束优先：negative prompt 比 positive 更能保住风格。
- 同族之间必须写出“他和最近亲的那位差在哪”。

## 扩展

新增一位导演：

1. 复制 `templates/director-entry.md` 到 `references/directors/<slug>.md`，按八节填写。
2. 从档案生成 `references/prompts/<slug>.md`，按 `templates/ai-prompt.md` 的结构。
3. 跑 `python tools/check_structure.py`、`python tools/check_visual.py`、`python tools/check_duplicates.py`。
4. 跑 `python tools/build_index.py` 重新生成总表。

全局复用：把 `.claude/skills/director-style/` 整个复制到 `~/.claude/skills/director-style/`。

## 数据来源与边界

- 档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- 视觉参考链接指向 [film-grab.com](https://film-grab.com/) 的静帧页面；只链接，不下载、不嵌入图片。
- 不确定的影片年份或链接标“待核验”。
