#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct Box {
  int l, w, h;
};

Box parse_box(const std::string &s) {
  Box box;
  char sep;

  std::stringstream ss(s);
  ss >> box.l >> sep >> box.w >> sep >> box.h;

  return box;
}

void p1_2(std::vector<Box> boxes) {
  int out1 = 0;
  int out2 = 0;

  for (Box box : boxes) {
    out1 += 2 * box.l * box.w + 2 * box.w * box.h + 2 * box.h * box.l;
    out1 += std::min({box.l * box.w, box.w * box.h, box.h * box.l});

    out2 += box.l * box.w * box.h;
    out2 += 2 * std::min({box.l + box.w, box.w + box.h, box.h + box.l});
  }

  std::cout << "Part1: " << out1 << std::endl;
  std::cout << "Part2: " << out2 << std::endl;
}

int main() {
  std::ifstream file(".input/day02");
  std::string line;

  std::vector<Box> boxes{};
  boxes.reserve(1000);

  while (std::getline(file, line)) {
    boxes.emplace_back(parse_box(line));
  }

  p1_2(boxes);

  return 1;
}
