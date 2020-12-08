#pragma once

#include <iostream>
#include <fstream>
#include <random>
#include <ctime>

#define random ((double)rand()/RAND_MAX)

using namespace std;

typedef struct dis
{
	double r;
	double cx;
	double cy;
	double cz;
};

class vec3d
{
public:
	double x, y, z;
	vec3d(double _x, double _y, double _z);
	dis distance(vec3d v1, double l);
	vec3d operator+(vec3d v1);
	vec3d operator-(vec3d v1);
	vec3d operator*(double a);
	double dot(vec3d v1);
};

class configuration
{
public:
	vector<vec3d> moles;
	int n_moles;
	double system_size;
	configuration(int _n_moles, double _system_size);
	void init_moles_position();
	void dump_data(ofstream& fp);
};

class melting
{
public:
	int n_moles;
	double system_size, sigma, epsilon, time_step, r_cutoff;
	vector < configuration > configurations;
	melting(int _n_moles, double _system_size, double _sigma, double _epsilon, double _time_step, double _r_cutoff);
	void update(double factor);
	void dump_data(int interval);
	void calcT(int period);
};