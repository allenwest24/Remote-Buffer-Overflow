all:
	gcc -m32 -fno-stack-protector -z execstack -o server server.c
clean:
	rm -f *.o 
