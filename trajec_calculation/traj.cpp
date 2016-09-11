#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

float my_func(float i)
{
    return i;
}

int main () 
{
// declare the variables

	float angle,velocity;
	float time,distance,height,dt;
    float vx,vy,vz;
    float ax,ay,az;
    float wx,wy,wz;
	float g;
	
	g = -9.80665;
	
// begin program and ask for user input
	
	cout << "Cannon Trajectory Program" << endl << endl;
	cout << "Enter the velocity (0-100): ";
	cin >> velocity;
	cout << "Enter the angle (0-90): ";
	cin >> angle;
	cout << endl << endl;

// output column headers

	cout << " Time    Distance    Height" << endl;
	cout << "------  ----------  --------" << endl;

// calculate results and display w/ loop
	
	time = 0;
      dt=0.001;
	height = 0;
	distance = 0;
	angle *= 3.1415926536 / 180; //Convert to radians
    vy = velocity * sin(angle);
    vx = velocity*cos(angle);
	
	while(height >= 0)
		{
			cout << time << " " << distance << " " << height << endl;


                vy += g*dt;
			distance += vx * dt;
			height += vy*dt;
			time += dt;
                cout << "my func: " <<my_func(time) << endl;
                cout << "my func: " << time << endl;                
			
		};
	
	return 0;
}
