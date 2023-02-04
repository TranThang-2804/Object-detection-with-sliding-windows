import torch

# Model
model = torch.hub.load('./yolov5', 'custom', path='./best.pt', source='local')
# methods = dir(model) 
# print(methods)

# Inference
def detectObject(img, confidence):
    results = model(img)
     

    if 0 in results.pandas().xyxy[0]['class']:
        if (results.pandas().xyxy[0]['confidence'] > confidence).any():
            print(results.pandas().xyxy[0])
            results.save()
            return True
