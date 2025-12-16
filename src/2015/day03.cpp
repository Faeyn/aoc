#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>

using Coord = std::array<int, 2>;
constexpr Coord operator+(const Coord &a, const Coord &b) {
  return {a[0] + b[0], a[1] + b[1]};
}

const std::unordered_map<char, Coord> dirs = {
    {'v', {1, 0}}, {'^', {-1, 0}}, {'<', {0, -1}}, {'>', {0, 1}}};

size_t part1(std::string &data) {
  Coord current_coord{0, 0};
  std::set<Coord> houses{{0, 0}};

  for (char c : data) {
    if (auto it = dirs.find(c); it != dirs.end()) {
      current_coord = current_coord + it->second;
      houses.insert(current_coord);
    }
  }
  return houses.size();
}

size_t part2(std::string &data) {
  Coord robo{0, 0};
  Coord santa{0, 0};

  std::set<Coord> houses{{0, 0}};

  for (std::size_t i = 0; i < data.size(); ++i) {
    if (auto it = dirs.find(data[i]); it != dirs.end()) {
      Coord &mover = (i % 2 == 0) ? robo : santa;
      mover = mover + it->second;
      houses.insert(mover);
    }
  }
  return houses.size();
}

int main() {
  std::ifstream file(".input/day03");
  if (!file) {
    std::cerr << "File couldn't be opened\n";
    return 1;
  }

  std::string data;
  std::getline(file, data);
  struct CoordHash {
    std::size_t operator()(const Coord &c) const noexcept {
      // Simple and effective hash combine
      std::size_t h1 = std::hash<int>{}(c.row);
      std::size_t h2 = std::hash<int>{}(c.col);
      return h1 ^ (h2 << 1);
    }
  };
  std::cout << "Part1: " << part1(data) << '\n';
  std::cout << "Part2: " << part2(data);

  return 0;
}
