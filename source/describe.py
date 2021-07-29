"""
The main of this script is the following.
We assume that we have the database "TVAR" with the tables : avdertisements, descriptors, apparitions

Function 1 :
input = Folder --> output = the table "avdertisements"
- From the folder advertisements read each ads and extracte the first and the last frame
- For each ads create the liste [id, name, first_frame, last_frame, duration]
- Write in to the table "avdertisements"

Function 2 :
input = output of Function 1 --> output = the table " descriptors"
- For each line in the table "avdertisements" create [id, name, first_frame_descriptor, last_frame_descriptor, duration]
- Write on the table "descriptors"
"""