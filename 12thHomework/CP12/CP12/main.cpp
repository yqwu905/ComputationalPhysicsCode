#include <cstdio>
//#include "Q1.h"
#include "Q2.h"
using namespace std;

//void Q1()
//{
//	const long NUM = 10000;
//	//cout << "q1 start!" << endl;
//	md md1(20, 10., 1., 1., 10., 0.001, 0,3.);
//	for (auto i = 0; i < NUM; i++)
//	{
//		if(i%(long)(NUM/100)==0)
//		{
//			cout << i << "/" << NUM << '\r';
//		}
//		//cout << i << ' ';
//		md1.update();
//	}
//	cout << endl;
//	md1.dump_data();
//	md1.calcV(0.2*NUM, 1*NUM, 1);
//}

void Q2()
{
	const long NUM = 15000;
	double T = 0, factor = 0.8;
	melting m1(125, 8., 1., 1., 0.001, 3.);
	for (auto i = 0; i < NUM; i++)
	{
		if (i % (long)(NUM / 500) == 0)
		{
			cout << i << "/" << NUM << '\r';
			m1.update(factor);
			if (factor < 1.1) factor += 0.001;
			//m1.dump_data(1.);
		}
		else
		{
			m1.update(1.0);
		}
	}
	cout << endl;
	m1.dump_data(100);
	m1.calcT(20);
}

int main()
{
	/*for (auto i = 0; i < 100; i++)
	{
		cout << "round "<< i << endl;
		Q1();
	}*/
	Q2();
	return 0;
}