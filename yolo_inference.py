from ultralytics import YOLO

model = YOLO('models/yolov5_last.pt')  # Load model``

result = model.predict('input_videos/input_video.mp4', conf=0.2, save=True)

print(result)
print("boxes:")

for box in result[0].boxes:
    print(box)