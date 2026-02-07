# Face Recognition Attendance System

An automated attendance system using real-time face recognition with liveness detection to prevent spoofing attacks. This system captures facial images, verifies liveness, and automatically marks attendance with timestamps.

## 🎯 Features

- **Real-time Face Detection**: Detect and recognize faces using webcam feed
- **Liveness Detection**: Advanced anti-spoofing mechanism to prevent fake face attacks
- **Face Recognition**: Uses FaceNet embeddings with cosine similarity matching
- **Automated Attendance**: Automatically marks attendance with timestamps
- **Face Registration**: Easy enrollment system for new users
- **CSV-based Records**: Attendance records stored in CSV format for easy export

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam/Camera
- Required Python libraries (see Installation)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahipal-01/Face-Recognition-Attendance-system.git
   cd Face-Recognition-Attendance-system
   ```

2. **Install required dependencies**
   ```bash
   pip install opencv-python
   pip install numpy
   pip install tensorflow
   pip install keras
   pip install scikit-learn
   pip install mediapipe
   ```

3. **Verify model files are present**
   - `facenet_keras.h5` - FaceNet model for face embeddings
   - `blaze_face_short_range.tflite` - Face detection model
   - `face_landmarker.task` - Face landmark detection model

## 📁 Project Structure

```
Face-Recognition-Attendance-system/
├── main.py                           # Main entry point
├── register.py                       # Face registration module
├── recognize.py                      # Face recognition module
├── embeddings.py                     # Face embedding generation
├── liveness.py                       # Liveness detection module
├── attendance.py                     # Attendance marking logic
├── faces/                            # Stored face embeddings (.npy files)
├── attendance.csv                    # Attendance records
├── facenet_keras.h5                  # Pre-trained FaceNet model
├── blaze_face_short_range.tflite    # Face detection model
├── face_landmarker.task              # Face landmark model
└── README.md                         # Project documentation
```

## 🚀 Usage

### 1. Register New Users

First, register users by capturing their face embeddings:

```bash
python register.py
```

- Enter the person's name when prompted
- Look at the camera and follow the on-screen instructions
- The system will capture facial embeddings and save them in the `faces/` directory as `.npy` files

### 2. Run Attendance System

Start the attendance recognition system:

```bash
python recognize.py
```

Or use the main entry point:

```bash
python main.py
```

**How it works:**
1. The camera feed will open
2. Position your face in front of the camera
3. Complete the liveness challenge displayed on screen
4. If your face is recognized and liveness is confirmed:
   - Your attendance will be marked
   - A confirmation message will appear
   - The record will be saved to `attendance.csv`

### 3. View Attendance Records

Attendance records are stored in `attendance.csv` with the following format:

```csv
Name, Date, Time, Status
John Doe, 2024-02-07, 09:15:23, Present
```

## 🔒 Liveness Detection

The system includes anti-spoofing measures to prevent attendance fraud:

- **Challenge-Response**: Users must complete visual challenges
- **Face Landmarks Analysis**: Validates 3D facial structure
- **Motion Detection**: Ensures the face is from a live person
- **Real-time Verification**: Continuous validation during recognition

## ⚙️ How It Works

### Face Registration Process
1. Captures face from webcam using BlazeFace detector
2. Generates 128-dimensional embedding using FaceNet
3. Saves embedding as `.npy` file in `faces/` directory

### Recognition Process
1. Detects face in real-time video feed
2. Generates embedding for detected face
3. Compares with stored embeddings using cosine similarity
4. If similarity > 0.6 (60% match) and liveness confirmed:
   - Marks attendance with timestamp
   - Updates `attendance.csv`

### Liveness Detection
- Uses MediaPipe Face Landmarks
- Analyzes facial movement patterns
- Prevents photo/video spoofing attacks

## 📊 Technical Details

### Models Used
- **FaceNet (Keras)**: Face recognition and embedding generation
- **BlazeFace**: Fast and efficient face detection
- **MediaPipe Face Landmarker**: Facial landmark detection for liveness

### Key Parameters
- **Similarity Threshold**: 0.6 (60% match required)
- **Embedding Dimension**: 128-D vector
- **Image Processing**: Face normalization and preprocessing

## 🔧 Configuration

You can modify the following parameters in the code:

- **Similarity Threshold** (in `recognize.py`):
  ```python
  if similarity > 0.6:  # Adjust threshold (0.0 to 1.0)
  ```

- **Display Duration** (in `recognize.py`):
  ```python
  cv2.waitKey(1500)  # Show result for 1.5 seconds
  ```

- **Camera Index** (in `recognize.py`):
  ```python
  cap = cv2.VideoCapture(0)  # 0 for default camera
  ```

## 🐛 Troubleshooting

**Camera not opening:**
- Check if camera is properly connected
- Try changing camera index: `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)`
- Ensure no other application is using the camera

**Face not detected:**
- Ensure good lighting conditions
- Face the camera directly
- Move closer or farther from the camera

**Recognition not working:**
- Check if face is properly registered in `faces/` directory
- Verify `.npy` files exist for registered users
- Try lowering the similarity threshold for testing

**Liveness detection failing:**
- Follow the on-screen challenge instructions
- Ensure your face is clearly visible
- Avoid wearing accessories that obscure facial features

## 📝 Notes

- Ensure proper lighting for better recognition accuracy
- Register multiple angles of the same person for improved accuracy
- Clean the `faces/` directory periodically to remove old/unused entries
- Backup `attendance.csv` regularly

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Mahipal**
- GitHub: [@mahipal-01](https://github.com/mahipal-01)

## 🙏 Acknowledgments

- FaceNet for face recognition model
- MediaPipe for face detection and landmarks
- OpenCV community for computer vision tools

## 📧 Contact

For questions, suggestions, or issues, please open an issue on the GitHub repository.

---

**Note**: This system is designed for educational and small-scale applications. For production use in large organizations, additional security measures and scalability improvements are recommended.
