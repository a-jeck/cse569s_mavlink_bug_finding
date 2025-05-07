**Folder Overview:**
This folder contains the scripts used to generate the test harness and seeds used for fuzzing MavLink with AFL++. The folder generating_code contains a script that, given a MavLink message.xml file (such as common.xml provided here), generates switch-case cases for each message type. The folder generating_message_encoding contains a script that, given messages.xml, generates functions that can be used to generate messages of that type to use as seeds for fuzzing.

udp_example.c is a test harness partially generated with the script in generating_code that can be used as a test harness for fuzzing AFL++. 

Common.xml is extracted from the the common message set XML defined here: https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml

**Fuzzing MavLink with AFL++**
1. Clone this repository: https://github.com/WUSTL-CSPL/mavlink_fuzz_CSE569
2. Replace `udp_example.c` with the `udp_example.c` file from this repository. 
3. `mavlink_fuzz_CSE569/examples/c` contains a `CMakeLists.txt`. Replace its text with the `CMakeLists.txt` defined in this README.
4. From `mavlink_fuzz_CSE569/examples/c`, run `cmake -Bbuild -H. -DCMAKE_PREFIX_PATH=$(pwd)/../../install` then `cmake --build build` to build the test harness
5. Generate seeds in this repository, then copy them to `mavlink_fuzz_CSE569/examples/c/input`
6. Begin fuzzing with `AFL_USE_ASAN=1 AFL_USE_UBSAN=1 afl-fuzz -i input -o output -- ./build/udp_example @@`. If AFL++ gives you a warning about your OS improperly storing crashes, run `echo core | sudo tee /proc/sys/kernel/core_pattern`.

**Fuzzing with Multiple Cores**
1. Running AFL above runs a single instances on one core, but we can run more instances with AFL++.
2. On the first instance of the fuzzer (the master), include `-M fuzzer00` when starting AFL++.
3. Open new terminal windows and run the same command above (slave instances), including `-S fuzzer01` when starting AFL++ (increment the number each time).
4. Depending on your machine, leave a couple cores free to maintain system stability. I fuzzed on 10/12 virtual cores (1 master, 9 slaves) without crashing.


`CMakeLists.txt`:
```
cmake_minimum_required(VERSION 3.13)


set(CMAKE_C_COMPILER   afl-clang-fast)     
set(CMAKE_CXX_COMPILER afl-clang-fast++)  

project(udp_example C)                   

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}   -fsanitize=address -fsanitize=undefined -g -O2")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address -fsanitize=undefined -g -O2")

set(CMAKE_C_STANDARD 11)

find_package(MAVLink REQUIRED)

add_executable(udp_example udp_example.c)
target_link_libraries(udp_example PRIVATE MAVLink::mavlink)

