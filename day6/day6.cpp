#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <algorithm>

std::string parse_data(const std::string filename){
    std::string line;
    std::ifstream infile(filename);
    
    infile >> line;

    return line;
}

void print(std::list<char> mylist){
    std::list<char>::iterator it;
    std::cout << "{";
    for (it = mylist.begin(); it != mylist.end(); ++it)
        std::cout << ' ' << *it;
    std::cout << " }\n";
}

int get_start_of_packet(const std::string data, int num_distinct_chars){
    std::list<char> my_list;
    for(int i = 0; i < data.size(); i++){
        if (my_list.size() == num_distinct_chars)
        {
            return i;
        }
        while (std::find(my_list.begin(), my_list.end(), data[i]) != my_list.end()){
            my_list.pop_front();
        }
        my_list.push_back(data[i]);
    }
    return 0;
}

int main(){
    std::string data = parse_data("input.txt");
    int num_distinct_chars = 4;
    std::cout<< "The start of the data packet occurs after " << get_start_of_packet(data, num_distinct_chars) << " characters." << std::endl;
    num_distinct_chars = 14;
    std::cout << "The start of the data packet occurs after " << get_start_of_packet(data, num_distinct_chars) << " characters." << std::endl;
    return 0;
}