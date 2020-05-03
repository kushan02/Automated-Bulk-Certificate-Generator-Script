# Script Author: Kushan Mehta
import cv2
import pandas as pd

#Modify the below variables according to your preferences

# Enter valid paths from your own file system

# The input file contains names as a comma seperated list of format (Rank, User handle, Name)
participants = pd.read_csv("ranklist.csv")

template_file_path = "CERTI_TEMPLATE.png"

# Make sure this output directory already exists or else certificates won't actually be generated
output_directory_path = "generated_certificates"

font_size = 3.8
font_color = (51,51,51)

# Test with different values for your particular Template
# This variables determine the exact position where your text will overlay on the template
# Y adjustment determines the px to position above the horizontal center of the template (may be positive or negative)
coordinate_y_adjustment = 280
# X adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative)
coordinate_x_adjustment = 7

disqualified = {"user_handle_of_disqualified"}

winners = {"user_handle_of_winners"}

for index, row in participants.iterrows():

    if row["User handle"] in disqualified or row["User handle"] in winners:
        continue

    print(row["User handle"])

    certiName = row["Name"].title()

    img = cv2.imread(template_file_path)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = certiName

	textsize = cv2.getTextSize(text, font, font_size, 10)[0]
	text_x = (img.shape[1] - textsize[0]) / 2 + coordinate_x_adjustment
	text_y = (img.shape[0] + textsize[1]) / 2 - coordinate_y_adjustment
	text_x = int(text_x)
	text_y = int(text_y)
	
	cv2.putText(img, text, (text_x, text_y ), font, font_size, font_color, 10)
	certi_path = output_directory_path + certi_name + '.png'
	cv2.imwrite(certi_path,img)

    certiPath = "{}/{}.png".format(output_directory_path,row["User handle"])
    cv2.imwrite(certiPath, img)

cv2.destroyAllWindows()
