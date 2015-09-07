"""Python parameters example."""

from sys import argv


try:
    s, name, age, work = argv

    print "\n\t____Python Parameters___\n"

    print "This is the list that contains all user arguments\n\t", argv

    print "\nThe first argument is always the script.\n\t", argv[0]

    print "\nThe second argument was your name. Nice to meet you", name

    print "\nThe third argument was your age. Now I know you're", age

    print "\nAnd the last argument was your occupation. Now I know you're", work

    print "\nAnd know I im able to write sentences like this one: "
    print "\tHello", name, "I've seen that you're", age, "and", work
except:
    print "You don't run the program correctly, please read the instrucions"
