import os
import hashlib
#set value
path='\\\\AWen_NAS\\AWen_NAS\\照片\\All_Pictures'


paths=os.listdir(path)
paths=sorted(paths,reverse = True)

def get_hash(img_path):
    # This function will return the `md5` checksum for any input image.
    with open(img_path, "rb") as f:
        img_hash = hashlib.md5()
        while chunk := f.read(8192):
           img_hash.update(chunk)
    return img_hash.hexdigest()



count=0
isCount=False

for time in range(len(paths)):
    removeList = []
    for fileName_ori in paths:
        print('Next:'+fileName_ori)
        count=0
        isCount=False
        for fileName_kill in paths:

            if fileName_ori==fileName_kill:
                print('SKIP!!!  '+fileName_ori +' == '+fileName_kill)
                isCount = True
                continue
            else:
                hash_ori = get_hash(path + '\\' + fileName_ori)
                hash_kill = get_hash(path + '\\' + fileName_kill)
                if hash_ori==hash_kill:
                    print('KILL*** '+fileName_ori + ' != ' + fileName_kill)
                    removeList.append(fileName_kill)
                    os.remove(path + '\\' +fileName_kill)



            # print(str(count)+' ' + fileName_ori + ' :: ' + fileName_kill)
            if isCount:
                count += 1
            if count==5:
                break
        paths.remove(fileName_ori)
        for removeFile in removeList:
            paths.remove(removeFile)
        break




