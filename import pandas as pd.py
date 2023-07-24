import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

### dataset rosario
de = pd.read_csv('C:/Users/Letícia Ferreira/Desktop/Python/volcano_plot_ros/NEW_res_total_volcano.csv', sep=',', header=0, decimal='.', skipinitialspace=True)
de['diffexpressed'] = 'NO'
de.loc[(de['log2FoldChange'] > 0.58) & (de['pvalue'] < 0.05), 'diffexpressed'] = 'UP'
de.loc[(de['log2FoldChange'] < -0.58) & (de['pvalue'] < 0.05), 'diffexpressed'] = 'DOWN'
de['diffexpressed'] = pd.Categorical(de['diffexpressed'], categories=['UP', 'DOWN', 'NO'])

de['delabel'] = np.nan
de.loc[de['diffexpressed'] != 'NO', 'delabel'] = de.loc[de['diffexpressed'] != 'NO']

### Plot

plt.figure(figsize=(6, 6))
mycolors = {'DOWN': '#d377a4', 'UP': '#42a174', 'NO': 'gray'}

plt.scatter(x=de['log2FoldChange'], y=-np.log(de['pvalue']), c=de['diffexpressed'].map(mycolors), alpha=1, s=70)
for i in range(len(de)):
    if np.isfinite(de.loc[i, 'log2FoldChange']) and np.isfinite(-np.log(de.loc[i, 'pvalue'])) and de.loc[i, 'diffexpressed'] != 'NO':
        plt.text(de.loc[i, 'log2FoldChange'], -np.log(de.loc[i, 'pvalue']), de.loc[i, 'gene_name'], fontsize=6, fontweight='regular', ha='left', va='bottom')



plt.title('The DEGs of basal vs treatment of statin')
plt.xlabel('log2 (Fold-Change)')
plt.ylabel('-log10 (p-value)')
plt.axhline(y=-np.log(0.05), color='red')
plt.axvline(x=0.58, color='red')
plt.axvline(x=-0.58, color='red')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(-5, 5)
plt.gca().spines['left'].set_linewidth(0.5)
plt.gca().spines['bottom'].set_linewidth(0.5)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().xaxis.set_tick_params(width=0.5, color='black')
plt.gca().yaxis.set_tick_params(width=0.5, color='black')
plt.gca().tick_params(axis='both', which='both', direction='out', length=4, width=0.5, color='black')
plt.gca().set_facecolor('white')

plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='DOWN', markerfacecolor='#d377a4', markersize=12),
                    plt.Line2D([0], [0], marker='o', color='w', label='UP', markerfacecolor='#42a174', markersize=12),
                    plt.Line2D([0], [0], marker='o', color='w', label='NO', markerfacecolor='gray', markersize=12)],
           loc='upper left')
for i in range(len(de)):
    if not pd.isna(de.loc[i, 'delabel']):
        plt.annotate(de.loc[i, 'delabel'], (de.loc[i, 'log2FoldChange'], -np.log(de.loc[i, 'pvalue'])),
                     textcoords='offset points', xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
plt.savefig('Volcano_rosario554f.pdf')
plt.close()

