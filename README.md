## **Object Detection with YOLOv8 🚀**  
An advanced AI-powered object detection system using **YOLOv8**, designed for real-time applications in security, surveillance, and automation.

![YOLOv8 Object Detection](https://github.com/ultralytics/assets/raw/main/im/yolov8_segment.png)  

---

## **📌 Project Overview**  
This project implements **YOLOv8**, the latest version of **You Only Look Once (YOLO)**, to detect and classify objects in images and videos. The model is trained on a custom dataset and fine-tuned for high-accuracy real-time object detection.  

✅ **Features:**  
- Fast and efficient object detection  
- Real-time inference on images and videos  
- Supports bounding boxes for detected objects  
- Custom dataset training with YOLOv8  
- Optimized for **security, surveillance, and automation**  

✅ **Applications:**  
- **Security Surveillance** 🏢  
- **Traffic Monitoring** 🚗  
- **Wildlife Tracking** 🦅  
- **Retail Analytics** 🏪  

---

## **🛠️ Setup & Installation**  

### **1️⃣ Install YOLOv8**  
```bash
pip install ultralytics
```

### **2️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/ObjectDetectionWithYOLOV8.git
cd ObjectDetectionWithYOLOV8
```

### **3️⃣ Download the Dataset**  
- Ensure your dataset is in **YOLO format** (`images` + `labels` directories).  
- Modify `data.yaml` to include dataset paths.

### **4️⃣ Train the Model**  
```bash
yolo train model=yolov8s.pt data=./data.yaml epochs=50 imgsz=640
```

### **5️⃣ Run Inference on Images**  
```bash
yolo predict model=best.pt source=your_image.jpg
```

### **6️⃣ Run Inference on a Video**  
```bash
yolo predict model=best.pt source=your_video.mp4
```

---

## **🖼️ Sample Results**  
| Input Image | Detected Objects |
|------------|----------------|
| ![input](https://github.com/ultralytics/assets/raw/main/im/yolov8_detect1.png) | ![output](https://github.com/ultralytics/assets/raw/main/im/yolov8_detect2.png) |

---

## **📝 Dataset**  
- **Format:** YOLO format (`images/`, `labels/`, `data.yaml`)  
- **Classes:** Weapons, vehicles, humans, etc.  
- **Source:** Kaggle / Custom-labeled data  

---

## **📊 Model Performance**  
| Metric  | Value |
|---------|-------|
| mAP@50  | 92.5% |
| FPS (Speed) | 35+ FPS |
| Inference Time | ~12ms |

---

## **📌 Future Enhancements**  
✅ Deploy as a **Web App** using Flask/Django  
✅ Optimize model size for **mobile devices**  
✅ Add **multi-class detection** for various applications  

---

## **📜 License**  
This project is open-source under the **MIT License**.  

---

## **📬 Contact**  
📧 **Email:** savarapradeep24.com  
 

---

🔹 **Like this project?** ⭐ Star this repository! 🚀  
🔹 **Contribute?** Open a pull request! 🤝  

---
