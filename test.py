import cv2
import numpy as np

# Function to apply brightness adjustment to a frame
def adjust_brightness(frame, brightness):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)
#COLOR_RGB2YCrCb====> filter one
    # Apply brightness adjustment to the V channel
    hsv[:, :, 2] += brightness
    # Ensure brightness values are within valid range
    hsv[:, :, 2] = np.clip(hsv[:, :, 2], 0, 255)
    # Convert frame back to BGR color space
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Open the video file
video_capture = cv2.VideoCapture('./input video.mp4')

# Get the video frame width and height
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter object to save the modified video
output_video = cv2.VideoWriter('output_video.mp4', 
                               cv2.VideoWriter_fourcc(*'mp4v'), 
                               30, 
                               (frame_width, frame_height))

# Adjust brightness by this value (increase/decrease as needed)
brightness_adjustment = 100

# Process each frame of the video
while video_capture.isOpened():
    ret, frame = video_capture.read()

    if not ret:
        break

    # Apply brightness adjustment to the frame
    modified_frame = adjust_brightness(frame, brightness_adjustment)

    # Write the modified frame to the output video file
    output_video.write(modified_frame)

    # Display the modified frame
    cv2.imshow('Modified Video', modified_frame)
    
    # Check for key press
    key = cv2.waitKey(25)
    if key == 27:  # Press 'Esc' to exit
        break

# Release video capture and writer objects
video_capture.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
