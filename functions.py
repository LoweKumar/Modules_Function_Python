# defining multiple arguments function

# def multipleArgs(*args, sep=' ', end='\n', file=None, flush=flush):
#     text = ""
#     for arg in args:
#         text += str(arg) + " "
#
#     print(text, end=end, file=file, flush=flush) # returns strings in normal form

def multipleArgs(*args):
    text = "".join(str(args))

    print(text) # returns strings in tuple form


multipleArgs("Tim","Buchalka","Python","Series","udemy")


