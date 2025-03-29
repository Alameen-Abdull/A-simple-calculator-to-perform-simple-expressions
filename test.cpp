#include <iostream>
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(10, 20);
    std::cout << "The sum of 10 and 20 is: " << result << std::endl;
    return 0;
}
