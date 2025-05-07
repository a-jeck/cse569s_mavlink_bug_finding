# Fuzzing SerenityOS

This directory contains instructions and contents for executing fuzzing of the Serenity operating system's ELF loader functionality.

## Clone the Source Code

All source files and contents related to the host-based interface exist in the repo [here](https://github.com/SerenityOS/serenity). 
Clone via 

`git clone https://github.com/SerenityOS/serenity`.

## Setup Our Fuzzer and Corpus

Our seed corpus, auto-generated during the first run of Serenity's unedited ELF fuzzer, is available as a zip in this repository. Clone/copy this somewhere reachable by binaries in the serenity project and unzip.

The fuzz src code is located at 

`<path-to-serenity>/Meta/Lagom/Fuzzers/FuzzELF.cpp`

Replace the file there with [our fuzz code](./FuzzELF.cpp).

## Build and Run

Run 

`<path-to-serenity>/Meta/Lagom/BuildFuzzers.sh`

then 

`<path-to-serenity>/Meta/Lagom/Build/lagom-fuzzers/bin/FuzzELF -artifact_prefix=crashes/ <path-to-unzipped-corpus>`

Crashing inputs will appear in ./crashes relative to wherever you're executing from.
