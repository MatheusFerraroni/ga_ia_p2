# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:06:55 2020

@author: lucaszl
"""

import matplotlib.pyplot as plt

results = {
           'airline_customer_satisfaction': [0.9457675136207261, 0.9434891279520373, 0.9398843043924385, 0.9446249842573368, 0.9446249842573368, 0.9446249842573368, 0.9398843043924385, 0.9434891279520373, 0.9446249842573368],
           'bands': [0.7232297634361627, 0.85482709780937, 0.8010129963056473, 0.8582509658429291, 0.8572080920020811, 0.8553106271351997, 0.833969116541077, 0.8002931870249268, 0.8124332679954971, 0.8306499379896973],
           'cellphone': [0.7284663352093257, 0.7540439003631092, 0.7516835820156592, 0.7520349151010001, 0.7566201149981417, 0.7540439003631092, 0.7544258385549605, 0.7520349151010001, 0.7544258385549605, 0.7544258385549605],
           'flag': [0.692635154319365, 0.798794740347372, 0.7923532315637578, 0.8087829422039947, 0.80394106478317, 0.8009188881294145, 0.7977519936204146, 0.8087829422039947, 0.7929651868599237, 0.7992502468291942],
           'glass': [0.6592883806247765, 0.7678706708850249, 0.7654754282607004, 0.7678706708850249, 0.7678706708850249, 0.7678706708850249, 0.7678706708850249, 0.7678706708850249, 0.7678706708850249, 0.7678706708850249],
           'IBM': [0.783887165482994, 0.47732396825680085, 0.4387435603612075, 0.47138958787668894, 0.48092131885411915, 0.4603483783495509, 0.48731870828266144, 0.4364826346867047, 0.460617557278013, 0.4674283339655272],
           'mushrooms': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
}


import matplotlib.pyplot as plt

plt.clf()
fig, ax = plt.subplots(figsize=(15, 5))

configs = ['Without\nSelection', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']

plt.title('Comparison of each end result', fontweight='bold', fontsize=15)

gap = .3 / 2.5

for i, key in enumerate(results.keys()):

    plt.bar(np.arange(0, len(results[key])) + i * gap, 
           results[key],
           label=key.upper(),
           width=gap,
           edgecolor='black',
           linewidth=1)
    
    for j in range(len(results[key])):
        ax.text(x=j+i*gap-0.1, y=results[key][j]+0.02, s='{0:.2f}'.format(results[key][j]), fontsize=7, fontweight='bold')

plt.xlabel('Configurations', fontweight='bold')
plt.ylabel('F1-score', fontweight='bold')

plt.xticks(np.arange(0, len(configs))+0.37, configs)

ax.grid(axis='y', color='gray', linestyle=':', linewidth=2, alpha=0.7)

plt.legend(ncol=3, loc=3)

#plt.show()
plt.savefig('res_classification.png', bbox_inches="tight", format='png')