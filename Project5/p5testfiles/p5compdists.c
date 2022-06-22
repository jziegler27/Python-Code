
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct point
{
    double x;
    double y;
    double z;
};

double *compute_distances(int numpts, struct point *points)
{
    int i, j, idx, numpairs;
    double xval, yval, zval, mindist;
    double *dists;
    
    printf("RMBSTART\n");
    // numpairs =  (numpts * (numpts+1)) / 2;  // gauss :-)
    numpairs =  ((numpts-1) * numpts) / 2;  // gauss :-)
    dists = (double *)malloc(numpairs * sizeof(double));

    mindist = 2.0;
    idx = 0;
    for (i=0; i < numpts; i++)
    {
        for (j=i+1; j < numpts; j++)  // i+1
        {
            xval = points[i].x - points[j].x;
            yval = points[i].y - points[j].y;
            zval = points[i].z - points[j].z;
            dists[idx] = sqrt(xval*xval + yval*yval + zval*zval);
            if (dists[idx] < mindist  &&  dists[idx] > 0.0)
                mindist = dists[idx];
            idx++;
        }
    }

    printf("RMBMIN  %14.12lf\n",mindist);
    return dists;
}
