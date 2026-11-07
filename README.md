# 电影创作技能 film-creation

从想法到可拍/可生成的电影创作技能。它不是导演百科，也不是提示词模板库，而是一个工作台：先把戏写对、拍对，再用某位导演/摄影的眼睛约束它。

## 快速开始

在 Claude Code 里直接说：

- 「我想拍一个 5 分钟短片，只有一个房间和两个人，帮我发展故事」
- 「帮我写这个故事的 treatment，检查结构」
- 「这场餐厅对峙怎么调度，给我走位和分镜」
- 「这场戏演员应该做什么，给我可执行的指令」
- 「用王家卫 × 卢贝兹基，写雨夜便利店的中景和 5 秒视频提示」

技能入口：`.claude/skills/film-creation/SKILL.md`

## 三层

1. **方法层（craft）**：故事、视觉、调度、表演、声音、制作
2. **风格层（style）**：125 位导演 + 29 位摄影指导
3. **输出层（output）**：treatment、scene card、shot list、AI prompt

核心原则：**先有戏，再有风格**。导演风格是约束，不是内容。

## 工作流

```
诊断 → 故事 spine → 视觉系统 → 调度与表演 → 声音 → 风格层 → 输出 → 自检
```

1. **诊断**：形式、时长、预算、场景、演员、平台、交付物
2. **故事 spine**：logline、theme、character、structure、scene goal/turn
3. **视觉系统**：景别、构图、焦段、光线、色彩、材质
4. **调度与表演**：走位、机位、运动、覆盖、演员 action
5. **声音**：环境声、音乐、沉默、旁白
6. **风格层**：选 1 位导演 + 0–1 位摄影，应用约束
7. **输出**：treatment / scene card / shot list / AI prompt
8. **自检**：craft checklist + 导演反向约束 + 提示词检查

## 六个方法模块

| 模块 | 解决什么 |
|---|---|
| `story` | 写什么、怎么结构、场景怎么转 |
| `visual` | 怎么看见：景别、构图、焦段、光、色、材质 |
| `staging` | 怎么走位、怎么覆盖、摄影机怎么动 |
| `performance` | 演员做什么、怎么排练、怎么给指令 |
| `sound` | 听见什么：透视、画外、沉默、音乐 |
| `production` | 能不能拍、怎么排期、怎么省钱 |

模块在 `references/craft/`，每篇 2000–3000 字，含核心方法、8–12 条规则、检查清单、常见错误、练习，以及与风格层的接口。

## 风格层

- **125 位导演**：八节风格约束 + 视觉配方 + AI 提示
- **29 位摄影指导**：视觉观、光线与色彩、时间与运动、制作条件 + AI 提示

用法：

- 按核心命题选导演，不按题材选
- 导演决定内容与时间，摄影决定光与镜头
- 冲突时导演优先
- 混搭规则见 `references/mixing.md`

## 输出模板

- `templates/treatment.md` — 一页纸
- `templates/scene-card.md` — 单场戏
- `templates/shot-list.md` — 分镜表
- `templates/ai-prompt.md` — AI 提示卡
- `templates/style-brief.md` — 剧本/现场执行卡

## 目录结构

```
.claude/skills/film-creation/
  SKILL.md
  references/
    craft/                  6 个创作方法模块
    index.md                125 导演 + 29 摄影总表
    taxonomy.md             风格族谱
    mixing.md               混搭 + 导演 × 摄影
    prompting.md            档案 → prompt 的转换规则
    directors/<slug>.md     125 份导演档案
    prompts/<slug>.md       125 份导演提示
    cinematographers/<slug>.md       29 份摄影档案
    prompts-cinematographers/<slug>.md 29 份摄影提示
  templates/
    treatment.md
    scene-card.md
    shot-list.md
    ai-prompt.md
    style-brief.md
DESIGN.md                   设计说明
CRAFT_BRIEF.md              方法模块简报
DP_BRIEF.md                 摄影指导层简报
tools/                      索引、结构/视觉/提示/重复度检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写，再生成对应提示文件
- 新增摄影：按 `DP_BRIEF.md` 的 14 节结构
- 调整方法模块：读 `CRAFT_BRIEF.md`，每篇 2000–3000 字

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 18 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- 视觉参考以 [film-grab.com](https://film-grab.com/) 为主；未收录时用 MUBI / Criterion Channel 等可核验页面补充。只链接，不下载、不嵌入图片。
- 提示词不写画幅；画幅由用户/平台设定。

## License

MIT © 2026 Ethan
