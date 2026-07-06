# Android 部署

## TFLite

```bash
yolo export model=best.pt format=tflite imgsz=640 int8=True data=data.yaml
```

## Kotlin 集成

```kotlin
import org.tensorflow.lite.Interpreter
val interpreter = Interpreter(loadModelFile("best.tflite"))
val inputBuffer = preprocessImage(bitmap, 640)
val output = Array(1) { Array(8400) { FloatArray(84) } }
interpreter.run(inputBuffer, output)
```

## NCNN（推荐）

```bash
yolo export model=best.pt format=ncnn imgsz=640
```

NCNN 在移动端通常优于 TFLite。

## 性能

| 框架 | Pixel 7 | Snapdragon 8 Gen 2 |
|------|---------|---------------------|
| TFLite INT8 | ~25ms | ~12ms |
| NCNN | ~18ms | ~8ms |
