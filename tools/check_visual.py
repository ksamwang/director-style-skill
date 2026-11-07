#!/usr/bin/env python3
"""Check visual/camera depth and 视觉配方 completeness."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, ".claude", "skills", "film-creation", "references", "directors")

VIS_DIMS = ["景别", "构图", "空间", "色彩", "光线", "材质"]
CAM_DIMS = ["机位", "焦段", "运动", "静止", "靠近", "远离", "权力"]
SPEC_FIELDS = ["参考画幅", "镜头/焦段", "机位与运动", "色彩", "光线", "材质/美术", "构图"]


def section(text: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    return text[start:start + nxt.start()] if nxt else text[start:]


def cjk_len(s: str) -> int:
    return len(re.findall(r"[一-鿿]", s))


def main() -> None:
    files = sorted(glob.glob(os.path.join(DIR, "*.md")))
    print(f"Files: {len(files)}\n")
    issues = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        name = os.path.basename(f)
        vis = section(text, "视觉规则")
        cam = section(text, "镜头语法")
        spec = section(text, "视觉配方")

        vis_hits = [d for d in VIS_DIMS if d in vis]
        cam_hits = [d for d in CAM_DIMS if d in cam]
        spec_lines = re.findall(r"^- ([^：:]+)[：:]", spec, re.M)
        missing_spec = [x for x in SPEC_FIELDS if x not in spec_lines]

        probs = []
        if len(vis_hits) < 4:
            probs.append(f"视觉维度{len(vis_hits)}/6")
        if len(cam_hits) < 3:
            probs.append(f"镜头维度{len(cam_hits)}/7")
        if missing_spec:
            probs.append("视觉配方缺:" + ",".join(missing_spec))
        if cjk_len(vis) < 150:
            probs.append(f"视觉规则短({cjk_len(vis)})")
        if cjk_len(cam) < 120:
            probs.append(f"镜头语法短({cjk_len(cam)})")

        if probs:
            issues += 1
            print(f"[!] {name}: {' | '.join(probs)}")
        else:
            print(f"[ok] {name}: 视觉{len(vis_hits)}/6 镜头{len(cam_hits)}/7 配方{len(SPEC_FIELDS)}/7")

    print(f"\nChecked {len(files)} files, {issues} with issues.")


if __name__ == "__main__":
    main()
