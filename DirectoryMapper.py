import jinja2, pathlib
from pathlib import Path


class DirectoryFolder(object):
    bookmark = []

    def __init__(self,folder,level=0):
        self.name = Path(folder).name
        self.level = level
        self.fpath = str(folder)
        self.parentNm = Path(folder).parent.name
        self.dirMap = {}

        for f in Path(self.fpath).glob(r'*'):
            if f.is_file():
                self.dirMap.update({f.name:(DirectoryFile(f,(self.level+1)),'file')})
            else:
                self.dirMap.update({f.name:(DirectoryFolder(f,level=self.level+1),'folder')})

    
    def __iter__(self):
        self.n = 0
        self.keys = list(self.dirMap.keys())
        DirectoryFolder.bookmark.append(self)
        return self

    def __next__(self):
        curIter = DirectoryFolder.bookmark[-1]
        if curIter.n < len(curIter.keys):
            outtuple = (curIter.keys[curIter.n],curIter.dirMap[curIter.keys[curIter.n]][0],
                        curIter.dirMap[curIter.keys[curIter.n]][1])
            #outtuple = (curIter.keys[curIter.n],curIter.dirMap[curIter.keys[curIter.n]][0],
                        #curIter.dirMap[curIter.keys[curIter.n]][1],curIter.level+1)
            curIter.n += 1
            if outtuple[2] == 'folder':
                iter(outtuple[1])
            return outtuple
        else:
            DirectoryFolder.bookmark.pop()
            if len(DirectoryFolder.bookmark) > 0:
                return next(DirectoryFolder.bookmark[-1])
            else:
                raise StopIteration

class DirectoryFile(DirectoryFolder):

    def __init__(self,filePath,level):
        self.name = Path(filePath).name
        self.fpath = str(filePath)
        self.level = level
        self.parentNm = Path(filePath).parent.name


if __name__ == '__main__':

    #frontierFile = r"C:\Users\Harriskd\Documents\Personal\Data\New Jersey"
    #outFile = r"C:/Users/Harriskd/Desktop/meowMap_withJS.html"
    frontierFile = r"J:\2020 projects\EBXD7901\800deliv"
    outFile = r"C:\Users\Harriskd\Documents\Personal\Projects\Roadway\LIE\Folder Maps\800Folder_20210121.html"

    env = jinja2.Environment( loader = jinja2.FileSystemLoader(str(Path.cwd())))
    template = env.get_template('DirTree_template.html')

    result = DirectoryFolder(frontierFile)


    with open(outFile,'w') as omap:
        try:
            omap.write(template.render(
                topFolder = result.name,
                topPath = result.fpath,
                mapList = result
            ))
        except UnicodeEncodeError:
            pass