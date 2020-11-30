#include <iostream>
#include "ising_model.h"

void Q1()
{
	float t = 0.1, end = 3.0, step = 0.01;
	unsigned int repeat = 200;
	while(t < end)
	{
		float totM = 0;
		for(auto i = 0; i < repeat; i++)
		{
			ising_model I(10, 1000, 1, 1, t, 0, 0.1, 0);
			totM += I.run(0);
		}
		std::cout << t << "," << totM/repeat << std::endl;
		t += step;
	}
}

void Q2() {
	{
		ising_model I(10, 2000, 1, 1, 0.5, 0, 0.5, 0);
		I.set_magnet_field(1.5);
		I.run(1000);
		I.set_magnet_field(-1.5);
		I.run(0);
		for (auto i = 0; i < 2000; i++) {
			std::cout << I.M[i] << ",";
		}
		std::cout << std::endl;
	}
	{
		ising_model I(10, 2000, 1, 1, 0.5, 0, 0.5, 1);
		I.set_magnet_field(1.5);
		I.run(1000);
		I.set_magnet_field(-1.5);
		I.run(0);
		for (auto i = 0; i < 2000; i++) {
			std::cout << I.M[i] << ",";
		}
		std::cout << std::endl;
	}
}
int main() {
	Q2();
    return 0;
}
