# Poker-hand-detector


Real-Time Poker Hand Detection System using YOLOv8 and OpenCV
This repository contains a complete real-time poker hand detection system powered by a custom-trained YOLOv8 object detection model and OpenCV for image processing.

The system utilizes live webcam input to detect multiple playing cards simultaneously and evaluates the best possible poker hand from the visible cards. It is optimized for educational, research, and interactive AI demonstration purposes, and offers a clear foundation for further development into smart gaming interfaces or card recognition tools.

Key Features
Real-Time Detection: Uses webcam input to identify playing cards on the fly.

Custom YOLOv8 Model: Trained on a curated dataset of standard 52-card poker images.

Hand Evaluation Engine: Interprets detected cards to determine current hand (e.g. Pair, Full House, Flush).

Modular and Readable Code: Built for clarity, ease of debugging, and extension.

Configurable Parameters: Adjustable detection confidence threshold for tuning accuracy.

Tech Stack
Python 3

YOLOv8 (via Ultralytics)

OpenCV for live video capture and annotation

Custom annotated dataset for card recognition

Project Status
Dataset Preparation: Completed

Model Training and Evaluation: Completed

Real-Time Inference and Hand Detection: Completed

Upcoming: Optional GUI, multiplayer support, or deployment via web or app interface

Use Cases
AI-powered casino tools

Smart poker table integrations

Educational demonstrations in computer vision

Real-time object detection experiments
