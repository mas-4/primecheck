#include <stdio.h>
#include <math.h>

int isprime(int n) {
  if (n <= 3) return n > 1;
  if (n % 2 == 0 || n % 3 == 0) return 0;
  double lim = sqrt(n);
  int i = 5;
  while (i <= lim) {
    if (n % i == 0 || (n % (i + 2)) == 0) {
        return 0;
    }
    i += 6;
  }
  return 1;
}

int main() {
  for (int i = 0; i < 100; i++) {
    printf("%d: %d\n", i, isprime(i));
  }
  return 0;
}
