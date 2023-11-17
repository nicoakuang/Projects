# Import the necessary libraries
import cv2  # Import the OpenCV library for computer vision tasks
import time  # Import the time library for time-related functions
import keyboard  # Import the keyboard library for monitoring and controlling keyboard input
import pyautogui  # Import the pyautogui library for controlling the mouse and screen
import win32api  # Import the win32api library for Windows API functions
import win32con  # Import the win32con library for Windows API constants

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a connection to your webcam (usually the default camera)
cap = cv2.VideoCapture(0)

# Function to simulate a mouse click at coordinates (x, y)
def click(x, y):
    # Set the mouse cursor position to (x, y)
    win32api.SetCursorPos((x, y))
    
    # Simulate a left mouse button press at the current cursor position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    
    # Pause for a short time (10 milliseconds)
    time.sleep(0.01)
    
    # Simulate a left mouse button release at the current cursor position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Start an infinite loop to continuously process frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection using the Haar Cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Check if exactly 2 faces are detected
    if len(faces) == 2:
        # Display "MET! CODE RUNNING" text on the frame
        cv2.putText(frame, "MET! CODE RUNNING", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Check the pixel color at (307, 400)
        if pyautogui.pixel(307, 400) == (0, 0, 0):
            # If the pixel color at (307, 400) is black (R=0, G=0, B=0), perform a click at that location
            click(307, 400)
            
        # Check the pixel color at (416, 400)
        if pyautogui.pixel(416, 400) == (0, 0, 0):
            # If the pixel color at (416, 400) is black (R=0, G=0, B=0), perform a click at that location
            click(416, 400)
        
        # Check the pixel color at (524, 400)
        if pyautogui.pixel(524, 400) == (0, 0, 0):
            # If the pixel color at (524, 400) is black (R=0, G=0, B=0), perform a click at that location
            click(524, 400)
            
        # Check the pixel color at (639, 400)
        if pyautogui.pixel(639, 400) == (0, 0, 0):
            # If the pixel color at (639, 400) is black (R=0, G=0, B=0), perform a click at that location
            click(639, 400)

    # Display the frame with face detection in a separate window
    cv2.imshow('Face detection', frame)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
