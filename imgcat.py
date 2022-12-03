import os, cv2, sys

SIZE = float(sys.argv[2])
BACKGROUND_PATH = sys.argv[3]
OUTPUT_FILE = sys.argv[1]

class Planche:
    def __init__(self, path):
        self.image = cv2.resize(cv2.imread(path), dsize = (0,0), fx = SIZE, fy = SIZE)
        self.coords = (int(path[0:2]), int(path[3:5]))

class Plan:
    def __init__(self, planches, void):
        abss = list(map(lambda elm : elm.coords[0], planches))
        ords = list(map(lambda elm : elm.coords[1], planches))
        image_at = lambda coords, planches, void : (list(map(lambda elm : elm.image, filter(lambda elm : elm.coords == coords, planches))) + [void])[0]
        matrix = [[image_at((x, y), planches, cv2.resize(void, dsize = (0,0), fx = SIZE, fy = SIZE))
            for x in range(min(abss), max(abss) + 1)]
            for y in range(min(ords), max(ords) + 1)]
        self.image = cv2.vconcat(list(map(lambda row : cv2.hconcat(row), matrix)))

plan = Plan(list(map(lambda path : Planche(path),
    list(filter(lambda elm : not elm in (os.path.realpath(__file__).split('/')[-1], BACKGROUND_PATH), os.listdir())))), cv2.imread(BACKGROUND_PATH))

cv2.imwrite(OUTPUT_FILE, plan.image)

#un peu illisible, mais élégant ! (si)
