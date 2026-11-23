# 接触点进出批次时的块摩擦投影

`data/record.json` 是 接触点进出批次时的块摩擦投影 使用的本地合成交换样本。数组按 JSON 的下标顺序排列。本文的坐标、单位和枚举约定与该记录配套。记录中如果有 `scale` 或 `limits`，对应同一输入协议的部署规格。

冲量分量按法向、切向一、切向二排列。basis_quarters 表示该局部切向基从世界切平面的标定基逆时针旋转了几个 90°。contact_ids 冒号后是接触世代。diagonal 是本地 3×3 对角块的对角线，coupling 是从第二个局部冲量进入第一块方程的块，反向块取转置。force_limit 是对世界 global_load_direction 投影之和的上界；一般场景的线性限位同时接受逐触点局部行系数及上限，力矩由上游提供。cotangent_world 依首帧顺序提供同场景冲量的导数。

## 读取样本

使用 Python 3.11 或 3.12，并在虚拟环境安装锁定依赖。读取入口返回原始记录。作为命令运行时，它会列出各顶层输入项目以及 NumPy 版本。

```sh
python -m pip install -r requirements.txt
python -m contact_compliance_input
python -m unittest discover -s tests -v
```

测试读取交换样本，核对其中的张量尺寸、标识与数据约定。
