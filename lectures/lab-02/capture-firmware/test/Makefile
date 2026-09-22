# Host build of the Lab 2 firmware against a stubbed HAL. Not for the target.
CFLAGS = -std=c11 -Wall -Wextra -Wno-unused-parameter -I. -I..

lab2_test: runner.c stub.c ../lab2_capture.c main.h ../lab2_capture.h ../lab2_config.h
	gcc $(CFLAGS) -o $@ runner.c stub.c ../lab2_capture.c -lm

.PHONY: check clean
check: lab2_test
	python3 check_lab.py

clean:
	rm -f lab2_test
