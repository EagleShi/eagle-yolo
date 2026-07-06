# Jetson 部署

## 设备支持

| 设备 | GPU | 推荐模型 |
|------|-----|----------|
| Jetson Nano | 128-core Maxwell | YOLOv8n |
| Jetson Xavier NX | 384-core Volta | YOLOv8s/m |
| Jetson Orin Nano | 1024-core Ampere | YOLOv8s/11s |
| Jetson Orin NX | 1024-core Ampere | YOLOv8m/11m |
| Jetson AGX Orin | 2048-core Ampere | YOLOv8x/11l |

## 必须在设备上构建 engine

```bash
yolo export model=best.pt format=engine half=True device=0
```

## 性能优化

```bash
sudo nvpmodel -m 0    # 最大性能
sudo jetson_clocks     # 锁频
```

## 功耗模式

| 模式 | 功耗 | 性能 |
|------|------|------|
| MAXN | 15-60W | 最高 |
| 5W | 5W | 最低 |
