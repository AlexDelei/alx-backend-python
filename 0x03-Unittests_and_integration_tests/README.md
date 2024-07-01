### Unittests and Integration Tests
**Unittest** - is the process of testing that a particular function returns expected results for different set of inputs and corner cases.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected ?

**Intergration** - this test aims to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

------------
**How to implement a test case**
------------
- A testcase is created by subclassing ```unittest.TestCase```. The three individual tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.

- The crux of each test is a call to ```assertEqual()``` to check for an expected result; ```assertTrue()``` or ```assertFalse()``` to verify a condition; or ```assertRaises()``` to verify that a specific exception gets raised. These methods are used instead of the _assert_ statement so the test runner can accumulate all test results and produce a report.

- The **setUp()** and **tearDown()** methods allow you to define instructions that will be executed before and after each test method.


#### Command Line options
**Unittests** supports these command-line options:

- **-b, --buffer**
The standard output and standard error streams are buffered during the test run. Output during a passing test is discarded. Output is echoed normally on test fail or error and is added to the failure messages.
- **-c, --catch**
Control-C during the test run waits for the current test to end and then reports all the results so far. A second Control-C raises the normal KeyboardInterrupt exception.

See Signal Handling for the functions that provide this functionality.
- **-f, --failfast**
Stop the test run on the first error or failure.
- **-k**
Only run test methods and classes that match the pattern or substring. This option may be used multiple times, in which case all test cases that match any of the given patterns are included.

Patterns that contain a wildcard character (*) are matched against the test name using fnmatch.fnmatchcase(); otherwise simple case-sensitive substring matching is used.

Patterns are matched against the fully qualified test method name as imported by the test loader.

For example, -k foo matches foo_tests.SomeTest.test_something, bar_tests.SomeTest.test_foo, but not bar_tests.FooTest.test_something.
- **--locals**
Show local variables in tracebacks.
- **--durations N**
Show the N slowest test cases (N=0 for all).

#### Test Discovery
- **-v, --verbose**
Verbose output
- **-s, --start-directory directory**
Directory to start discovery (. default)
**-p, --pattern pattern**
Pattern to match test files (test*.py default)
**-t, --top-level-directory directory**
Top level directory of project (defaults to start directory)