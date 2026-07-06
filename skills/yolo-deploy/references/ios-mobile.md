# iOS 部署

## CoreML

```bash
yolo export model=best.pt format=coreml imgsz=640
```

## Swift 集成

```swift
import Vision
let model = try! VNCoreMLModel(for: YOLOv8().model)
let request = VNCoreMLRequest(model: model) { req, _ in
    guard let results = req.results as? [VNRecognizedObjectObservation] else { return }
    for det in results { print(det.labels.first?.identifier, det.confidence) }
}
try! VNImageRequestHandler(cgImage: image).perform([request])
```

## 性能

| 模型 | iPhone 14 Pro | iPhone 12 |
|------|---------------|-----------|
| YOLOv8n | ~8ms | ~15ms |
| YOLO11n | ~7ms | ~13ms |
