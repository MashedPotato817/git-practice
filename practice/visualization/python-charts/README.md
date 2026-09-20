# Python 图表练习

本练习用虚拟数据演示一张“平均等待时间—需求情景”折线图。重点是可复现脚本、清楚的单位与诚实的注释，不是让曲线看起来更漂亮。

## 运行

```powershell
python plot_waiting_time.py
```

脚本读取 `waiting_time.csv`，将图片输出到上级 `generated/`。需要安装 `matplotlib`：

```powershell
python -m pip install matplotlib
```

## 改造练习

1. 增加一组方案，并让图例清楚区分。
2. 将数据改为柱状图或散点图，解释为什么这种图更适合你的变量。
3. 在 README 中记录数据来源、单位、作图命令和你不能据此得出的结论。
