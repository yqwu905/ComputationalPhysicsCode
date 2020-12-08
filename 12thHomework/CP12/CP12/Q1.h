#include "cmath"
#include <iostream>
#include <vector>
#include <random>
#include <ctime>
#include "fstream"

#define random ((double)rand()/RAND_MAX)
#define pi 3.141592653

using namespace std;

typedef struct dist
{
	double distant;
	double cost;
	double sint;
};

class coord
{
public:
	double x;
	double y;
	coord(double _x, double _y);
	coord operator+(coord p1);
	coord operator-(coord p1);
	dist distance(coord p1, double _l);
};

class configuration
{
public:
	int n_moles;
	double system_size, sigma, epsilon;
	configuration(int _n_moles, double _system_size, double _sigma, double _epsilon);
	vector<coord> moles;
	void init_moles_position();
	void add_random_perturbation(double _quantity);
	void dump_data(ofstream& fp);
};

class md
{
public:
	int n_moles;
	double system_size, sigma, epsilon, tot_time, time_step, r_cutoff;
	vector<configuration> configurations;
	md(int _n_moles, double _system_size, double _sigma, double _epsilon, double _tot_time, double _time_step, double _v0, double _r_cutoff);
	void update();
	void dump_data();
	void calcV(int start, int end, int status);
};