---
name: hirokazu-kore-eda
title: 是枝裕和 Hirokazu Kore-eda
style_file: ../directors/hirokazu-kore-eda.md
---

## 风格锚点
Cinematic film still, Japanese observational family drama, camera at human height slightly farther back, fixed, a doorway or corridor edge cutting the room into unequal parts, family members each occupying a separate patch of the same frame, natural window light with shadow allowed in the corners, low warm desaturated color shifting with the season, an old wooden table, bowls, a drying pole, worn walls, 1.85:1, quiet, unjudging, unresolved.

## 图像提示
- 主体 / 场景：a family eating noodles under the eaves; a grandmother and grandson in a cluttered kitchen; a child waiting alone at a doorstep; clothes hanging on a drying pole.
- 景别 / 构图：medium and full shot holding the family in one frame; a door frame, corridor or table divides the space naturally; no symmetrical centerpiece; close-up only for hands and objects.
- 镜头 / 焦段：35–50mm at human height, slightly distant, static.
- 光线：natural window light, interior shadows allowed, no fill.
- 色彩：low saturation and warm; seasonal — summer green dull and heavy, winter grey and pale.
- 材质：old wooden table, bowls and chopsticks, drying pole, worn wall, cheap fabric.
- 画幅：1.85:1.

## 视频提示
- 镜头运动（只选一种）：static at human height; at the emotional peak the camera retreats to the doorway and holds; never pushes in.
- 主体运动：cooking, eating, hanging laundry, a child running past; people exit frame and the room stays in shot past comfort.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no motion blur; cut after the action ends.

## 负面提示
no score telling the audience when to cry, no big close-up of weeping, no flashback explaining trauma, no theme sentence spoken during an argument, no dramatic reversal, no angelic children, no blood-line answer, no tidy conclusion about social services, no shot that enters a character's mind, no tatami-height camera used for nostalgia, no handheld, no shallow-focus tears, no warm filter.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
  - 色彩：low warm saturation, shifting with the season.
  - 镜头：35–50mm at human height, static, 1.85:1.
  - 光线：natural window light, shadows allowed.
  - 构图：door frame or corridor splits the space, family held in one frame, camera outside the room at the peak.
  - 材质：old wood, bowls, drying pole, worn wall.
- 禁止漂移：no score-driven emotion, no drone, no modern glass apartment, no LED white, no teal-and-orange, no close-up tears, no tatami-height drift.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 100`；写 `natural window light, domestic clutter, figures partly blocked by a door frame`；避免 `dramatic`、`emotional`。
- SDXL / ComfyUI：ControlNet depth 锁门框与走廊切分；低饱和暖调 LoRA；negative 写 `tears close-up, studio light, shallow bokeh, handheld`。
- Runway / Kling / Sora / Veo：固定人体高度机位，6–10 秒、24fps；人物出画后的空房间单独生成一条 hold；不做推近，不加入任何镜头运动。
