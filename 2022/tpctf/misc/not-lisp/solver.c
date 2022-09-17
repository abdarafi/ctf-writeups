#include <utility>
#include <vector>
 
std::vector< std::pair<int, int> > factor_table;
void fill_sieve( int n )
{
	factor_table.resize(n+1);
	for( int i = 1; i <= n; ++i )
		factor_table[i] = std::pair<int, int>(i, 1);
	for( int j = 2, j2 = 4; j2 <= n; (j2 += j), (j2 += ++j) ) {
		if (factor_table[j].second == 1) {
			int i = j;
			int ij = j2;
			while (ij <= n) {
				factor_table[ij] = std::pair<int, int>(j, i);
				++i;
				ij += j;
			}
		}
	}
}
 
std::vector<unsigned> powers;
 
template<int dir>
void factor( int num )
{
	while (num != 1) {
		powers[factor_table[num].first] += dir;
		num = factor_table[num].second;
	}
}
 
void calc_catalan(unsigned N)
{
    powers.resize(2*N+1);
    for( unsigned k = 2; k <= N; ++k ) {
         factor<+1>(k+N);
         factor<-1>(k);
    }
}
 
#include <iostream>
#include <cmath>
    int main(void)
    {
        fill_sieve(20000);
        unsigned N = 10000;
        unsigned long long M = 1000;
        calc_catalan(N);
        char* sep = "";
        unsigned long long result = 1;
        for( unsigned i = 0; i < powers.size(); ++i ) {
            while (powers[i]--) {
                result *= i;
                result %= M;
            }
        }
        std::cout << "Catalan(" << N << ") modulo " << M << " = " << result << "\n\n";
    }