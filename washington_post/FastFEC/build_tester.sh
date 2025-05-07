#!/usr/bin/env bash

# root, target, output
ROOT=$(dirname "$(realpath "$0")")
HARNESS_SRC="$ROOT/harness.c"
OUTBIN="$ROOT/tester"

# compile normally, not for AFL++ 
export CC=clang

# asan and ubsan important to find more interesting crashes
CFLAGS="-fsanitize=address,undefined -g"

# want all files in src except test and wasm files were causing compilation issues
# and were unnecessary. main.c has been replaced by my harness so cut it
CORE_SRC=$(find "$ROOT/src" -maxdepth 1 -name '*.c' \
           ! -name '*test.c' ! -name 'main.c' ! -name 'wasm.c')

# some pcre files needed but others were causing compilation issues
PCRE_SRC=$(find "$ROOT/src/pcre" -name 'pcre_*.c' ! -name '*_test.c')

$CC $CFLAGS \
  -I"$ROOT/src" -I"$ROOT/src/pcre" \
  $CORE_SRC $PCRE_SRC $HARNESS_SRC \
  -o "$OUTBIN" \
  -lcurl -lzstd -lm

echo "built to $OUTBIN"

