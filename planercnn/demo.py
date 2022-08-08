import numpy as np
import matplotlib.pyplot as plt

def point_plane_intersection(planes_masks, point):
    for i in range(planes_masks.shape[0]):
        if planes_masks[i][point[1], point[0]]:
            return i
    return -1

def onclick(ax, event, planes_parameters, planes_masks):
    planes_normals, planes_offsets = normals_and_offsets_from_planes_parameters(planes_parameters)
    point = [int(round(event.xdata)), int(round(event.ydata))]
    planeidx = point_plane_intersection(planes_masks, point)
    # print(planes_normals[planeidx],planes_offsets[planeidx])    
    print(planes_offsets[planeidx])    
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

def mask_area(mask):
    return mask[mask == 1].sum()

def normals_and_offsets_from_planes_parameters(planes_parameters):
    # plane parameters = n * d
    # n is unit vector so by taking the magnitude we can calculate d then n
    offsets = np.linalg.norm(planes_parameters, axis=1)
    normals = planes_parameters / np.reshape(offsets,(planes_parameters.shape[0],1))
    return normals, offsets

def load_example_image():
    image = plt.imread("test/inference/2_segmentation_0_final.png")
    masks = np.load("test/inference/2_plane_masks_0.npy")
    parameters = np.load("test/inference/2_plane_parameters_0.npy")
    return image, masks, parameters

def main():
    # X: horizontal
    # Y: into screen
    # Z: vertical
    image, planes_masks, planes_parameters = load_example_image()
    show_image_and_masks(image, planes_parameters, planes_masks)

    # area = mask_area(mask)
    # print("Area: ", area)
    # show_mask(mask)

    # mask = planes_masks[9]
    # print(mask_area(mask))


    # import cv2
    # mat = mask
    # ret, thresh = cv2.threshold(mat, 0, 255, 0)
    # thresh = thresh.astype(np.uint8)
    # im2, contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # # print(len(res1),len(res2),len(res3))
    # # fin = cv2.drawContours(mat, contours, -1, (0,255,0), 3)
    # print(cv2.contourArea(contours[0]))

    # K = np.array([
    #     [587,0,240,0],
    #     [0,587,320,0],
    #     [0,0,1,0],
    # ])
    
    
    # print(planes_normals * 3779.5276)
    # normals = np.array([np.abs(np.matmul(K, n)) for n in planes_normals]).round()
    # normals = np.array([np.abs(np.matmul(K, np.append(n,0))) for n in planes_normals]).round()
    # print(normals)
    # print(np.concatenate(planes_normals,-1,0,axis=3))
    
    # K=3x3, n=3x1
    # normals = np.array([np.abs(np.matmul(K, n)) for n in planes_normals]).round()
    # planes_normals[:,0], planes_normals[:,1] = planes_normals[:,0] * 640, planes_normals[:,1] * 480
    # normals = np.abs(planes_normals.round())
    # show_masks(planes_masks)
    # plt.scatter(x=normals[:,0],y=normals[:,1])
    # plt.show()



if __name__ == "__main__":
    main()