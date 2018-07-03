# DOI_Extraction

In this script we load the file into python framework using opencv's cv2 and then make other grayscale varient of that.
On that greyscale varint we apply thresholding keeping in veiw that ROI(region of intrest) has black background. we applying contouring
and 30th contour gives us the requieed contour we apply ractangle function and get the starting coordinate(top-left) and the width and height of the required rectangle which we then crop from the actual colour image and then save that crop imaged back to the directory. 
<table>
 <tr>
  <td>!<a src="3.png"> </td>
  <td>![This is the source image](https://cdn.onlinewebfonts.com/svg/img_70394.png "This is the source image")</td>
  <td>![We are to extract this from this](cropped_img.jpg "We are to extract this from this")</td>
 </tr>
</table>
