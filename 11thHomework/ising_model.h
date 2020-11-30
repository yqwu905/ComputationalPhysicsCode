//
// Created by yqwu on 29/11/2020.
//

#ifndef UNTITLED_ISING_MODEL_H
#define UNTITLED_ISING_MODEL_H

#endif //UNTITLED_ISING_MODEL_H

#pragma once

class ising_model
{
public:
    ising_model(unsigned int L, unsigned int N, float J, float kB, float T, float H, float Mu, unsigned int boudary);
    ~ising_model();
    void update();
    float run(int run_step);
	float* M;
    void set_magnet_field(float H);
private:
    int** spin;
    float j, kb, t, h, mu;
    unsigned int size, steps, boundary_condition, current_step;
    bool flip(int* s, unsigned int n);
    void bound_process(unsigned int i, unsigned int j);
    void statistic(unsigned int i);
};