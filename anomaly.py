import cv2
path = 'static/img'
def detect_anomalies(input_image, reference_image, threshold, filename):
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(input_gray, reference_gray)
    _, anomalies = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(anomalies, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    anomalies_image = input_image.copy()
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(anomalies_image, center, radius, (0, 0, 255), 2)
    output_path =  path + "/" + filename + ".jpg"
    cv2.imwrite(output_path, anomalies_image)
    return output_path

def anomalies(inpp, reff, filename):
    input_image = cv2.imread(inpp)
    reference_image = cv2.imread(reff)
    threshold = 30
    result = detect_anomalies(input_image, reference_image, threshold, filename)
    return result
