import cv2

def record_video(output_file="output.avi", codec="XVID", fps=20.0, resolution=(640, 480), duration=10):
    """
    Record a video using OpenCV.

    Parameters:
        output_file (str): Name of the output file.
        codec (str): FourCC code for the video codec (e.g., 'XVID', 'MP4V').
        fps (float): Frames per second.
        resolution (tuple): Resolution of the video (width, height).
        duration (int): Duration of the recording in seconds.
    """
    # Initialize the video capture object (0 for default camera)
    cap = cv2.VideoCapture(0)
    
    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(output_file, fourcc, fps, resolution)
    
    # Calculate the number of frames to capture
    frame_count = int(fps * duration)
    frame_index = 0

    print("Recording video... Press 'q' to stop manually.")
    
    while cap.isOpened() and frame_index < frame_count:
        ret, frame = cap.read()
        if ret:
            # Write the frame to the output file
            out.write(frame)
            
            # Display the frame (optional)
            cv2.imshow("Recording", frame)
            
            # Break loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            frame_index += 1
        else:
            break
    
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_file}")

# Usage
record_video(output_file="recorded_video.avi", codec="XVID", fps=20.0, resolution=(640, 480), duration=10)
