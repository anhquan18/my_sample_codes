CXX=g++
CFLAGS=`pkg-config --cflags opencv`
LIBS=`pkg-config --libs opencv`

mat_show: mat_show.cpp
	 $(CXX) $(CFLAGS) -o $@ $^ $(LIBS)
check: check.cpp
	 $(CXX) $(CFLAGS) -o $@ $^ $(LIBS)
