// pi counter
// author: grafstor
// date: 23.06.2020

#include <iostream>
#include <experimental/random>
#include <cmath>

int main()
{
	int in_target = 0;
	int field = 500;
	int interations = 10000*10000;
	int show_each = 1000*1000;

	int x;
	int y;
	float length;
	float result;

	for (int i = 1; i < interations; i++)
	{
	    x = std::experimental::randint(-field+1, field);
	    y = std::experimental::randint(-field+1, field);

	    length = sqrt(x*x + y*y);

	    if (length < field)
	    {
	    	in_target++;
	    }

	    if (i % show_each == 0)
	    {
	    	result = (float)in_target / (float)i;
	    	result = result * 4.0;

	    	std::cout << result << std::endl;
	    }
	}

	return 0;
}