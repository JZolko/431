#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <list>
#include <iostream>
#include <sstream>



int main(){
	int N = scanf("%d", &N);
	std::string line;
	for(int i = 0; i < N; i++){
		std::getline(std::cin, line);
		std::istringstream iss(line);
		std::string word;
		while(iss >> word){
			std::cout << word << std::endl;
		}
	}
	return 0;
}
