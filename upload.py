from imagekitio import ImageKit
import os
import time

imagekit = ImageKit(
    private_key='',
    public_key='',
    url_endpoint=''
)

directory = 'images'
c = 0 
# iterate over files in
# that directory
print(os.listdir(directory))
print("\n")
for filename in os.listdir(directory):
    isdir = os.path.isdir(filename)
    if(isdir):
        di = filename
        # print("di="+di)
        for filename in os.listdir(di):
            f = os.path.join(directory, di, filename)
            if os.path.isfile(f):
                path = "/a/images1/"+di+"/"
                print("f1=="+path+"\n")
                f2 = os.path.join(di,filename)

                imagekit.upload_file(
                    file=open(f2,"rb"),  # required
                    file_name=filename,  # required
                    options={
                        "folder": path,
                        "is_private_file": False,
                        "use_unique_file_name": False,
                        "response_fields": ["is_private_file", "tags"],
                        
                    }
                )
                print(f+"\n")
                c += 1
                print("Count",c)
    else:
        f = os.path.join(directory, filename)
    # checking if it is a file
        if os.path.isfile(f):
            print(f+"\n")



