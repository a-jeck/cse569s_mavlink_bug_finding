**Folder Overview:**
This folder contains a copy of the FastFEC repository (https://github.com/washingtonpost/FastFEC) and a script, `downloader.py`, for downloading .fec files. 

**Downloading Seeds and Setup** 
1. The FastFEC folder contains two scripts: `build_fuzz.sh` and `build_tester.sh`. Run `build_fuzz.sh` to instrument the test harness and compile it for AFL++. If you would like to test individual FEC files with the parsing logic, `'build_tester.sh` to build the harness with ASan and UBSan without instrumentation for AFL++.
2. Download 10,000 FEC files by running `python3 downloader.py`. This will create a folder inputs with all .fec files.
3. Run `afl-cmin -i input -o in_min -T all -- ./FastFEC/harness @@` to minimize the 10,000 .fec files into unique cases that AFL++ finds the best for fuzzing.
4. Move the minimized input folder, `in_min`, to `./FastFEC/in_min`.

**Fixing Bugs in FastFEC** 
1. As described in our report, there are many bugs present in FastFEC. There is one bug, however, that will immediately cause UBSan to crash the program, even when testing with .fec files. 
2. This issue has been fixed in the source code. The fix is present in line 21 of buffer.c (and buffer.h) and is labelled bug fix #1. Other bugs described in the report have commented out fixes. These are present at line 91 of encoding.c and line 197 of csv.c.

**Fuzzing FastFEC with AFL++**
1. Run the following commands:
```
cd ./FastFEC
AFL_USE_ASAN=1 AFL_USE_UBSAN=1 afl-fuzz -i in_min -o output -- ./harness @@
```
2. If you removed the bug fix described in the section above, the fuzzer likely will not run. Depending on the .fec files you download, it is possible other test cases fail and the program will need to be fixed.

**Fuzzing with Multiple Cores**
1. Running AFL above runs a single instances on one core, but we can run more instances with AFL++.
2. On the first instance of the fuzzer (the master), include `-M fuzzer00` when starting AFL++.
3. Open new terminal windows and run the same command above (slave instances), including `-S fuzzer01` when starting AFL++ (increment the number each time).
4. Depending on your machine, leave a couple cores free to maintain system stability. I fuzzed on 10/12 virtual cores (1 master, 9 slaves) without crashing.
