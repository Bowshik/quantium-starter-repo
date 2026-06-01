#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the test suite
pytest test_app.py -v

# Return exit code (0 = pass, 1 = fail)
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi