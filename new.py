import cv2

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Could not read frame.")
else:
    # Display the frame in a window
    cv2.imshow("Camera", frame)
    cv2.waitKey(1000)

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
