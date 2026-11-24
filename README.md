# pairwise-stair-slope-adhesion

## 领域

游戏、图形与多媒体

## 主题

楼梯台阶与斜坡贴地

## 说明

多射线贴地、帧号对齐与校正容差。

初始状态下 `gameplay/stair_slope_adhesion.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
