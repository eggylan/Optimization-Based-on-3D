#pragma GCC optimize(3,"Ofast","inline")
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <stdexcept>

struct Coord {
    int x, y, z;
    bool operator<(const Coord& other) const {
        if (x != other.x) return x < other.x;
        if (y != other.y) return y < other.y;
        return z < other.z;
    }
};

struct FillResult {
    std::vector<std::string> fill_commands;
    std::vector<std::string> setblock_commands;
    int block_count_3d = 0;
    int block_count_2d = 0;
    int block_count_1d = 0;
    int single_block_count = 0;
    int original_command_count = 0;
};

std::vector<std::string> split_string(const std::string& s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        if (!token.empty()) {
            tokens.push_back(token);
        }
    }
    return tokens;
}

std::string join_strings(const std::vector<std::string>& parts, size_t start) {
    std::string result;
    for (size_t i = start; i < parts.size(); ++i) {
        if (i != start) result += " ";
        result += parts[i];
    }
    return result;
}

int parse_coordinate(const std::string& s) {
    if (s.empty()) return 0;
    if (s[0] == '~') {
        return s.size() > 1 ? std::stoi(s.substr(1)) : 0;
    }
    return std::stoi(s);
}

bool is_continuous_region(const std::map<Coord, std::pair<std::string, std::string>>& blocks,
                         int x1, int y1, int z1,
                         int x2, int y2, int z2,
                         const std::string& block_name,
                         const std::string& state_string) {
    for (int x = x1; x <= x2; ++x) {
        for (int y = y1; y <= y2; ++y) {
            for (int z = z1; z <= z2; ++z) {
                Coord coord{x, y, z};
                auto it = blocks.find(coord);
                if (it == blocks.end() || 
                    it->second.first != block_name || 
                    it->second.second != state_string) {
                    return false;
                }
            }
        }
    }
    return true;
}

struct Region { Coord start, end; };

Region find_largest_region(const std::map<Coord, std::pair<std::string, std::string>>& blocks,
                           Coord start, const std::string& block_name, const std::string& state_string) {
    int x = start.x, y = start.y, z = start.z;
    int x_end = x, y_end = y, z_end = z;

    while (is_continuous_region(blocks, x, y, z, x_end + 1, y_end, z_end, block_name, state_string)) {
        x_end++;
    }
    while (is_continuous_region(blocks, x, y, z, x_end, y_end + 1, z_end, block_name, state_string)) {
        y_end++;
    }
    while (is_continuous_region(blocks, x, y, z, x_end, y_end, z_end + 1, block_name, state_string)) {
        z_end++;
    }

    return { {x, y, z}, {x_end, y_end, z_end} };
}

std::vector<std::string> split_fill_command(Coord start, Coord end,
                                           const std::string& block_name,
                                           const std::string& state_string) {
    int x1 = start.x, y1 = start.y, z1 = start.z;
    int x2 = end.x, y2 = end.y, z2 = end.z;
    int block_count = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1);
    
    if (block_count <= 32767) {
        std::string cmd = "fill ~" + std::to_string(x1) + " ~" + std::to_string(y1) + 
                         " ~" + std::to_string(z1) + " ~" + std::to_string(x2) + 
                         " ~" + std::to_string(y2) + " ~" + std::to_string(z2) + " " + block_name;
        if (!state_string.empty()) cmd += " " + state_string;
        return {cmd};
    }

    std::vector<std::string> commands;
    int step = std::max(1, static_cast<int>(std::pow(block_count, 1.0/3)));

    for (int x = x1; x <= x2; x += step) {
        for (int y = y1; y <= y2; y += step) {
            for (int z = z1; z <= z2; z += step) {
                int sub_x2 = std::min(x + step - 1, x2);
                int sub_y2 = std::min(y + step - 1, y2);
                int sub_z2 = std::min(z + step - 1, z2);
                auto sub_commands = split_fill_command({x, y, z}, {sub_x2, sub_y2, sub_z2}, block_name, state_string);
                commands.insert(commands.end(), sub_commands.begin(), sub_commands.end());
            }
        }
    }
    return commands;
}

