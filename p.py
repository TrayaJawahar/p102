import cv2 
import dropbox
import time
import random 

start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    vd = cv2.VideoCapture(0)
    result = True
    
    while(result):
        ret , frame= vd.read()
        name = "img"+str(number)+".png"
        cv2.imwrite(name,frame)
        start_time=time.time
        result = False

    return name
    print("Snapshot taken..")
    vd.release()
    cv2.destroyAllWindows()

def upload_file(name):
    access_token="4915DVAw43EAAAAAAAAAAehQAUFqFyH0ITBBLtGIt-qbzvf9cGRTcICeL7SWpRaB"
    file=name
    file_from =file
    file_to = "/testFolder/"+(name)
    dbx=dropbox.Dropbox(access_token)
    with open (file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")

def main ():
    while(True):
        if((time.time()-start_time)>=5):
            n=take_snapshot()
            upload_file(n)

main()

