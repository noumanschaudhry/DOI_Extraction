# DOI_Extraction

In this script we load the file into python framework using opencv's cv2 and then make other grayscale varient of that.
On that greyscale varint we apply thresholding keeping in veiw that ROI(region of intrest) has black background. we applying contouring
and 30th contour gives us the requieed contour we apply ractangle function and get the starting coordinate(top-left) and the width and height of the required rectangle which we then crop from the actual colour image and then save that crop imaged back to the directory. 
<table>
 <tr>
  <td><img src="3.jpg"> </td>
  <td width="200px"><img src="https://png.icons8.com/windows/1600/long-arrow-right.png"></td>
  <td><img src="cropped_img.jpg"We are to extract this from this")</td>
 </tr>
 <tr>
  <td align='center'>We have these screenshots</td>
  <td></td>
  <td align='center'>We are to extract this from this</td>
 </tr>
</table>