FillResult find_fill_regions(const std::map<Coord, std::pair<std::string, std::string>>& blocks) {
    FillResult result;
    std::set<Coord> visited;

    for (const auto& entry : blocks) {
        const Coord& coord = entry.first;
        if (visited.count(coord)) continue;

        const std::string& block_name = entry.second.first;
        const std::string& state_string = entry.second.second;

        Region region = find_largest_region(blocks, coord, block_name, state_string);
        Coord start = region.start;
        Coord end = region.end;

        int region_size = (end.x - start.x + 1) * (end.y - start.y + 1) * (end.z - start.z + 1);

        if (region_size > 1) {
            auto commands = split_fill_command(start, end, block_name, state_string);
            result.fill_commands.insert(result.fill_commands.end(), commands.begin(), commands.end());

            int dx = end.x - start.x + 1;
            int dy = end.y - start.y + 1;
            int dz = end.z - start.z + 1;

            if (dx > 1 && dy > 1 && dz > 1) {
                result.block_count_3d += region_size;
            } else if ((dx > 1 && dy > 1) || (dx > 1 && dz > 1) || (dy > 1 && dz > 1)) {
                result.block_count_2d += region_size;
            } else {
                result.block_count_1d += region_size;
            }
        } else {
            result.single_block_count++;
            std::string cmd = "setblock ~" + std::to_string(coord.x) + " ~" + 
                             std::to_string(coord.y) + " ~" + std::to_string(coord.z) + 
                             " " + block_name;
            if (!state_string.empty()) cmd += " " + state_string;
            result.setblock_commands.push_back(cmd);
        }

        for (int x = start.x; x <= end.x; x++) {
            for (int y = start.y; y <= end.y; y++) {
                for (int z = start.z; z <= end.z; z++) {
                    visited.insert({x, y, z});
                }
            }
        }
    }
    return result;
}

FillResult optimize_mcfunction(const std::string& input_file, const std::string& output_file) {
    std::map<Coord, std::pair<std::string, std::string>> blocks;
    int original_count = 0;

    std::ifstream in(input_file);
    if (!in) throw std::runtime_error("Failed to open input file.");

    std::string line;
    while (std::getline(in, line)) {
        original_count++;
        if (line.find("setblock") == 0) {
            auto parts = split_string(line, ' ');
            if (parts.size() < 5) continue;

            int x = parse_coordinate(parts[1]);
            int y = parse_coordinate(parts[2]);
            int z = parse_coordinate(parts[3]);
            std::string block_name = parts[4];
            std::string state = join_strings(parts, 5);

            blocks[{x, y, z}] = {block_name, state};
        }
    }
    in.close();

    FillResult result = find_fill_regions(blocks);
    result.original_command_count = original_count;

    std::ofstream out(output_file);
    if (!out) throw std::runtime_error("Failed to create output file.");

    for (const auto& cmd : result.fill_commands) out << cmd << "\n";
    for (const auto& cmd : result.setblock_commands) out << cmd << "\n";
    out.close();

    return result;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input file> <output file>\n";
        return 1;
    }

    try {
        FillResult result = optimize_mcfunction(argv[1], argv[2]);
        
        std::cout << "[3D] Command counts: " << result.block_count_3d << "\n"
                  << "[2D] Command counts: " << result.block_count_2d << "\n"
                  << "[1D] Command counts: " << result.block_count_1d << "\n"
                  << "[setblock counts]: " << result.single_block_count << "\n"
                  << "Original command counts: " << result.original_command_count << "\n"
                  << "After optimization: " << result.fill_commands.size() + result.setblock_commands.size() << "\n";
    } catch (const std::exception& e) {
        std::cerr << "ERROR:" << e.what() << "\n";
        return 1;
    }
    return 0;
}