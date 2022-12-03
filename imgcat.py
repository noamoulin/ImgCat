import os, cv2, sys

av = sys.argv

OUTPUT_FILE = av[1]
SIZE = float(av[2])

XMIN = int(av[3])
XMAX = int(av[4])
YMIN = int(av[5])
YMAX = int(av[6])

BACKGROUND_PATH = av[7]

def coords_of(path): return (int(path[0:2]), int(path[3:5]))

class Planche:
    def __init__(self, path):
        self.image = cv2.resize(cv2.imread(path), dsize = (0,0), fx = SIZE, fy = SIZE)
        self.coords = coords_of(path)

class Plan:
    def __init__(self, planches, void):
        abss = list(map(lambda elm : elm.coords[0], planches))
        ords = list(map(lambda elm : elm.coords[1], planches))
        image_at = lambda coords, planches, void : (list(map(lambda elm : elm.image, filter(lambda elm : elm.coords == coords, planches))) + [void])[0]
        matrix = [[image_at((x, y), planches, cv2.resize(void, dsize = (0,0), fx = SIZE, fy = SIZE))
            for x in range(min(abss), max(abss) + 1)]
            for y in range(min(ords), max(ords) + 1)]
        self.image = cv2.vconcat(list(map(lambda row : cv2.hconcat(row), matrix)))

files = os.listdir()
utils = (os.path.realpath(__file__).split('/')[-1], BACKGROUND_PATH)
planches_paths = list(filter(lambda elm : not elm in utils, files))
elues = list(filter(lambda elm : XMIN <= coords_of(elm)[0] <= XMAX and YMIN <= coords_of(elm)[1] <= YMAX, planches_paths))
planches = list(map(lambda path : Planche(path), elues))
background = cv2.imread(BACKGROUND_PATH)
plan = Plan(planches, background)

cv2.imwrite(OUTPUT_FILE, plan.image)
