CFLAGS = -Wall -Wno-write-strings -DSWAP_BYTES -g -fdiagnostics-show-option
#LFLAGS = -Llib -L$(ROOTSYS)/lib -L$(RATROOT)/lib
LFLAGS = -L$(ROOTSYS)/lib -L$(RATROOT)/lib


INCLUDES= `root-config --cflags --glibs` \
-Iinclude \
-Iinclude/RAT \
-I/Users/kate/snoing/install/rat-dev/include \
-I/Users/kate/snoing/install/rat-dev/include/RAT \
-I/Users/kate/snoing/install/rat-dev/include/RAT/DS \
-lRATEvent_Darwin

#-Iinclude \
-Iinclude/RAT \
-I/data/snoplus/shared/code/snoing/x11install/rat-4.5.0/include \
-I/data/snoplus/shared/code/snoing/x11install/rat-4.5.0/include/RAT \
-I/data/snoplus/shared/code/snoing/x11install/rat-4.5.0/include/RAT/DS \
-lRATEvent_Linux

CC= g++

SOURCES=plotCrateViewPed.cc

OBJECTS=$(SOURCES: .cc*=)

EXECUTABLE=../libexec/plotCrateViewPed
.PHONY: all


all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(CFLAGS) $(LFLAGS) -L/usr/lib -o $@ $(OBJECTS) $(INCLUDES)

