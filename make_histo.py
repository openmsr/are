import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

array=np.loadtxt("ARE_detectorBody150_dose.txt")
print("Photon dose: {} [Sv/sec]".format(array[:,0].sum()))
print("Neutron dose: {} [Sv/sec]".format(array[:,1].sum()))
print("Photon dose: {} [Sv/sec]".format(array[:,0].mean()))
print("Neutron dose: {} [Sv/sec]".format(array[:,1].mean()))

df1=pd.DataFrame(array[:,0],columns=["Dose[Sv/sec]"])
df1["Particle"]="Photon"
df2=pd.DataFrame(array[:,1],columns=["Dose[Sv/sec]"])
df2["Particle"]="Neutron"
DF=pd.concat([df1,df2],axis=0).reset_index(drop=True)
means=DF.groupby("Particle")["Total Dose[Sv/sec]"].mean()
sums=DF.groupby("Particle")["Mean Dose[Sv/sec]"].sum()
#ax=sns.displot(data=DF,x="Dose[Sv/sec]",hue="Particle")
#ax.fig.get_axes()[0].set_yscale("log")
#plt.show()
#plt.savefig("detectorBody_doseDistribution.png")

#plt.hist(my_df["Photon"],bins=100,density=False)
#plt.savefig("photon.png")
#plt.hist(my_df["Neutron"],bins=2,density=True)
#plt.savefig("photon.png")
