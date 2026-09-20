"""用虚拟数据绘制可复现的练习图表。"""

from csv import DictReader
from pathlib import Path

import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "generated" / "waiting-time-by-demand.png"


def main() -> None:
    with (HERE / "waiting_time.csv").open(encoding="utf-8", newline="") as source:
        rows = list(DictReader(source))

    demand = [int(row["scenario"]) for row in rows]
    baseline = [float(row["baseline_minutes"]) for row in rows]
    improved = [float(row["improved_minutes"]) for row in rows]

    fig, axis = plt.subplots(figsize=(7, 4.5), layout="constrained")
    axis.plot(demand, baseline, marker="o", label="Baseline")
    axis.plot(demand, improved, marker="o", label="Improved")
    axis.set_title("Virtual exercise: waiting time by demand scenario")
    axis.set_xlabel("Demand scenario (% of reference demand)")
    axis.set_ylabel("Average waiting time (minutes)")
    axis.grid(alpha=0.25)
    axis.legend()

    OUTPUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUTPUT, dpi=200)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
