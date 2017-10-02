#
# Makefile
#
# Computer Science 50
# Problem Set 3
#

all: find generate

find: find.c helpers.c helpers.h
	clang -Wall -Werror -o find.run find.c helpers.c -lm

generate: generate.c
	clang -Wall -Werror -o generate.run generate.c -lm

clean:
	rm -f *.run
