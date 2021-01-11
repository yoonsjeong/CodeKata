

""" 
helper('hello', ['b']) -> '<b>hello</b>'
helper('hello', ['b', 's']) -> '<s><b>hello</b></s>'
"""


def helper(text, fmt):
    out = text
    for i in fmt:
        out = "<{1}>{0}</{1}>".format(out, i)
    return out

def start(fmt):
    return "<{}>".format(fmt)
def end(fmt):
    return "</{}>".format(fmt)


"""
Given text string and different formats with indexes indicated 
(ie. bold:[0.3], italics[2,4], underline:[2,6]) return formatted 
text with html tags representing start and end of different formats 
"""


# def htmlify(text, fmt):
#     n = len(text)
#     store = [[] for _ in range(n)]
#     for i in range(n):
#         for j in fmt:
#             if j[1] <= i <= j[2]:
#                 store[i].append(j[0])

#     out = ""
#     to_fmt = ""
#     fmt_with = []
#     for k in range(n):
#         to_fmt += text[k]
#         fmt_with += store[k]
#         if k != n-1 and store[k] == store[k+1]:
#             continue
#         out += helper(to_fmt, store[k])
#         to_fmt = ""

#     return out

def htmlify(text, fmt):
    n = len(text)
    store = [[] for _ in range(n)]
    for i in range(n):
        for j in fmt:
            if j[1] <= i < j[2]:
                store[i].append(j[0])
    print(store)
    out = ""
    in_progress = []
    end_everything = False
    for i in range(n):
        fmt_arr = store[i]
        for ip in in_progress:
            if ip in fmt_arr:
                continue
            else:
                end_everything = True

        if end_everything:
            while in_progress != []:
                out += end(in_progress.pop())
            end_everything = False

        for f in fmt_arr:
            if f in in_progress:
                continue
            else:
                out += start(f)
                in_progress.append(f)
        out += text[i]
    return out

bold = ("b", 0, 4)
italic = ("i", 2, 6)
strike = ("s", 0, 6)

text = "ABCDEFGHIJ"
formatting = [bold, italic, strike]
output = htmlify(text, formatting)
print(output)
# should be <b>AB<i>CD</i></b><i>EF</i>GHIJ
