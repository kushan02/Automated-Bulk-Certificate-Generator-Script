# Script Author: Kushan Mehta
# Target Python version: 3.6+ (Not tested with python 2 version)

# Imports OpenCV library - required for this script
import cv2

#Modify the below variables according to your preferences

# Enter valid paths from your own file system

# The input file contains names as a line seperated list
input_txt_file = 'D:\Path-to-your-input-file\certi-namelist.txt'

template_file_path = 'D:\Path-to-your-own-template-image\CERTI_TEMPLATE.png'

# Make sure this output directory already exists or else certificates won't actually be generated
output_directory_path = 'D:\Path-for-output-directory\Generated_Certificates\\'

font_size = 3.8
font_color = (51,51,51)

# Test with different values for your particular Template
# This variables determine the exact position where your text will overlay on the template
# Y adjustment determines the px to position above the horizontal center of the template (may be positive or negative)
coordinate_y_adjustment = 280
# X adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative)
coordinate_x_adjustment = 7

# Core Logic begins

print('The Script is running...')

with open(input_txt_file) as input_list:
    
    content = input_list.read().splitlines()

    for line in content:

        certi_name = line

        img = cv2.imread(template_file_path)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = certi_name
    
        textsize = cv2.getTextSize(text, font, font_size, 10)[0]
        text_x = (img.shape[1] - textsize[0]) / 2 + coordinate_x_adjustment
        text_y = (img.shape[0] + textsize[1]) / 2 - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)
		
        cv2.putText(img, text, (text_x, text_y ), font, font_size, font_color, 10)
        certi_path = output_directory_path + certi_name + '.png'
        cv2.imwrite(certi_path,img)

cv2.destroyAllWindows()

