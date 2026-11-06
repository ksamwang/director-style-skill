---
name: park-chan-wook
title: 朴赞郁 Park Chan-wook
style_file: ../directors/park-chan-wook.md
---

## 风格锚点
Cinematic film still, jewel-toned baroque thriller, saturated crimson, emerald, violet and gold, one-point perspective symmetry, subject pinned on the geometric axis of a corridor or doorway, 35–85mm compression, hard-edged practical light, half the face cut away, velvet and lacquered wood, elegant menace.

## 图像提示
- 主体 / 场景：a man in a tailored suit standing at the exact center of a long hotel corridor; a woman in an emerald dress at the far end of a tiled hall, wallpaper pattern readable; a hand being washed at a sink before an act.
- 景别 / 构图：medium to medium close-up; the designer of the scene gets the full symmetrical wide, the person being designed gets the halved face close-up; one-point perspective, centered on the axis, doorway and corridor as frame; subject off-axis only when power is lost.
- 镜头 / 焦段：35–85mm, compressed foreground and background so the two walls seem to touch; 85mm and above for the key close-up.
- 光线：practical sources only — table lamp, window, chandelier; hard-edged shadows, light divided into zones, darks kept detailed, never flat.
- 色彩：jewel palette — crimson, emerald, violet, gold; high saturation, clean blacks; adjacent hues placed against each other, not graded into one.
- 材质：velvet, lacquered wood, glazed tile, patterned wallpaper, rain, glass, blood.

## 视频提示
- 镜头运动（只选一种）：precise lateral tracking shot, level and mechanical, gliding along a corridor and stopping dead on the axis.
- 主体运动：ritual preparation first — washing hands, straightening a tie, opening a drawer — then one sudden acceleration of the body; no flailing.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, crisp edges, no handheld shake, no speed ramp.

## 负面提示
no symmetrical composition as decoration, no symmetry without a power relation, no gore spectacle, no blood used as wallpaper, no nudity as depth, no moral victory ending, no catharsis, no fully explained psychology, no woman as prize or rescue object, no score telling us who is right, no handheld documentary shake, no neon montage, no clean digital sharpness.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：jewel red-green-violet-gold, high saturation, clean darks; 35–85mm compressed; practical light with hard-edged shadow zones; one-point centered symmetry, door and corridor frames; velvet, lacquer, tile, wallpaper.
- 禁止漂移：no desaturated grey palette, no handheld realism, no modern glass office towers, no LED white, no naturalistic flat daylight, no symmetrical frame with no one inside it.

## 平台备注
- Midjourney：`--style raw --stylize 250`；用一张《小姐》或《老男孩》静帧做 `--sref`锁珠宝色与对称；构图靠 `--sref`比靠文字稳。
- SDXL / ComfyUI：positive 固定块 + 高饱和珠宝色 palette 参考（IP-Adapter）；用 ControlNet depth 或 canny 锁一点透视与门洞；negative 单独成块，保留上列全部条目。
- Runway / Kling / Sora / Veo：先给首帧对称构图图，只写一种横移；5–8 秒、24fps；人物脸与服装用参考图/角色 ID 保持，不靠形容词；不要同时写推轨与升降。
