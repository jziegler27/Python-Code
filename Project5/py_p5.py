import sys, random
seed = int(sys.argv[1])
number_points = int(sys.argv[2])
random.seed(seed)
test = []
values = []
distances = []
from cffi import FFI
ffi = FFI()
ffi.cdef("""
        struct point {
            double x;
            double y;
            double z;
        };
        double *compute_distances(int numpts, struct point *points);
    """
    )

cpoints = ffi.new(f"struct point[%i]" %number_points)
for i in range(number_points):
    cpoints[i].x = random.random()
    cpoints[i].y = random.random()
    cpoints[i].z = random.random()

lib = ffi.dlopen("./libp5.so")
distances = lib.compute_distances(number_points, cpoints)
mim = 2.0
for j in range( int(((number_points-1) * number_points) / 2)):
    if distances[j] < mim:
        mim = distances[j]
print(f"{mim:.12f}")




