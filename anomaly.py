
    
# import cv2
# import numpy as np
path = 'static/img'
# # def detect_anomalies(input_image, reference_image, threshold, filename):
# #     # Convert images to grayscale
# #     input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
# #     reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

# #     # Compute absolute difference between input and reference image
# #     diff = cv2.absdiff(input_gray, reference_gray)

# #     # Apply threshold to identify anomalies
# #     _, anomalies = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

# #     # Find contours of anomalies
# #     contours, _ = cv2.findContours(anomalies, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #     # Draw circles around detected anomalies
# #     anomalies_image = input_image.copy()
# #     for contour in contours:
# #         (x, y), radius = cv2.minEnclosingCircle(contour)
# #         center = (int(x), int(y))
# #         radius = int(radius)
# #         cv2.circle(anomalies_image, center, radius, (0, 0, 255), 2)
# #         name = path + "/" + filename + ".jpg"
# #         cv2.imwrite(name, image)
# #     return name

    

# # def anomaly( inpp, reff):
# #     # Load input and reference images
# #     input_image = cv2.imread(inpp)
# #     reference_image = cv2.imread(reff)

# #     # Set threshold for anomaly detection
# #     threshold = 30

# #     # Detect anomalies
# #     anomalies_detected = detect_anomalies(input_image, reference_image, threshold, filename)

# #     # Display input image with anomalies detected
# #     # cv2.imshow('Anomalies Detected', anomalies_detected)
# #     # cv2.waitKey(0)
# #     # cv2.destroyAllWindows()

import cv2
import numpy as np

def detect_anomalies(input_image, reference_image, threshold, filename):
    # Convert images to grayscale
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference between input and reference image
    diff = cv2.absdiff(input_gray, reference_gray)

    # Apply threshold to identify anomalies
    _, anomalies = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Find contours of anomalies
    contours, _ = cv2.findContours(anomalies, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw circles around detected anomalies
    anomalies_image = input_image.copy()
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(anomalies_image, center, radius, (0, 0, 255), 2)

    # Save the image with anomalies marked
    output_path =  path + "/" + filename + ".jpg"
    cv2.imwrite(output_path, anomalies_image)

    return output_path

def anomalies(inpp, reff, filename):
    # Load input and reference images
    input_image = cv2.imread(inpp)
    reference_image = cv2.imread(reff)

    # Set threshold for anomaly detection
    threshold = 30

    # Detect anomalies
    result = detect_anomalies(input_image, reference_image, threshold, filename)
    return result





    
# import cv2
# import numpy as np
# path = 'static/img'
# def detect_anomalies(input_image, reference_image, threshold):
#     # Convert images to grayscale
#     input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
#     reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

#     # Compute absolute difference between input and reference image
#     diff = cv2.absdiff(input_gray, reference_gray)

#     # Apply threshold to identify anomalies
#     _, anomalies = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

#     # Find contours of anomalies
#     contours, _ = cv2.findContours(anomalies, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw circles around detected anomalies
#     anomalies_image = input_image.copy()
#     for contour in contours:
#         (x, y), radius = cv2.minEnclosingCircle(contour)
#         center = (int(x), int(y))
#         radius = int(radius)
#         cv2.circle(anomalies_image, center, radius, (0, 0, 255), 2)

#     return anomalies_image

# def anomalies(input_image, reference_image, filename):
#     # Load input and reference images
#     # input_image = cv2.imread("E:\\Anomaly\\.venv\\002.png")
#     # reference_image = cv2.imread("E:\\Anomaly\\.venv\\000.png")

#     # Set threshold for anomaly detection
#     threshold = 30

#     # Detect anomalies
#     anomalies_detected = detect_anomalies(input_image, reference_image, threshold)

#     output_path =  path + "/" + filename + ".jpg"
#     cv2.imwrite(output_path, anomalies_detected)
#     # Display input image with anomalies detected
#     return output_path




