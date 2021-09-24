#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

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

char* erat(int n) {
  char* sieve;
  if (n < 2) return NULL;
  int m = (int) sqrt((double) n);
  sieve = calloc(n+1, sizeof(sieve));
  for (int i=0; i<=n; i++) sieve[i] = 1;
  sieve[0] = sieve[1] = 0;
  sieve[2] = 1;
  /* For every i>=2, if it is prime, mark every multiple of it as not prime. */
  /*
  for (int i=2; i<=m; i++)
    if (sieve[i]==1)
      for (int j=2*i; j<=n; j+=i)
        sieve[j] = 0;
  */
  return sieve;
}

int main() {
  return 0;
}
