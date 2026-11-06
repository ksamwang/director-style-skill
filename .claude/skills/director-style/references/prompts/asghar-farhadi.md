---
name: asghar-farhadi
title: 阿斯哈·法哈蒂 Asghar Farhadi
style_file: ../directors/asghar-farhadi.md
---

## 风格锚点
Cinematic film still, Iranian domestic moral drama, 1.85:1, 35–50mm handheld at eye level, crowded interior framing split by a doorway, two people over-the-shoulder in a small apartment, plain available daylight and ceiling bulb, beige and grey walls, kitchen tile, paperwork, perspiration, no score.

## 图像提示
- 主体 / 场景：a husband and wife arguing across a kitchen table while a third person stands in the doorway; a driver holding documents in a parked car; a mother at a sink, listening to the argument through the wall.
- 景别 / 构图：medium close and medium, crowded; doorframe divides who is inside, who is outside, who speaks through the door; over-the-shoulder two-shots; furniture and people block each other; no clean negative space.
- 镜头 / 焦段：35–50mm, close enough to see hesitation, wide enough to see who stands behind whom.
- 光线：interior natural light and a bare ceiling bulb; no shaping, no rim light, no motivated glow.
- 色彩：plain ungraded natural — beige, grey, old wood, faded paint.
- 材质：peeling rental wall, kitchen tile, plastic bag, stacked paper, thin door, worn upholstery.
- 画幅：1.85:1.

## 视频提示
- 镜头运动（只选一种）：handheld follow that changes sides as the argument shifts; it locks off when a lie lands or when the scene empties into a corridor.
- 主体运动：walking through a doorway, sitting down hard, turning toward a new speaker, hands busy with an object; realistic overlap and interruption.
- 时长 / 帧率 / 运动模糊：real time, 10–20 seconds, 24fps, slight natural shake, no stylized blur.

## 负面提示
no clear villain, no score guiding sympathy, no flashbacks explaining the past, no courtroom-debate spectacle, no character stating the theme, no beautiful composition, no argument that resolves anything, no handheld-plus-shouting festival formula, no high-style grading, no symmetrical family portrait.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：plain beige-grey natural palette, 35–50mm, 1.85:1; available daylight plus ceiling bulb, no shaping; doorframe splits the frame, crowded over-shoulder two-shots; peeling wall, tile, plastic bag, paper, thin door.
- 禁止漂移：no teal-orange grade, no shallow-focus bokeh portrait, no symmetrical staging, no dolly moves, no glossy middle-class advertising interior, no drone.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 50`；写 `cramped apartment, doorway in foreground`；不要用高电影感 `--sref`，会把画面美化。
- SDXL / ComfyUI：ControlNet depth 锁门框与过肩关系；避免浅景深 LoRA；negative 单独压 `cinematic lighting, bokeh, symmetrical`。
- Runway / Kling / Sora / Veo：首帧给门框分割的双人构图，运动只写 `handheld follow, camera changes sides`；10–20 秒、24fps；结尾走廊另起一段 `static` 镜头，不混在同一段。
