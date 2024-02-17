#codigo para ilustrar como encontrar o fator = k
import matplotlib.patches as mpatches

figsize = (7, 7)
colunas = 1
linhas = 1
#Criar os objetos fig e ax
fig, ax = plt.subplots(linhas, colunas, figsize=figsize)

#Quadrado unindo os pontos (-1,-1), (-1,1), (1,1) e (1,-1).
vertices_q = np.array([[-1,-1, 1, 1], [-1, 1, 1, -1]])
quadrado = mpatches.Polygon(vertices_q.T, fc = 'white', ec = 'tab:blue', lw = 1)
ax.add_patch(quadrado)

#Quadrado rotacionado alpha e contraído usando fator = 1/(cos(alpha) + sen(alpha)).
alpha = np.pi/6
fator = 1/(np.cos(alpha) + np.sin(alpha))
vertices_q1 = fator*R(alpha)@vertices_q    
quadrado1 = mpatches.Polygon(vertices_q1.T, fc = 'white', ec = 'tab:green', lw = 1)
ax.add_patch(quadrado1)

#Figuras para o ponto rotacionado
ax.plot([vertices_q1[0,2],0], [vertices_q1[1,2],0], color = 'gray', ls = '--', lw = 1, marker = 'o', markersize = 5)
ax.text(vertices_q1[0,2]-0.25, vertices_q1[1,2]+0.05, r'($k[\cos(\alpha)-\sin(\alpha)],k[\cos(\alpha)+\sin(\alpha)]$)')  

#Configuraçoes dos eixos tipo "matemática"
ax.axis('square')
ax.set_xticks([-1,0,1])
ax.set_yticks([-1,0,1])
ax.axis([-1.2,1.2,-1.2,1.2])
ax.set_ylabel('y', loc = 'top', rotation= 'horizontal')
ax.set_xlabel('x', loc = 'right')

#Plotar eixos tipo math
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
ax.spines[["top", "right"]].set_visible(False)


# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each
# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,
# respectively) and the other one (1) is an axes coordinate (i.e., at the very
# right/top of the axes).  Also, disable clipping (clip_on=False) as the marker
# actually spills out of the axes.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.show()
