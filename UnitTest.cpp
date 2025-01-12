#include <vector>
#include <iostream>
#include "Solution.hpp"

struct testcase { string s, k; bool output; };

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;
public:
    UnitTest() {
        testcases = {{"))()))", "010100", true},
                     {"()()", "0000", true},
                     {")", "0", false}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            bool result = obj.canBeValid(testcases[i].s, testcases[i].k);
            cout << "TestCase " << i+1 << ": " << ((result == testcases[i].output) ? "passed":"failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}