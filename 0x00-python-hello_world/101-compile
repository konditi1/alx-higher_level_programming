#!/bin/bash

# Extract the filename from the environment variable
filename="${PYFILE##*/}"

# Compile the Python script
echo "Compiling $filename ..."
python3 -m py_compile "$PYFILE" > /dev/null

# Rename the compiled file
compiled_filename="${filename%.*}.pyc"
mv "$filename" "$compiled_filename" 2>/dev/null
