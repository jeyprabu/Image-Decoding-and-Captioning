import matplotlib.pyplot as plt
import cv2
path = 'static/img'
def edges(image, filename):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(image= image_rgb, threshold1=100, threshold2=700)
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')
    axs[1].imshow(edges)
    axs[1].set_title('Image edges')
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout()
    name = path+"/"+filename+".png"
    plt.savefig(name)
    return name

