import cv2

def start_webcam(detector):
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    print("Press 'Q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Processing the frame
        processed_frame, count = detector.process_frame(frame)

        # UI Overlay: Display sheep count
        cv2.putText(
            processed_frame, 
            f"Sheep Count: {count}", 
            (20, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 0), 
            2
        )

        # Show the output window
        cv2.imshow("Sheep Counter Live", processed_frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
