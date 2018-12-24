import sys


def usage():
    print "BHP net tool"
    print
    print "Usage: 04.Netcat -t target_host -p port"
    print "-l --listen						-listen on [host]:[port]  for incoming connections"
    print "-e --execute=file_to_run				-execute the given file upon receiving a connection "
    print "-c --command						-initialize a command shell"
    print "-u --upload						-upon receiving a connection upload a file and write to [destination]"
    print
    sys.exit(0)
