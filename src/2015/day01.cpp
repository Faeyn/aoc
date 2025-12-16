#include <fstream>
#include <iostream>
#include <string>

void p1(std::string);
void p2(std::string);

int main() {
  std::ifstream file(".input/day01");
  std::string data;
  std::getline(file, data);
  // std::cout << data;

  p1(data);
  p2(data);

  return 0;
}

void p1(std::string data) {
  int count = 0;
  for (char c : data) {
    if ('(' == c) {
      count++;
    } else {
      count--;
    }
  }
  std::cout << count << '\n';
  return;
}

void p2(std::string data) {
  int i = 0;
  int count = 0;

  for (char c : data) {
    i++;
    if ('(' == c) {
      count++;
    } else {
      count--;
    }

    if (count < 0) {
      std::cout << i << '\n';
      return;
    }
  }
}
