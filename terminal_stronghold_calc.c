#include <stdio.h>
#include <math.h> // for the tan trig function and pi

int main()
{
    struct point
    {
        float x, z, f;
    };

    // declaring the points using structures to get values for the coordinates and angles
    struct point firstPoint, secondPoint;

    // declaring variables that will be the outputted result
    int x, z;

    // getting values for the coordinates and angles
    printf("Name your first x value: ");
    scanf("%f", &firstPoint.x);

    printf("Name your first z value: ");
    scanf("%f", &firstPoint.z);

    printf("Name your first f value: ");
    scanf("%f", &firstPoint.f);

    printf("Name your second x value: ");
    scanf("%f", &secondPoint.x);

    printf("Name your second z value: ");
    scanf("%f", &secondPoint.z);

    printf("Name your second f value: ");
    scanf("%f", &secondPoint.f);

    // solving for x and z coordinates of the stronghold
    // M_PI is the value of pi
    z = ((firstPoint.z * tan(-firstPoint.f * M_PI / 180)) - (secondPoint.z * tan(-secondPoint.f * M_PI / 180)) - firstPoint.x + secondPoint.x) / (tan(-firstPoint.f * M_PI / 180) - tan(-secondPoint.f * M_PI / 180));
    x = (z - firstPoint.z) * tan(-firstPoint.f * M_PI / 180) + firstPoint.x;

    // output results
    printf("\nThe stronghold is at (%i, %i).\n", x, z);

    return 0;
}