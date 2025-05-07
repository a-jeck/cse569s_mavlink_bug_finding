**Folder Overview:**
This folder contains the scripts used to generate the test harness and seeds used for fuzzing MavLink with AFL++. The folder generating_code contains a script that, given a MavLink message.xml file (such as common.xml provided here), generates switch-case cases for each message type. The folder generating_message_encoding contains a script that, given messages.xml, generates functions that can be used to generate messages of that type to use as seeds for fuzzing.

udp_example.c is a test harness partially generated with the script in generating_code that can be used as a test harness for fuzzing AFL++. 

Common.xml is extracted from the the common message set XML defined here: https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml

**Generating Code and Seeds**
Steps 1-3 are already completed in this repository, but if you would like to rerun it, follow these instructions.
1. First, download pymavlink (suggested: create a virtual enviornment and install via `pip install pymavlink`).
2. Next, we will use `generating_code/generating_harness_cases/generating_harness.py` to generate a test harness. Use the common.xml provided in this repository and run `python3 generating_harness.py path/to/common.xml switch_cases.txt`, This will create a series of switch cases for each message type in common.xml which can replace the switch-case statements udp_example.c. Alternatively, the switch-case statements in udp_example.c already handle all messages from common.xml.
3. Next, we will generate code that can create valid MavLink messages to use as seeds. This file is located in `generating_code/generating_message_encoding/`. Run `python3 gen_encode.py path/to/common.xml logic.txt`, which will generate a series of Python of if-else statements that can generate each type of MavLink message from common.xml. This can then replace the if-else statements in `generating_seeds/message_encode.py`. The current logic of `message_encode.py` already handles all messages from common.xml.
4. Now we can generate seeds. Run `python3 generating_seeds/full_seed_gen.py`, which will create a folder input with a seed of each message type. 

**Fuzzing MavLink with AFL++**
1. Clone this repository: https://github.com/WUSTL-CSPL/mavlink_fuzz_CSE569
2. Replace `examples/c/udp_example.c` with the `udp_example.c` file from this repository. 
3. From the root of the repository, download PyMavLink then build MavLink using the following commands:
```
python3 -m pip install -r pymavlink/requirements.txt
cmake -Bbuild -H. -DCMAKE_INSTALL_PREFIX=install
cmake --build build --target install
```
4. From `mavlink_fuzz_CSE569/examples/c`, run `cmake -Bbuild -H. -DCMAKE_PREFIX_PATH=$(pwd)/../../install` then `cmake --build build` to build the test harness
5. Generate seeds in this repository, then copy them to `mavlink_fuzz_CSE569/examples/c/input`
6. Begin fuzzing with `AFL_USE_ASAN=1 AFL_USE_UBSAN=1 afl-fuzz -i input -o output -- ./build/udp_example @@`. If AFL++ gives you a warning about your OS improperly storing crashes, run `echo core | sudo tee /proc/sys/kernel/core_pattern`.

**Fuzzing with Multiple Cores**
1. Running AFL above runs a single instances on one core, but we can run more instances with AFL++.
2. On the first instance of the fuzzer (the master), include `-M fuzzer00` when starting AFL++.
3. Open new terminal windows and run the same command above (slave instances), including `-S fuzzer01` when starting AFL++ (increment the number each time).
4. Depending on your machine, leave a couple cores free to maintain system stability. I fuzzed on 10/12 virtual cores (1 master, 9 slaves) without crashing.
