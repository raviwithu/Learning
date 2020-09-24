# LLVM

int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size)

clang -fsanitize=fuzzer,address coverage.c -o coverage

./coverage


./coverage seed=1

#parallelize 
./coverage -workers=6 -job=6