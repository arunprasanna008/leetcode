"""
Verifies the actual output against the expected output
"""
    
def verify(actual_output, expected_output):
    try:
        assert (actual_output == expected_output)
        print("correct solution: %s" % actual_output)
    except AssertionError:
        print ("wrong solution \n actual: %s \n expected: %s" % (actual_output, expected_output))