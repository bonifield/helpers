#!/usr/bin/env python3

# https://github.com/xflr6/graphviz
# some lines in this script taken exactly from the above repo's examples
# python3 -m pip install graphviz
import graphviz

dot = graphviz.Digraph(comment="The Round Table")
#dot.format = "pdf" # default
dot.format = "png"
#dot.format = "svg"
dot.attr(rankdir="LR", size="8,5") # default TB (top-to-bottom) if .attr omitted

dot.node("A", "King Arthur")  # doctest: +NO_EXE
dot.node("B", "Sir Bedevere the Wise")
dot.node("L", "Sir Lancelot the Brave")

dot.edges(["AB", "AL"])
dot.edge("B", "L", constraint="false")

print(dot.source)

dot.render("doctest-output/round-table.gv").replace("\\", "/")
