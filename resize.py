from PIL import Image
import os
import cv2

def resize_images(input_folder, output_folder, new_size):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)

        # Check if the file is an image
        if not os.path.isfile(filepath):
            continue
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            continue

        # Open the image
        with Image.open(filepath) as img:
            # Resize the image while maintaining the aspect ratio
            img2=img.resize(new_size ) 

            # Save the resized image to the output folder
            output_filepath = os.path.join(output_folder, filename)
            img2.save(output_filepath)
    return img2


    


if __name__ == "__main__":
    input_folder = "img/Original Images"  # Replace with the path to the folder containing the images
    output_folder = "img/new_size_original"  # Replace with the path to the folder where resized images will be saved
    input_folder2= "img/Meibomian Gland Labels" 
    output_folder2 = "img/new_size_glands"  # Replace with the path to the folder where resized images will be saved
    input_folder3= "img/Eyelid Lebels" 
    output_folder3="img/new_size_eyelid"
    # input_folder4= "chaos/dcms" 
    # output_folder4="chaos/new_dcms"
    # input_folder5= "chaos/pngs" 
    # output_folder5="chaos/new_pngs"
    input_folder6= "img/new_raw" 
    output_folder6= "img/new_size_raw" 
    # input_folder7= "mete_jpg/images"
    # output_folder7= "mete_jpg/images2"
    # input_folder8= "mete_jpg/masked_images" 
    # output_folder8= "mete_jpg/masked_images2"
    
    new_size = (128, 64)  # Replace with the desired new size (width, height) in pixels


    resize_images(input_folder, output_folder, new_size)
    resize_images(input_folder2, output_folder2, new_size)
    resize_images(input_folder3, output_folder3, new_size)
    resize_images(input_folder6, output_folder6, new_size)
    # resize_images(input_folder4, output_folder4, new_size)
    # resize_images(input_folder5, output_folder5, new_size)
    # resize_images(input_folder7, output_folder7,new_size)
    # resize_images(input_folder8, output_folder8,new_size)
