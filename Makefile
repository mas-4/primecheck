primelib.so:
	gcc -shared -Wl,-soname,primelib -o primelib.so -fPIC primelib.c
