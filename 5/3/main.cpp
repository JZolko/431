#include <vector>
#include <iostream>



int main(){

	// get an int input from the user
	int number_of_test_cases;
    int brick_types, target_length;

	std::cin >> number_of_test_cases;


    for(int first = 0; first < number_of_test_cases; first++){
        // get an int pair from user
        std::cin >> brick_types >> target_length;
        // make an int vector of size N
        std::vector<int> bricks;
        for(int second = 0; second < brick_types; second++){
            // add an int to the vector
            int temp;
            std::cin >> temp;
            bricks.push_back(temp);
        }

        // make a vector of 0s with size L + 1
        std::vector<int> table;
        for(int zeros = 0; zeros < target_length + 1; zeros++)
            table.push_back(0);

        table[0] = 1;

        for(int i = 0; i < brick_types; i++)
            for(int j = table[i]; j <= target_length ; j--)
                table[j] = table[j] + table[j - bricks[i]];

        if(table[-1])
            std::cout << table[-1] % 1000000009 << std::endl;




    }




	return 0;
}
