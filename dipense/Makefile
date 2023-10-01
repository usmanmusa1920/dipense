# Define the compiler, flags, and libraries
CXX := g++
CXXFLAGS = -Wall -g
# CXXFLAGS = -g -Wall

all: one two

one:
	${CXX} ${CXXFLAGS} -o base dbox/stats/base.cpp
two:
	./base && echo $(CURDIR)
three:
	touch man

clean: 
	$(RM) base
