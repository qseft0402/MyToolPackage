import os
import shutil
path_source='\\\\AWen_NAS\\AWen_NAS\\照片\\All_Pictures'
path_target_parent='\\\\AWen_NAS\\home\\Photos\\'

newFolder='All_Pictures2'
path_target=path_target_parent+newFolder
print(not os.path.exists(path_target))
print(os.path.isfile(path_target))

if os.path.isfile(path_target):
    print("目的端名稱相同，請檢查")
    exit
if not os.path.exists(path_target):
        os.mkdir(path_target)



paths=os.listdir(path_source)

count=0
for fileName in paths:
    count+=1
    print(str(int(count/len(paths)*100))+"% "+str(count)+'/'+str(len(paths)),end='')
    print(' copy '+path_source+'\\'+fileName + ' -----> '+path_target+'\\'+fileName)
    shutil.copy(path_source+'\\'+fileName,path_target+'\\'+fileName )
