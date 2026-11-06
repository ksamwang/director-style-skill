---
name: glauber-rocha
title: 格劳贝尔·罗查 Glauber Rocha
style_file: ../directors/glauber-rocha.md
---

## 风格锚点
Cinematic film still, brutal overhead sun with no fill on the face, low camera near the ground looking up so the figure cuts into a huge white sky, 25–35mm wide angle, high-contrast black and white or earth-yellow, blood-red and indigo, dry earth, rock, dead tree, dust, sweat, coarse cloth, handheld frame with aggressive energy, 1.85:1, mythic, hungry, confrontational.

## 图像提示
- 主体 / 场景：a peasant or bandit standing against a white sky; a crowd in a village square; a corpse on dry ground seen from above; a preacher addressing the camera directly.
- 景别 / 构图：medium wide and wide, figure treated as a monument; sky and land take most of the frame, the person is small but not weak; low angle, subject pressing into the horizon.
- 镜头 / 焦段：25–35mm wide, person and land pulled into the same frame; no telephoto isolation.
- 光线：harsh sun, no fill, face allowed to burn out; soft light only for the interior of the powerful.
- 色彩：high-contrast black and white by default; color passages use earth yellow, blood red, indigo.
- 材质：dust, sweat, blood, coarse cloth, dry stone, dead wood, film grain.
- 画幅：1.85:1; 2.35:1 for wide-screen passages.

## 视频提示
- 镜头运动（只选一种）：aggressive handheld push-in toward a face, camera as agitator, never a neutral observer.
- 主体运动：a crowd pressing forward, a speaker turning to the lens, a figure walking against the wind; gestures theatrical and declarative.
- 时长 / 帧率 / 运动模糊：3–6 seconds, 24fps, harsh motion; sudden zoom or cut rather than a smooth move.

## 负面提示
no soft light, no pretty poverty, no smooth continuity editing, no psychological flashback, no neutral observer camera, no clean studio set, no folk culture as decoration, no reconciled final shot, no gentle golden-hour grade.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：monochrome high contrast or earth yellow, blood red, indigo.
- 镜头：25–35mm, low and wide, 1.85:1 (2.35:1 wide passages).
- 光线：overhead sun, no fill, burned-out highlights.
- 构图：sky and land dominate, figure cuts the horizon.
- 材质：dust, sweat, blood, coarse cloth, dry earth, grain.
- 禁止漂移：no drone aerials, no soft-focus humanism, no clean digital color, no modern city, no passive victim framing.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 100`；黑白段落直接写 `high-contrast black and white`，避免默认彩色。
- SDXL / ComfyUI：固定 prompt 块 + 粗颗粒 LoRA；ControlNet depth 锁低机位仰拍与大面积天空。
- Runway / Kling / Sora / Veo：首帧图 + 只写 handheld push-in 或 sudden zoom，3–6 秒、24fps；不要平滑运镜。
