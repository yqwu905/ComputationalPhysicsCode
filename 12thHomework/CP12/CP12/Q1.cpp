#include "Q1.h"

coord::coord(double _x, double _y)
{
	x = _x;
	y = _y;
}

coord coord::operator+(coord p1)
{
	coord new_coord(x+p1.x, y+p1.y);
	return new_coord;
}

coord coord::operator-(coord p1)
{
	coord new_coord(x - p1.x, y - p1.y);
	return new_coord;
}

dist coord::distance(coord p1, double _l)
{
	double minR = INFINITY;
	int min_r_idx = 0;
	vector<dist> condition(9);
	for(auto i = -1; i < 2; i++)
	{
		for(auto j = -1; j < 2; j++)
		{
			condition[(i + 1) * 3 + (j + 1)].distant = sqrt(pow(p1.x - (x+i*_l),2) + pow(p1.y - (y+j*_l),2));
			if (condition[(i + 1) * 3 + (j + 1)].distant < minR)
			{
				minR = condition[(i + 1) * 3 + (j + 1)].distant;
				condition[(i + 1) * 3 + (j + 1)].cost = ((x + i * _l - p1.x) / condition[(i + 1) * 3 + (j + 1)].distant);
				condition[(i + 1) * 3 + (j + 1)].sint = ((y + j * _l - p1.y) / condition[(i + 1) * 3 + (j + 1)].distant);
				min_r_idx = (i + 1) * 3 + (j + 1);
			}
			
		}
	}
	return condition[min_r_idx];
}


configuration::configuration(int _n_moles, double _system_size, double _sigma, double _epsilon)
{
	n_moles = _n_moles;
	system_size = _system_size;
	sigma = _sigma;
	epsilon = _epsilon;
}

void configuration::init_moles_position()
{
	int n_moles_per_row = ((int)sqrt(n_moles) == sqrt(n_moles)) ? (int)sqrt(n_moles) : (int)sqrt(n_moles) + 1;
	//cout << n_moles_per_row << " molecules per row." << endl;
	double distance_between_moles = system_size / (n_moles_per_row+1);
	//cout << "Distance between molecules:" << distance_between_moles << endl;
	for(auto i = 0; i < n_moles; i++)
	{
		moles.push_back(coord((i%n_moles_per_row+1)*distance_between_moles, (int)(i/n_moles_per_row + 1)*distance_between_moles));
	}
	add_random_perturbation(0.5 * sigma);
}

void configuration::add_random_perturbation(double _quantity)
{
	for(auto i = 0; i < n_moles; i++)
	{
		double theta = 2 * pi * random;
		//cout << i << '\t' << _quantity * cos(theta) << '\t' << _quantity * sin(theta) << endl;
		moles[i].x += _quantity * cos(theta);
		moles[i].y += _quantity * sin(theta);
	}
}

void configuration::dump_data(ofstream& fp)
{
	for (coord i : moles)
	{
		fp << i.x << "," << i.y << endl;
	}
}


md::md(int _n_moles, double _system_size, double _sigma, double _epsilon, double _tot_time, double _time_step, double _v0, double _r_cutoff)
{
	srand(time(NULL));
	n_moles = _n_moles;
	system_size = _system_size;
	sigma = _sigma;
	epsilon = _epsilon;
	tot_time = _tot_time;
	time_step = _time_step;
	r_cutoff = _r_cutoff;
	configurations.push_back(configuration(n_moles, system_size, sigma, epsilon));
	configurations[0].init_moles_position();
	configurations.push_back(configurations.back());
	//configurations[1].add_random_perturbation(_v0*time_step);
	for(auto i = 0; i < n_moles; i++)
	{
		configurations[1].moles[i].x += random * time_step;
	}
}

void md::update()
{
	vector<double> totfx(n_moles);
	vector<double> totfy(n_moles);
	configurations.push_back(configurations.back());
	for(auto i = 0; i < n_moles; i++)
	{
		totfx[i] = 0;
		totfy[i] = 0;
		for (auto j = 0; j < n_moles; j++)
		{
			if (i == j) continue;
			dist d = configurations.back().moles[i].distance(configurations.back().moles[j], system_size);
			if (d.distant>r_cutoff) continue;
			double f = 24 * (2 * pow(d.distant, -13) - pow(d.distant, -7));
			if(f > pow(time_step,-2))
			{
				cout << d.distant << ' ' << f << endl;
			}
			totfx[i] += f * d.cost;
			totfy[i] += f * d.sint;
		}
	}
	
}

void md::dump_data()
{
	ofstream fp("Q1.txt", ios::out);
	for (auto i = 0; i < configurations.size(); i+=20)
	{
		fp << "Iter:" << i << endl;
		configurations[i].dump_data(fp);
	}
}

void md::calcV(int start, int end, int status)
{
	ofstream fp("Q1-V.txt", ios::app);
	for(auto i = 0; i < n_moles; i++)
	{
		double vx = 0, vy = 0;
		for(auto a1 = start + 1; a1 < end; a1++)
		{
			dist d = configurations[a1].moles[i].distance(configurations[a1-1].moles[i], system_size);
			vx += d.distant * d.cost / time_step;
			vy += d.distant * d.sint / time_step;
		}
		vx = vx / (end - start);
		vy = vy / (end - start);
		double v = sqrt(pow(vx, 2) + pow(vy, 2));
		switch (status)
		{
		case 0:
			fp << v << endl;
			break;
		case 1:
			fp << vx << endl;
			break;
		case 2:
			fp << vy << endl;
			break;
		}
	}
}
