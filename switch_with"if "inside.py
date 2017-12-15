def appendCodesToList(indoor, outdoor):
	# helper function to return a list with two strings
	back_end_codes = []
	back_end_codes.append(indoor)
	back_end_codes.append(outdoor)
	return back_end_codes

def switch_demo(argument):
    a = 5
    b = 10
    switcher = {
        1: [ "in", "out"],
        2: (["February","aaa"] if (a>10) else ["hgfng","bbb"]) if a>b else ["aaa", "sss"],

        3: (["March", "nnn"] if (a>10) ) ["mmm", ""]
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return (switcher.get(argument, "Invalid month"))
y = []
y = switch_demo(2)
x = appendCodesToList(y[0], y[1])
print(x)

# x = switch_demo(2)
# print(x)


# def x():
#     return {"a", "b"}
# y = {}
# y =
# print(y[0])
