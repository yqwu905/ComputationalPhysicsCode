#include "Q2.h"

vec3d::vec3d(double _x, double _y, double _z)
{
	x = _x;
	y = _y;
	z = _z;
}

dis vec3d::distance(vec3d v1, double l)
{
	dis d;
	d.r = INFINITY;
	double r;
	for(auto ix = -1; ix < 2; ix++)
	{
		for (auto iy = -1; iy < 2; iy++)
		{
			for (auto iz = -1; iz < 2; iz++)
			{
				r = sqrt(pow(v1.x - (x + ix*l),2) + pow(v1.y - (y+iy*l),2) + pow(v1.z - (z + iz*l),2));
				if (r < d.r)
				{
					d.r = r;
					d.cx = ((x + ix * l) - v1.x) / r;
					d.cy = ((y + iy * l) - v1.y) / r;
					d.cz = ((z + iz * l) - v1.z) / r;
				}
			}
		}
	}
	return d;
}

vec3d vec3d::operator+(vec3d v1)
{
	vec3d v_new(x+v1.x, y+v1.y, z+v1.z);
	return v_new;
}

vec3d vec3d::operator-(vec3d v1)
{
	vec3d v_new(x - v1.x, y - v1.y, z - v1.z);
	return v_new;
}

vec3d vec3d::operator*(double a)
{
	vec3d v_new(x*a, y*a, z*a);
	return v_new;
}

double vec3d::dot(vec3d v1)
{
	return (x * v1.x + y * v1.y + z * v1.z);
}


configuration::configuration(int _n_moles, double _system_size)
{
	n_moles = _n_moles;
	system_size = _system_size;
}

void configuration::init_moles_position()
{
	int n_moles_per_row = ((int)pow(n_moles, 1. / 3) == pow(n_moles, 1. / 3)) ? (int)pow(n_moles, 1. / 3) : (int)pow(n_moles, 1. / 3) + 1;
	cout << n_moles << " " << pow(n_moles, 1. / 3) << endl;
	cout << n_moles_per_row << " molecules per row." << endl;
	double distance_between_moles = system_size / (n_moles_per_row + 1);
	cout << "Distance between molecules:" << distance_between_moles << endl;
	for(auto i = 0; i < n_moles_per_row; i++)
	{
		for (auto j = 0; j < n_moles_per_row; j++)
		{
			for (auto k = 0; k < n_moles_per_row; k++)
			{
				moles.push_back(vec3d((i+1)*distance_between_moles, (j+1)*distance_between_moles, (k+1)*distance_between_moles));
			}
		}
	}
}

void configuration::dump_data(ofstream& fp)
{
	for (vec3d i: moles)
	{
		fp << i.x << "," << i.y << "," << i.z << endl;
	}
}

melting::melting(int _n_moles, double _system_size, double _sigma, double _epsilon, double _time_step, double _r_cutoff)
{
	n_moles = _n_moles;
	system_size = _system_size;
	sigma = _sigma;
	epsilon = _epsilon;
	time_step = _time_step;
	r_cutoff = _r_cutoff;
	configurations.push_back(configuration(n_moles,system_size));
	configurations.back().init_moles_position();
	configurations.push_back(configurations.back());
}

void melting::update(double factor)
{
	//cout << n_moles << endl;
	vector<vec3d> totF;
	configurations.push_back(configurations.back());
	for (auto i = 0; i < n_moles; i++)
	{
		//f(i==0) cout << configurations.back().moles[i].x << " " << configurations.back().moles[i].y << " " << configurations.back().moles[i].z << endl;
		totF.push_back(vec3d(0, 0, 0));
		for (auto j = 0; j < n_moles; j++)
		{
			if (i == j) continue;
			//cout << i << " " << j << endl;
			dis d = configurations.back().moles[i].distance(configurations.back().moles[j], system_size);
			//cout << i << " " << j << endl;
			//if (i == 0 && j == 2) cout << configurations.back().moles[i].z << " " << d.r*d.cz << endl;
			if (d.r > r_cutoff) continue;
			double f = 24 * (2 * pow(d.r, -13.) - pow(d.r, -7.));
			if (f > pow(time_step, -2))
			{
				cout << d.r << ' ' << f << endl;
			}
			totF[i] = totF[i] + vec3d(d.cx, d.cy, d.cz)*f;
		}
	}
	//cout << totF[13].x << " " << totF[13].y << " " << totF[13].z << endl;
	for (auto i = 0; i < n_moles; i++)
	{
		configurations.back().moles[i] = configurations.back().moles[i] + (configurations[configurations.size() - 2].moles[i] - configurations[configurations.size() - 3].moles[i])*factor + totF[i]*time_step*time_step;
		if (configurations.back().moles[i].x > system_size)
		{
			configurations.back().moles[i].x = configurations.back().moles[i].x - floor(configurations.back().moles[i].x / system_size) * system_size;
		}
		if (configurations.back().moles[i].x < 0)
		{
			configurations.back().moles[i].x = (floor(abs(configurations.back().moles[i].x) / system_size) + 1) * system_size + configurations.back().moles[i].x;
		}
		if (configurations.back().moles[i].y > system_size)
		{
			configurations.back().moles[i].y = configurations.back().moles[i].y - floor(configurations.back().moles[i].y / system_size) * system_size;
		}
		if (configurations.back().moles[i].y < 0)
		{
			configurations.back().moles[i].y = (floor(abs(configurations.back().moles[i].y) / system_size) + 1) * system_size + configurations.back().moles[i].y;
		}
		if (configurations.back().moles[i].z > system_size)
		{
			configurations.back().moles[i].z = configurations.back().moles[i].z - floor(configurations.back().moles[i].z / system_size) * system_size;
		}
		if (configurations.back().moles[i].z < 0)
		{
			configurations.back().moles[i].z = (floor(abs(configurations.back().moles[i].z) / system_size) + 1) * system_size + configurations.back().moles[i].z;
		}
	}
}

void melting::dump_data(int interval)
{
	ofstream fp("Q2.txt", ios::out);
	for(auto i = 0; i < configurations.size(); i+=interval)
	{
		cout << i << "/" << configurations.size() << "\r";
		fp << "Iter:" << i << endl;
		configurations[i].dump_data(fp);
	}
	cout << endl;
}

void melting::calcT(int period)
{
	vector<double> TList, RList;
	for(auto i = 1; i < configurations.size(); i++)
	{
		double T = 0, rMean = 0;
		for (auto n = 0; n < n_moles; n++)
		{
			if (n != 0)
			{
				dis d = configurations[i].moles[0].distance(configurations[i].moles[n], system_size);
				rMean += d.r/(n_moles - 1);
			}
			vec3d V(0, 0, 0);
			V = configurations[i].moles[n] - configurations[i-1].moles[n];
			T += V.dot(V);
		}
		if(i%(int)(configurations.size()/100)==0)
		cout << i << "/" << configurations.size() << '\r';
		TList.push_back(T);
		RList.push_back(rMean);
	}
	cout << endl;
	ofstream fp("Q2-T.txt", ios::out);
	for(auto i = 0;i < RList.size(); i++)
	{
		fp << TList[i] << "," << RList[i] << endl;
	}
	fp.close();
}