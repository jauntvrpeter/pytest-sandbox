Pytest-Sandbox
==============

This is a sample project to do exploratory testing of the capabilities of pytest. Some folks might find this helpful if you're delving into pytest, so I will continually update the README for a summarization of operations that can be used

## Quick Commands

    cd tests
    py.test
    py.test -c conftest.py
    py.test --markers
    py.test -lvv -m smoke
    py.test -lvv -m smoke -k world1
    py.test -lvv -m smoke test_hello_world.py
    py.test -lvv -m foobar