#include <vector>
#include <iostream>
#include <bits/stdc++.h>




int main(){
	
	const int64_t SOME_REALLY_BIG_NUMBER = 1000000009;
	
	int64_t number_of_test_cases;
    int64_t brick_types, target_length;

	std::cin >> number_of_test_cases;


    for(int64_t first = 0; first < number_of_test_cases; first++){

        std::cin >> brick_types >> target_length;

        int64_t bricks[brick_types];
        for(int64_t brick = 0; brick < brick_types; brick++){

            int64_t temp;
            std::cin >> temp;
            bricks[brick] = temp;
        }

       	
		/** let the fun begin **/
		int64_t table[target_length + 1];
		memset(table, 0, sizeof(table));

        table[0] = 1;


        for(int64_t i = 1; i <= target_length; i++)
			for(auto brick : bricks)
				if(i - brick >= 0)
	            	table[i] += table[i - brick] % SOME_REALLY_BIG_NUMBER;


        std::cout << table[target_length] % SOME_REALLY_BIG_NUMBER << std::endl;
		//std::cout << std::endl;
		//std::cout << table[target_length] << std::endl;


		//for (int64_t i = 0; i <= target_length; i++)
		//	std::cout << table[i] << " ";
		//std::cout << std::endl;
    }
	return 0;
	/** There was no fun to be had **/
}
