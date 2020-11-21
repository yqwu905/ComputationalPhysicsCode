#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class point
{
    public:
    int coord[2];
    point(int x, int y)
    {
        coord[0] = x;
        coord[1] = y;
    }
    float R2()
    {
        return (float)(coord[0]*coord[0] + coord[1]*coord[1]);
    }
    point add(int dx, int dy)
    {
        return point(coord[0] + dx, coord[1] + dy);
    }
};

class path
{
    public:
        vector<point> p;
        bool inPath(int newx, int newy)
        {
            int lastx = p.back().coord[0];
            int lasty = p.back().coord[1];
            for(int i = 0; i < p.size(); i++)
            {
                if(lastx + newx == p[i].coord[0] && lasty + newy == p[i].coord[1])
                    return false;
            }
            //cout << "inPath\t" << newx << "\t" << newy << endl;
            return true;
        }
        void setOrigin()
        {
            p.push_back(point(0,0));
        }
        void push(int newx, int newy)
        {
            p.push_back(p.back().add(newx,newy));
        }
        void show()
        {
            cout << p.size();
            for(int i = 0; i < p.size(); i++)
            {
                cout << "(" << p[i].coord[0] << "," << p[i].coord[1] << ")";
            }
            cout << "\n";
        }
};

vector<path> iter(vector<path>& paths)
{
    int dx[4] = {1,-1,0,0};
    int dy[4] = {0,0,1,-1};
    vector<path> newPath;
    while(paths.size() > 0)
    {

        //paths[i].show();
        for(int j = 0; j < 4; j++)
        {
            //cout <<"j\t" << j << "\t" << dx[j] << "\t" << dy[j] << endl;
            path a = paths.back();
            if(a.inPath(dx[j],dy[j]))
            {
                a.push(dx[j], dy[j]);
                newPath.push_back(a);
            }
        }
        paths.pop_back();
    }
    return newPath;
}

float calcR(vector<path>& paths)
{
    float R = 0;
    for(long i = 0; i < paths.size(); i++)
    {
        path a = paths[i];
        R += a.p.back().R2();
    }
    return R/paths.size();
}

int main()
{
    path origin;
    origin.setOrigin();
    vector <path> paths;
    paths.push_back(origin);
    cout << sizeof(origin) << endl;
    
    for(int i = 1; i <= 50; i++)
    {
        cout << "############################" << endl;
        paths = iter(paths);
        cout << "R^2 " << calcR(paths) << endl;
        cout << i << "\t" << paths.size() << endl;;
    }

    return 0;
}