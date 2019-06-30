#include <iostream>
using namespace std;

class Test
{
    public:
        Test(int a, int b);
        Test();
    private:
        char c;
};

Test::Test(int a, int b)
{
    int x = a;
    int y = b;
    cout << x << y << endl;
}

Test::Test()
{
    cout << "no params" << endl;
}

int main()
{
    int a = 0;
    do
    {
        a++;
        cout << a << endl;
    }
    while (a<11);
    Test Test2(4, 5);

    return 0;

}