import matplotlib.pyplot as plt
import cv2
import numpy as np

def detect_edges_and_corners(image, filename):
    path = 'static/img'
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(image=image_rgb, threshold1=100, threshold2=700)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    image_with_corners = np.copy(image)
    image_with_corners[dst > 0.01 * dst.max()] = [0, 0, 255]  
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image', fontsize=20)
    axs[1].imshow(edges, cmap='gray')
    axs[1].set_title('Image Edges', fontsize=20)
    axs[2].imshow(cv2.cvtColor(image_with_corners, cv2.COLOR_BGR2RGB))
    axs[2].set_title('Image with Corners', fontsize=20)
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout()
    output_name = f"{path}/{filename}_output.png"
    plt.savefig(output_name)
    plt.close() 
    return output_name
