# 从导演档案到 AI 提示

> 这一层不解释电影，只把档案转成模型能执行的视觉指令。

## 三层结构

1. **风格锚点**：一段式英文，40–80 词，放在所有 prompt 开头。
2. **镜头提示**：图像与视频分开写；图像管构图/光/色，视频管运动/时间。
3. **负面提示 + 一致性锚点**：防止模型滑回通用审美，防止跨镜头漂移。

## 从「视觉规则」提取

| 档案维度 | Prompt 语言 |
|---|---|
| 景别 | extreme wide / wide / medium / medium close-up / close-up / extreme close-up |
| 构图 | centered / off-center / frame-within-frame / foreground obstruction / negative space |
| 空间 | deep space / flat space / claustrophobic / open landscape |
| 色彩 | specific hues + saturation + contrast（例：saturated emerald green and deep red, low-key） |
| 光线 | source（neon / tungsten / window / overcast）+ direction + hardness + ratio |
| 材质 | film grain / smoke / rain / dust / silk / concrete / cheap wallpaper |
| 画幅 | 1.37:1 / 1.66:1 / 1.85:1 / 2.39:1 / 4:3 / 16:9 |

## 从「镜头语法」提取

- **机位**：eye level / low angle / high angle / overhead；distance to subject。
- **焦段**：18mm / 24mm / 35mm / 50mm / 85mm / 135mm；wide-angle distortion or compression。
- **运动**：static / handheld drift / dolly in / track / crane / whip pan / follow。
- **何时动**：only when the subject moves / only at the reveal / never。
- **权力**：who is followed, who is left out of frame, who occupies the center。

## 从「反向约束」提取负面提示

每条禁令转成一个 negative token，不要照抄中文：

- 不要均匀补光 → `no even studio lighting, no fill light`
- 不要对称构图 → `no symmetrical composition, no centered framing`
- 不要慢镜三件套 → `no slow-motion cliché, no neon montage, no voice-over`
- 不要干净数字感 → `no clean digital sharpness, no HDR, no modern glass architecture`
- 不要暖色怀旧滤镜 → `no warm nostalgia filter, no sepia`

## 一致性锚点

跨镜头生成时，锁住五件事：

1. **色彩**：3–5 个色相 + 饱和度 + 对比度。
2. **镜头**：一个主焦段 + 一个画幅。
3. **光线**：一个主光源 + 光比。
4. **构图**：机位高度 + 前景习惯。
5. **材质**：胶片/颗粒/烟雾/雨/织物。

再加一条**禁止漂移**：模型最容易加进来的现代元素（玻璃幕墙、LED 白光、无人机航拍、干净数字皮肤）。

## 平台适配

### Midjourney

- 用 `--ar` 锁画幅，`--style raw` 降低默认美化，`--stylize` 控制风格强度。
- 风格锚点放最前，主体放中间，技术参数放最后。
- 需要跨图一致时，用 `--sref` 或参考图，不要只靠文字。

### SDXL / ComfyUI

- positive 与 negative 分开；风格锚点做成固定 prompt 片段或 LoRA。
- 构图用 ControlNet（depth / canny / pose）；色彩用 IP-Adapter 或 palette 参考。
- 固定 seed 只保证单模型内一致，跨模型仍要靠参考图。

### Runway / Kling / Sora / Veo

- 先给首帧图像，再写运动；不要用一段文字同时描述画面和运动。
- 镜头运动只写一种：`slow dolly in` / `handheld follow` / `static`；不要叠加三种。
- 时长、帧率、运动模糊分开写；模型对“慢”与“快”的理解不一致，用具体秒数。
- 角色一致性优先用参考图/角色 ID，不靠形容词。

## 混搭

- 命题唯一：主风格的世界观不让。
- 最多借两层，且不能碰签名层。
- 在 prompt 里，冲突会表现为矛盾的光线、色彩或运动；按主风格签名层优先。
- 不要把两位导演的名字直接堆在一起；用视觉基元，模型更稳。
- 如果平台屏蔽导演名，删掉名字，只留基元。

## 反模仿

- 不要只写 “Wong Kar-wai style”。模型会给你霓虹 + 慢镜 + 独白的通用拼贴。
- 每个 prompt 至少一个**只属于该导演**的约束：一个机位、一个光源、一个材质、一个剪辑/运动规则。
- 用「误读警告」做 negative prompt 的第一行。
