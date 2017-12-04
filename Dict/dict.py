import collections
import datetime
import random

import sys

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


def main():
    print("Creating data...", end=' ')
    sys.stdout.flush()

    data_list = []
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))


    print("Done")
    sys.stdout.flush()

    print("Reordering data for random access ...", end=' ')
    sys.stdout.flush()

    data_list.sort(key=lambda d: d.quality)
    print("done.")

    # Creating interestin grandom ids

    interesting_ids = {random.randint(0, len(data_list)) for _ in range(0, 100)}
    print("Creating {} interesting IDs to seek.".format(len(interesting_ids)))

    print("Locating data in list...", end=' ')
    sys.stdout.flush()

    t0 = datetime.datetime.now()
    interesting_points = []
    for i in interesting_ids:
        pt = find_point_by_id_in_list(data_list, i)
        interesting_points.append(pt)


if __name__ == '__main__':
    main()



