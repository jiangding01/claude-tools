#!/usr/bin/env python3
"""汇总 skill-creator benchmark 运行结果，输出真实通过率。

背景：skill-creator 自带的 aggregate_benchmark 与 benchmark.json 的实际结构
不匹配，会生成 Pass Rate 0%、Tokens 0 的零值假报告（静默失败）。
本脚本直接读 benchmark.json 的 runs 数组，逐条 expectation 统计，
并列出所有未通过项及其证据，数字可逐条对账。

用法：
    python3 scripts/report_evals.py <workspace>/iteration-N/benchmark.json
"""

import json
import sys
from collections import defaultdict


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = json.load(f)

    meta = data.get("metadata", {})
    print(f"skill:    {meta.get('skill_name', '?')}")
    print(f"executor: {meta.get('executor_model', '?')}")
    print(f"time:     {meta.get('timestamp', '?')}")
    print()

    totals: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    failures: list[tuple[str, str, str]] = []

    for run in data.get("runs", []):
        cfg = run["configuration"]
        for exp in run.get("expectations", []):
            totals[cfg][1] += 1
            if exp["passed"]:
                totals[cfg][0] += 1
            else:
                failures.append((run["eval_name"], cfg, exp["text"]))

    if not totals:
        print("benchmark.json 里没有 runs 数据 —— 检查评测是否真的跑了。")
        sys.exit(2)

    print(f"{'配置':<12} {'通过/总数':<12} 通过率")
    for cfg, (passed, total) in sorted(totals.items()):
        print(f"{cfg:<12} {passed}/{total:<10} {passed / total:.1%}")

    if failures:
        print("\n未通过项：")
        for eval_name, cfg, text in failures:
            print(f"  [{cfg}] {eval_name}: {text}")
    else:
        print("\n全部期望项通过。")


if __name__ == "__main__":
    main()
