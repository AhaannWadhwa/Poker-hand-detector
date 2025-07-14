# Poker-hand-detector



# 🃏 Real-Time Poker Hand Detection Using YOLOv8 & OpenCV

This project is a *real-time card recognition* and *poker hand evaluation system* built with a custom-trained *YOLOv8 model* and *OpenCV*. It captures live video from your webcam, detects multiple cards in a single frame, and intelligently determines your best poker hand from the visible cards.

# 🚀 Features 

~ Detects multiple playing cards simultaneously using YOLOv8 

~ Live webcam feed with card overlays and poker hand classification 

~ Custom-trained model on a 52-card poker deck 

~ Displays hand type: Pair, Two Pair, Full House, Flush, etc. 

~ Easily adjustable detection confidence threshold 


# 🛠️ Technologies Used 

~ Python 3  

~ OpenCV (cv2) 

~ Ultralytics YOLOv8 

# 📦 Installation 

First, clone the repository:

git clone https://github.com/yourusername/poker-hand-detector.git
cd poker-hand-detector

Install the required Python libraries:

pip install ultralytics opencv-python

Running the App 

To start real-time card detection and hand evaluation, run:

python running_model.py

Make sure your webcam is connected and functional.

# 🧠 Model Details 

~ YOLOv8 trained on custom dataset of individual poker cards 

~ Format: label = “RankSuit” (e.g., KH = King of Hearts) 

~ Model output is used to determine best visible poker hand 

# 📋 Example Detected Cards 

~ AH (Ace of Hearts) 

~ 10S (Ten of Spades) 

~ JD (Jack of Diamonds)

~ 7C (Seven of Clubs) 

And many more — the full 52-card set is supported.

# 🧼 Cleanup

~ Press the 'q' key during detection to stop the webcam and close the application safely.

# 📌 To-Do / Ideas for Expansion

~ Detect overlapping or partially visible cards

~ Train model on real-life card images for improved accuracy

~ Add web-based GUI for easier interaction

~ Support for gesture-based control or voice commands

# 📜 License
~ This project is open source under the MIT License.

# 🙌 Acknowledgements

~ Ultralytics YOLOv8

~ OpenCV

~ Dataset preparation by project team

~ Developed with care and sleepless nights

Created with ❤️ by Ahaann

