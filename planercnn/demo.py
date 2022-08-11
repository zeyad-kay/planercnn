import numpy as np
import matplotlib.pyplot as plt
import math

PPM = 1
FOCAL_LENGTH = 587

def point_plane_intersection(planes_masks, point):
    for i in range(planes_masks.shape[0]):
        if planes_masks[i][point[1], point[0]]:
            return i
    return -1

def onclick(ax, event, planes_parameters, planes_masks):
    planes_normals, planes_offsets = normals_and_offsets_from_planes_parameters(planes_parameters)
    point = [int(round(event.xdata)), int(round(event.ydata))]
    planeidx = point_plane_intersection(planes_masks, point)
    area = mask_area(planes_masks[planeidx], planes_normals[planeidx], planes_offsets[planeidx])
    print("Area: ", area)
    ax.clear()
    if planeidx != -1:
        ax.imshow(planes_masks[planeidx])
        ax.plot([point[0], point[0] + abs(planes_normals[planeidx][0]* 50)], [point[1], point[1] + abs(planes_normals[planeidx][2]* 50)], linewidth=3,color="red",alpha=1-abs(planes_normals[planeidx][1]))
    else:
        ax.imshow(np.zeros((planes_masks.shape[1],planes_masks.shape[2])))
    # ax.scatter(point[0], point[1],color="red",s=50)
    plt.show()

def show_image_and_masks(image, planes_parameters, planes_masks):
    combined_masks = np.sum(planes_masks, axis=0)
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(image)
    axs[1].imshow(combined_masks)
    fig.canvas.mpl_connect('button_press_event', lambda e: onclick(axs[1], e, planes_parameters, planes_masks))
    plt.show()
    return

def mask_area(mask, normal, offset):
    theta = math.atan(normal[1]/normal[0])
    alpha = math.acos(normal[2]/np.linalg.norm(normal))
    print(f"offset: {offset}, normal: {normal}, theta: {theta * 180 / math.pi}, alpha: {alpha * 180 / math.pi}")

    # l = offset * pixels / FOCAL_LENGTH
    pixel_area = (mask * offset * 1e3 / FOCAL_LENGTH) ** 2
    
    return abs((pixel_area / math.sin(theta) / math.sin(alpha)).sum() * 1e-6)

def normals_and_offsets_from_planes_parameters(planes_parameters):
    # plane parameters = n * d
    # n is unit vector so by taking the magnitude we can calculate d then n
    offsets = np.linalg.norm(planes_parameters, axis=1)
    normals = planes_parameters / np.reshape(offsets,(planes_parameters.shape[0],1))
    return normals, offsets

def load_example_image():
    image = plt.imread("test/inference/1_image_0.png")
    # image = plt.imread("test/inference/2_segmentation_0_final.png")
    masks = np.load("test/inference/1_plane_masks_0.npy")
    parameters = np.load("test/inference/1_plane_parameters_0.npy")
    return image, masks, parameters

def main():
    # X: horizontal
    # Y: into screen
    # Z: vertical
    image, planes_masks, planes_parameters = load_example_image()
    show_image_and_masks(image, planes_parameters, planes_masks)

    # K = np.array([
    #     [587,0,240],
    #     [0,587,320],
    #     [0,0,1],
    # ])   

if __name__ == "__main__":
    main()