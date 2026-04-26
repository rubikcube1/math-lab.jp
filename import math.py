#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

vector<int> spf;

void build_spf(int n) {
    if (n < spf.size()) return;
    spf.resize(n + 1);
    for (int i = 0; i <= n; ++i) spf[i] = i;
    for (int i = 2; i * i <= n; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= n; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

long long get_jump(int k) {
    if (k < 2) return 0;
    int temp = k;
    long long factor_sum = 0;
    int factor_count = 0;
    while (temp > 1) {
        factor_sum += spf[temp];
        temp /= spf[temp];
        factor_count++;
    }
    if (factor_count == 1) return 1;
    return factor_sum;
}

int main() {
    int start_x, end_x;
    cerr << "計算開始値 (x) : ";
    cin >> start_x;
    cerr << "計算終了値 (x) : ";
    cin >> end_x;

    if (start_x < 2) start_x = 2;
    build_spf(end_x);

    long long D_val = 0;
    // D(x)の初期累積（開始値の前まで）
    for (int i = 2; i < start_x; ++i) {
        bool is_p = (spf[i] == i);
        D_val += (get_jump(i) - (is_p ? 1 : 0));
    }

    // ヘッダー表示
    cout << "x,D(x),is_prime,delta,match" << endl;

    for (int x = start_x; x <= end_x; ++x) {
        bool is_p = (spf[x] == x);
        long long j = get_jump(x);
        
        long long D_prev = D_val;
        D_val += (j - (is_p ? 1 : 0));
        
        long long delta = D_val - D_prev;
        bool match = ((delta == 0) == is_p);

        // 中略なしで一行ずつ出力
        cout << x << "," 
             << D_val << "," 
             << (is_p ? "True" : "False") << "," 
             << delta << ","
             << (match ? "OK" : "NG") << endl;
    }

    return 0;
}