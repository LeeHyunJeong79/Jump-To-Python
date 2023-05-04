import os
def search(dirname):
    try:
        filenames=os.listdir(dirname) #해당 디렉토리에 있는 파일(파일명 추출)들의 리스트를 구함
    # print(filenames)
        for filename in filenames:
            full_filename=os.path.join(dirname,filename) #파일명과 디렉토리를 이어주는 함수
            if os.path.isdir(full_filename):
                search(full_filename)
            # print(full_filename)
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext=='.py':
                    print("파이썬 파일",full_filename)

    except PermissionError:
        pass

search("C:/Users/hjeon/OneDrive - 군포e비즈니스고등학교/2021 교과/jump to python")