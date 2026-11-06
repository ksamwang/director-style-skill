#!/usr/bin/env python3
"""Normalize heading and signature_layers names across director entries."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / ".claude" / "skills" / "director-style" / "references" / "directors"

CANON = ["核心命题", "人物关系", "视觉规则", "镜头语法", "表演与对白", "时间与剪辑", "声音规则", "反向约束"]

LAYER_MAP = {
    "声音": "声音规则",
    "声音设计": "声音规则",
    "剪辑": "时间与剪辑",
    "长镜头": "时间与剪辑",
    "自然光": "视觉规则",
    "空间调度": "视觉规则",
    "空间与调度": "视觉规则",
    "场面调度": "视觉规则",
    "空间": "视觉规则",
    "画框": "视觉规则",
    "特写": "视觉规则",
    "对白": "表演与对白",
    "视觉": "视觉规则",
    "调度": "镜头语法",
    "表演": "表演与对白",
    "人物关系": "人物关系",
    "核心命题": "核心命题",
}

FM_RE = re.compile(r"^signature_layers:\s*\[(.*?)\]\s*$", re.M)
HEAD_RE = re.compile(r"^## 声音\s*$", re.M)


def normalize_layers(raw: str) -> list:
    seen = []
    for item in raw.split(","):
        item = item.strip().strip('"').strip("'")
        if not item:
            continue
        item = LAYER_MAP.get(item, item)
        if item in CANON and item not in seen:
            seen.append(item)
    return seen[:2]


def main() -> None:
    changed = 0
    for path in sorted(DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        original = text

        text = HEAD_RE.sub("## 声音规则", text)

        def repl(m):
            layers = normalize_layers(m.group(1))
            return "signature_layers: [" + ", ".join(layers) + "]"

        text = FM_RE.sub(repl, text)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"[fixed] {path.stem}")

    print(f"\nNormalized {changed} files.")


if __name__ == "__main__":
    main()
