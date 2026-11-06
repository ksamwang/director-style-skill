#!/usr/bin/env python3
"""Build references/index.md from director frontmatter + one-line signatures."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / ".claude" / "skills" / "director-style" / "references" / "directors"
DP_DIR = ROOT / ".claude" / "skills" / "director-style" / "references" / "cinematographers"
OUT = ROOT / ".claude" / "skills" / "director-style" / "references" / "index.md"

REGION_ORDER = [
    "华语", "中国大陆", "香港", "台湾",
    "日本", "韩国",
    "南亚", "东南亚", "西亚", "伊朗", "土耳其", "巴勒斯坦", "印度", "泰国", "菲律宾", "越南",
    "欧洲", "法国", "意大利", "德国", "奥地利", "北欧", "瑞典", "丹麦", "芬兰", "挪威",
    "英国", "西班牙", "葡萄牙", "东欧", "俄罗斯", "波兰", "匈牙利", "塞尔维亚", "罗马尼亚", "希腊",
    "北美", "美国", "加拿大",
    "拉美", "巴西", "阿根廷", "墨西哥", "智利", "古巴",
    "非洲", "塞内加尔", "马里", "毛里塔尼亚", "埃及", "南非",
    "大洋洲", "澳大利亚", "新西兰",
]


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip("\n")
    data = {}
    current_list = None
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list:
            data.setdefault(current_list, []).append(line[4:].strip())
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                current_list = key
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                data[key] = [x.strip() for x in val[1:-1].split(",") if x.strip()]
                current_list = None
            else:
                data[key] = val.strip('"').strip("'")
                current_list = None
    return data


def one_line_signature(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "## 一句话签名":
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    return nxt.strip()
            break
    return ""


def region_rank(region: str) -> int:
    region = region or ""
    if region.startswith("中国"):
        region = "中国大陆"
    if region.startswith("苏联"):
        region = "俄罗斯"
    for i, key in enumerate(REGION_ORDER):
        if region == key or region.startswith(key):
            return i
    return len(REGION_ORDER)


def slug_link(title: str, slug: str) -> str:
    return f"[{title}](directors/{slug}.md)"


GROUP_ORDER = ["华语", "日本", "韩国", "南亚 / 东南亚 / 西亚", "欧洲", "北美", "拉美", "非洲", "大洋洲", "其他"]


def group_of(region: str) -> str:
    r = region or ""
    if r.startswith(("中国", "香港", "台湾")):
        return "华语"
    if r.startswith("日本"):
        return "日本"
    if r.startswith("韩国"):
        return "韩国"
    if r.startswith(("印度", "伊朗", "土耳其", "泰国", "菲律宾", "越南", "巴勒斯坦", "以色列", "黎巴嫩", "斯里兰卡", "巴基斯坦", "孟加拉")):
        return "南亚 / 东南亚 / 西亚"
    if r.startswith(("法国", "意大利", "德国", "奥地利", "瑞典", "丹麦", "芬兰", "挪威", "英国", "西班牙", "葡萄牙", "波兰", "苏联", "俄罗斯", "匈牙利", "塞尔维亚", "罗马尼亚", "希腊", "捷克", "比利时", "荷兰", "瑞士", "爱尔兰")):
        return "欧洲"
    if r.startswith(("美国", "加拿大")):
        return "北美"
    if r.startswith(("巴西", "阿根廷", "墨西哥", "智利", "古巴", "哥伦比亚", "秘鲁", "乌拉圭", "委内瑞拉", "玻利维亚")):
        return "拉美"
    if r.startswith(("塞内加尔", "马里", "毛里塔尼亚", "埃及", "南非", "尼日利亚", "布基纳法索", "摩洛哥", "突尼斯", "阿尔及利亚", "肯尼亚", "埃塞俄比亚", "加纳")):
        return "非洲"
    if r.startswith(("澳大利亚", "新西兰")):
        return "大洋洲"
    return "其他"


def main() -> None:
    rows = []
    for path in sorted(DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm.get("title"):
            print(f"SKIP (no frontmatter): {path.name}")
            continue
        rows.append({
            "slug": path.stem,
            "title": fm.get("title", path.stem),
            "region": fm.get("region", ""),
            "era": fm.get("era", ""),
            "family": fm.get("family", ""),
            "layers": "、".join(fm.get("signature_layers", []) or []),
            "signature": one_line_signature(text),
            "group": group_of(fm.get("region", "")),
        })

    rows.sort(key=lambda r: (GROUP_ORDER.index(r["group"]) if r["group"] in GROUP_ORDER else 99,
                             region_rank(r["region"]), r["region"], r["title"]))

    dp_rows = []
    for path in sorted(DP_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm.get("title"):
            print(f"SKIP DP (no frontmatter): {path.name}")
            continue
        dp_rows.append({
            "slug": path.stem,
            "title": fm.get("title", path.stem),
            "region": fm.get("region", ""),
            "era": fm.get("era", ""),
            "family": fm.get("family", ""),
            "layers": "、".join(fm.get("signature_layers", []) or []),
            "collaborators": "、".join(fm.get("collaborators", []) or []),
            "signature": one_line_signature(text),
        })
    dp_rows.sort(key=lambda r: r["title"])

    out = []
    out.append("# 总表\n")
    out.append(f"> 共 {len(rows)} 位导演 + {len(dp_rows)} 位摄影指导。按地域/角色分组；风格族见 `taxonomy.md`，混搭规则见 `mixing.md`。\n")

    for group in GROUP_ORDER:
        group_rows = [r for r in rows if r["group"] == group]
        if not group_rows:
            continue
        out.append(f"## {group}（{len(group_rows)}）\n")
        out.append(f"| 导演 | 地域 | 年代 | 风格族 | 签名层 | 一句话签名 | AI 提示 |")
        out.append("|---|---|---|---|---|---|---|")
        for r in group_rows:
            out.append(
                f"| {slug_link(r['title'], r['slug'])} | {r['region']} | {r['era']} | {r['family']} | {r['layers']} | {r['signature']} | [提示](prompts/{r['slug']}.md) |"
            )
        out.append("")

    if dp_rows:
        out.append(f"## 摄影指导（{len(dp_rows)}）\n")
        out.append("| 摄影指导 | 地域 | 年代 | 风格族 | 签名层 | 合作导演 | 一句话签名 | AI 提示 |")
        out.append("|---|---|---|---|---|---|---|---|")
        for r in dp_rows:
            out.append(
                f"| [{r['title']}](cinematographers/{r['slug']}.md) | {r['region']} | {r['era']} | {r['family']} | {r['layers']} | {r['collaborators']} | {r['signature']} | [提示](prompts-cinematographers/{r['slug']}.md) |"
            )
        out.append("")

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT} with {len(rows)} directors + {len(dp_rows)} cinematographers.")

    missing = [r for r in rows if not r["signature"]]
    if missing:
        print("MISSING SIGNATURE:", ", ".join(r["slug"] for r in missing))
    if len(rows) != 125:
        print(f"WARNING: expected 125 directors, got {len(rows)}")
    if len(dp_rows) != 29:
        print(f"WARNING: expected 29 cinematographers, got {len(dp_rows)}")


if __name__ == "__main__":
    main()
