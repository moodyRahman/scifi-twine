out = ""
copy = """.fade{n}{{\nopacity: 0.0;\nanimation: example {n}s 1;\nanimation-fill-mode: forwards;\n}}\n"""

for x in range(6, 100):
    out = out + "\n\n" + copy.format(n=str(x))


print(out)
a="sdfsdfsfds"
