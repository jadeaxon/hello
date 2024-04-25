# After installing a new package, you need to restart Visual Studio Code.
# Else, you'll get a warning about the module being missing.
import matplotlib.pyplot as pp

squares = [x ** 2 for x in range(0, 6)]
# fig is all the plots; ax is a single plot
fig, ax = pp.subplots()
ax.plot(squares, linewidth=3)
ax.set_title("Squares", fontsize=14)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square", fontsize=14)
ax.tick_params(labelsize=14)
print(pp.style.available)
pp.style.use('seaborn-v0_8')
pp.show()

