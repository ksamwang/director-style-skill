#!/usr/bin/env python3
"""Check the six craft modules."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, ".claude", "skills", "film-creation", "references", "craft")

REQUIRED = ["核心方法", "可执行规则", "场景检查清单", "常见错误", "练习", "与风格层的接口"]
CJK = re.compile(r"[一-鿿]")


def main() -> None:
    files = [f for f in sorted(glob.glob(os.path.join(DIR, "*.md")))
             if not f.endswith("README.md")]
    print(f"Craft modules: {len(files)}\n")
    issues = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        name = os.path.basename(f)
        chars = len(CJK.findall(text))
        missing = [s for s in REQUIRED if f"## {s}" not in text]
        probs = []
        if chars < 1800:
            probs.append(f"太短({chars})")
        elif chars > 3500:
            probs.append(f"太长({chars})")
        if missing:
            probs.append("缺章节:" + ",".join(missing))
        if probs:
            issues += 1
            print(f"[!] {name}: {' | '.join(probs)}")
        else:
            print(f"[ok] {name}: {chars} 字")
    print(f"\nChecked {len(files)} modules, {issues} with issues.")
    if len(files) != 6:
        print(f"WARNING: expected 6 modules, got {len(files)}")


if __name__ == "__main__":
    main()
