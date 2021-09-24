lib:
	gcc -shared -Wl,-soname,primelib -o primelib.so -fPIC primelib.c
clean:
	rm primelib.o primelib.a
