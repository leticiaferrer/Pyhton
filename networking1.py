import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


G = nx.Graph()

#Nós
G.add_nodes_from([
    'BDKRB2', 'CXCL8', 'MAS1', 'CCL2', 'ZFP36', 'CXCL5', 'LIF', 'TCAP', 'HOPX',
    'RYR2', 'MYLK3', 'CACNA2D4', 'SNAP91', 'ZNF804A', 'MYH1', 'PDE4B', 'BHLHE40',
    'JUN', 'ICAM1', 'RRAS', 'NR4A1', 'SERPINE1', 'CCN2', 'MYLK2',
    'Abnormal renal glomerulus morphology MP 0005325', 'Cardiac fibrosis MP:0003141',
    'Increased tumor growth/size MP: 0003721', 'Decreased anxiety-related response MP:0001364',
    'Rheumathoid arthritis', 'TNF signaling pathway', 'Chagas disease',
    'AGE-RAGE signaling pathway in diabetic complications', 'Apelin signaling pathway', 'Increased response of heart to induced stress MP:0004485'
])

#Arestas
G.add_edge('Decreased anxiety-related response MP:0001364', 'CACNA2D4')
G.add_edge('Decreased anxiety-related response MP:0001364', 'SNAP91')
G.add_edge('Decreased anxiety-related response MP:0001364', 'ZNF804A')
G.add_edge('Decreased anxiety-related response MP:0001364', 'MYH1')
G.add_edge('Decreased anxiety-related response MP:0001364', 'PDE4B')
G.add_edge('BDKRB2', 'Chagas disease')
G.add_edge('BDKRB2', 'Abnormal renal glomerulus morphology MP 0005325')
G.add_edge('CXCL8','Chagas disease')
G.add_edge('CXCL8','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('CXCL8','Rheumathoid arthritis')
G.add_edge('MAS1','Abnormal renal glomerulus morphology MP 0005325')
G.add_edge('CCL2', 'Chagas disease')
G.add_edge('CCL2','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('CCL2','TNF signaling pathway')
G.add_edge('CCL2','Rheumathoid arthritis')
G.add_edge('ZFP36','Abnormal renal glomerulus morphology MP 0005325')
G.add_edge('CXCL5','Rheumathoid arthritis')
G.add_edge('CXCL5','TNF signaling pathway')
G.add_edge('LIF','TNF signaling pathway')
G.add_edge('BHLHE40','TNF signaling pathway')
G.add_edge('JUN','Chagas disease')
G.add_edge('JUN','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('ICAM1','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('ICAM1','TNF signaling pathway')
G.add_edge('ICAM1','Rheumathoid arthritis')
G.add_edge('ICAM1','Increased tumor growth/size MP: 0003721')
G.add_edge('SERPINE1','Abnormal renal glomerulus morphology MP 0005325')
G.add_edge('SERPINE1','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('SERPINE1','Chagas disease')
G.add_edge('SERPINE1','Cardiac fibrosis MP:0003141')
G.add_edge('SERPINE1','Apelin signaling pathway')
G.add_edge('RRAS','Apelin signaling pathway')
G.add_edge('RRAS','Increased tumor growth/size MP: 0003721')
G.add_edge('NR4A1','Increased tumor growth/size MP: 0003721')
G.add_edge('CCN2','Apelin signaling pathway')
G.add_edge('Apelin signaling pathway', 'MYLK2')
G.add_edge('Apelin signaling pathway', 'MYLK3')
G.add_edge('Apelin signaling pathway','RYR2')
G.add_edge('TCAP','Increased response of heart to induced stress MP:0004485')
G.add_edge('TCAP','Cardiac fibrosis MP:0003141')
G.add_edge('Increased response of heart to induced stress MP:0004485','RYR2')
G.add_edge('Increased response of heart to induced stress MP:0004485','MYLK3')
G.add_edge('Cardiac fibrosis MP:0003141','HOPX')
G.add_edge('Cardiac fibrosis MP:0003141','RYR2')
G.add_edge('Chagas disease','AGE-RAGE signaling pathway in diabetic complications')
G.add_edge('Rheumathoid arthritis','TNF signaling pathway')

#Listas
kegg = ['TNF signaling pathway', 'Chagas disease', 'AGE-RAGE signaling pathway in diabetic complications', 'Apelin signaling pathway', 'Rheumathoid arthritis']
mgi = ['Abnormal renal glomerulus morphology MP 0005325', 'Cardiac fibrosis MP:0003141', 'Increased tumor growth/size MP: 0003721', 'Decreased anxiety-related response MP:0001364', 'Increased response of heart to induced stress MP:0004485']
genes = ['BDKRB2', 'CXCL8', 'MAS1', 'CCL2', 'ZFP36', 'CXCL5', 'LIF', 'TCAP', 'HOPX', 'RYR2', 'MYLK3', 'CACNA2D4', 'SNAP91', 'ZNF804A', 'MYH1', 'PDE4B', 'BHLHE40', 'JUN', 'ICAM1', 'RRAS', 'NR4A1', 'SERPINE1', 'CCN2', 'MYLK2']

#cores
colors = {'KEGG 2021 Human': '#e3694f', 
          'MGI Mammalian Phenotype Level 4 2021': '#2f5274', 
          'Genes': '#84acc6', 'Increased response of heart to induced stress MP:0004485' : '#2f5274'}


#Atribuir cada lista a uma cor
node_colors = []
for node in G.nodes:
    if node in kegg:
        node_colors.append(colors['KEGG 2021 Human'])
    elif node in mgi:
        node_colors.append(colors['MGI Mammalian Phenotype Level 4 2021'])
    elif node in genes:
        node_colors.append(colors['Genes'])

#tamanho dos nós
node_size = 9000
#tamanho da fonte
font_size = 0.2
#posição dos nós
nx.spring_layout(G, k=200)
#tamanho  do png
plt.figure(figsize=(30, 30))



# Visualizar o gráfico com as cores atribuidas
nx.draw(G, pos=nx.spring_layout(G), node_color=node_colors)
plt.show()

#Salvar como PNG
plt.savefig('grafo.png', format='png')

