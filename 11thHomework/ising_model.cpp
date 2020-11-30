//
// Created by yqwu on 29/11/2020.
//

#include "ising_model.h"
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;

ising_model::ising_model(unsigned int L, unsigned int N, float J, float kB, float T, float H, float Mu, unsigned int boudary)
{
    srand(time(NULL));
    j = J;
    size = L;
    steps = N;
    kb = kB;
    t = T;
    h = H;
    mu = Mu;
    current_step = 0;
    spin = new int* [size];
    boundary_condition = boudary;
    for(auto i = 0; i < size; i++)
    {
        spin[i] = new int[size];
    }
    for(auto i = 0; i < size; i++)
    {
        for(auto j = 0; j < size; j++)
        {
            spin[i][j] = 1;
            //spin[i][j] = rand() % 2 == 1 ? 1 : -1;
        }
    }
    M = new float[steps];
}

ising_model::~ising_model()
{
    for(auto i = 0; i < size; i++)
    {
        delete[] spin[i];
    }
    delete[] spin;
    delete[] M;
}

bool ising_model::flip(int* s, unsigned int n)
{
    float Ef = 2*mu*h*s[0];
    for(auto i = 1; i < n; i++)
    {
        Ef += 2*j*s[0]*s[i];
    }
    if(Ef<0)
    {
        return true;
    }
    else
    {
        if (rand() < exp(-Ef / (kb * t)) * RAND_MAX)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

}


void ising_model::bound_process(unsigned int i, unsigned int j)
{
    switch (boundary_condition)
    {
        case 0:			//Period boundary condition.
        {
	        int s[5] = {spin[i][j], spin[(i + 1) % size][j], spin[i == 0 ? size - 1 : i - 1][j],
	                    spin[i][(j + 1) % size], spin[i][j == 0 ? size - 1 : j - 1]};
	        if (flip(s, 5)) {
		        spin[i][j] = -1 * spin[i][j];
	        }
        }
        case 1:         //Free boundary condition
        {
	        if ((i == 0 || i == size-1) && (j == size - 1 || j == 0))        //Corner
	        {
		        int s[3] = {spin[i][j], spin[i == 0 ? 1 : size - 2][j], spin[i][j == 0 ? 1 : size - 2]};
		        if (flip(s, 3)) {
			        spin[i][j] = -1 * spin[i][j];
		        }
	        }
	        else                                                //Edge
	        {
		        if (i == 0 || i == size - 1) {
			        int s[4] = {spin[i][j], spin[i == 0 ? 1 : size - 2][j], spin[i][j + 1], spin[i][j - 1]};
			        if (flip(s, 4)) {
				        spin[i][j] = -1 * spin[i][j];
			        }
		        }
		        else {
			        int s[4] = {spin[i][j], spin[i][j == 0 ? 1 : size - 2], spin[i + 1][j], spin[i - 1][j]};
			        if (flip(s, 4)) {
				        spin[i][j] = -1 * spin[i][j];
			        }
		        }
	        }
        }
    }
}


void ising_model::update()
{
    for(auto i = 0; i < size; i++)
    {
        for(auto j = 0; j < size; j ++)
        {
            //cout << i << " " << j << endl;
            if(i==0 || j==0 || i==size-1 || j==size-1)
            {
                bound_process(i, j);
            }
            else
            {
                int s[5] = { spin[i][j], spin[i + 1][j] ,spin[i - 1][j] ,spin[i][j + 1] ,spin[i][j - 1] };
                if(flip(s, 5))
                {
                    spin[i][j] = -1 * spin[i][j];
                }
            }
        }
    }
}

void ising_model::statistic(unsigned int i)
{
    float tot_m = 0;
    for(auto i = 0; i < size; i++)
    {
        for(auto j = 0; j < size; j++)
        {
            tot_m += spin[i][j];
        }
    }
    //cout << tot_m/(size*size) << endl;
    M[i] = tot_m/(size*size);
}

float ising_model::run(int run_step)
{

	if (run_step==0)
	{
		run_step = steps - current_step;
	}
    float totM = 0;
    for(int j=0; j < run_step; current_step++,j++)
    {
        update();
        statistic(current_step);
        totM += M[current_step];
    }
    return totM/steps;
}

void ising_model::set_magnet_field(float H) {
	h = H;
	//cout << "Magnetic filed amplitude has change:" << h << endl;
}

