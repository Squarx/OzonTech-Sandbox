#include <iostream>
#include <vector>
#include <string>

int common_suffix(const std::string& str1, const std::string& str2) {
    if (str1 == str2) {
        return 0;
    }
    int l1 = static_cast<int>(str1.length()) - 1;
    int l2 = static_cast<int>(str2.length()) - 1;
    int suffix = 0;
    while (l1 >= 0 && l2 >= 0 && str1[l1] == str2[l2]) {
        ++suffix;
        --l1;
        --l2;
    }
    return suffix;
}

int main() {
    int cnt_dict;
    std::cin >> cnt_dict;
    std::vector<std::string> words_dict(cnt_dict + 10);
    for (int i = 0; i < cnt_dict; ++i) {
        std::cin >> words_dict[i];
    }
    int cnt_w;
    std::cin >> cnt_w;
    for (int i = 0; i < cnt_w; ++i) {
        std::string word;
        std::cin >> word;
        int max_len = 0;
        int max_id = 0;
        for (int id = 0; id < cnt_dict; ++id) {
            int l = common_suffix(words_dict[id], word);
            if (l > max_len) {
                max_len = l;
                max_id = id;
            }
        }
        std::cout << words_dict[max_id] << '\n';
    }

    return 0;
}
