#!/usr/bin/python3
import hidden_4


def principal():
    for i in dir(hidden_4):
	if not (i[0] == '_' and i[i] == '_'):
	    print(i)


if __name__ == "__main__":
    principal()
