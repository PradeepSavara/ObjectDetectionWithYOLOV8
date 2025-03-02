# from ultralytics import YOLO
# import cv2


# # load yolov8 model
# model = YOLO('yolov8n.pt')

# # load video
# video_path = './shop1.mp4'
# cap = cv2.VideoCapture(video_path)

# ret = True
# # read frames
# while ret:
#     ret, frame = cap.read()

#     if ret:

#         # detect objects
#         # track objects
#         results = model.track(frame, persist=True)

#         # plot results
#         # cv2.rectangle
#         # cv2.putText
#         frame_ = results[0].plot()

#         # visualize
#         cv2.imshow('frame', frame_)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Load video
video_path = './shop1.mp4'
cap = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = cap.read()
    
    if ret:
        # Detect and track objects
        results = model.track(frame, persist=True)

        # Check if a "person" is detected
        if results[0].boxes is not None:
            for box in results[0].boxes.data:
                class_id = int(box[5])  # Get class ID
                if class_id == 0:  # Class ID 0 corresponds to 'person' in YOLO
                    print("🚨 ALERT: Person detected!")

                    # You can replace this with an actual alert mechanism, like sending an email or a notification.

        # Draw detections
        frame_ = results[0].plot()

        # Show the frame
        cv2.imshow('frame', frame_)
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
