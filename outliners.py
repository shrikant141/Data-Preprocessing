# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:16:29 2021

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

boston_data = pd.read_csv("F:/DataSets/boston_data.csv")
boston_data

boston_data.dtypes
boston_data.isna().sum()

sns.boxplot(boston_data.crim)
plt.title('Boxplot')
plt.show()

IQR = boston_data['crim'].quantile(0.75) - boston_data['crim'].quantile(0.25)
IQR
lower_limit = boston_data['crim'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['crim'].quantile(0.75) + (IQR * 1.5)


boston_data['crim_replaced']= pd.DataFrame(np.where(boston_data['crim'] > upper_limit, upper_limit, np.where(boston_data['crim'] < lower_limit, lower_limit, boston_data['crim'])))
sns.boxplot(boston_data.crim_replaced);plt.title('Boxplot');plt.show()

##########
sns.boxplot(boston_data.zn)
plt.title('Boxplot')
plt.show()

IQR = boston_data['zn'].quantile(0.75) - boston_data['zn'].quantile(0.25)
IQR
lower_limit = boston_data['zn'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['zn'].quantile(0.75) + (IQR * 1.5)


boston_data['zn_replaced']= pd.DataFrame(np.where(boston_data['zn'] > upper_limit, upper_limit, np.where(boston_data['zn'] < lower_limit, lower_limit, boston_data['zn'])))
sns.boxplot(boston_data.zn_replaced);plt.title('Boxplot');plt.show()

##############
sns.boxplot(boston_data.indus)
plt.title('Boxplot')
plt.show()

#### NO outliers in indus

IQR = boston_data['indus'].quantile(0.75) - boston_data['indus'].quantile(0.25)
IQR
lower_limit = boston_data['indus'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['indus'].quantile(0.75) + (IQR * 1.5)


##############
sns.boxplot(boston_data.chas)
plt.title('Boxplot')
plt.show()

IQR = boston_data['chas'].quantile(0.75) - boston_data['chas'].quantile(0.25)
IQR
lower_limit = boston_data['chas'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['chas'].quantile(0.75) + (IQR * 1.5)


boston_data['chas_replaced']= pd.DataFrame(np.where(boston_data['chas'] > upper_limit, upper_limit, np.where(boston_data['chas'] < lower_limit, lower_limit, boston_data['chas'])))
sns.boxplot(boston_data.chas_replaced);plt.title('Boxplot');plt.show()

##############3
sns.boxplot(boston_data.nox)
plt.title('Boxplot')
plt.show()

#### NO outlers in nox

IQR = boston_data['nox'].quantile(0.75) - boston_data['nox'].quantile(0.25)
IQR
lower_limit = boston_data['nox'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['nox'].quantile(0.75) + (IQR * 1.5)


###################
sns.boxplot(boston_data.rm)
plt.title('Boxplot')
plt.show()

IQR = boston_data['rm'].quantile(0.75) - boston_data['rm'].quantile(0.25)
IQR
lower_limit = boston_data['rm'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['rm'].quantile(0.75) + (IQR * 1.5)


boston_data['rm_replaced']= pd.DataFrame(np.where(boston_data['rm'] > upper_limit, upper_limit, np.where(boston_data['rm'] < lower_limit, lower_limit, boston_data['rm'])))
sns.boxplot(boston_data.rm_replaced);plt.title('Boxplot');plt.show()

##################
sns.boxplot(boston_data.age)
plt.title('Boxplot')
plt.show()

#####  NO outliers in age

IQR = boston_data['age'].quantile(0.75) - boston_data['age'].quantile(0.25)
IQR
lower_limit = boston_data['age'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['age'].quantile(0.75) + (IQR * 1.5)


################
sns.boxplot(boston_data.dis)
plt.title('Boxplot')
plt.show()

IQR = boston_data['dis'].quantile(0.75) - boston_data['dis'].quantile(0.25)
IQR
lower_limit = boston_data['dis'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['dis'].quantile(0.75) + (IQR * 1.5)


boston_data['dis_replaced']= pd.DataFrame(np.where(boston_data['dis'] > upper_limit, upper_limit, np.where(boston_data['dis'] < lower_limit, lower_limit, boston_data['dis'])))
sns.boxplot(boston_data.dis_replaced);plt.title('Boxplot');plt.show()

####################
sns.boxplot(boston_data.rad)
plt.title('Boxplot')
plt.show()

##### NO outliers in rad

IQR = boston_data['rad'].quantile(0.75) - boston_data['rad'].quantile(0.25)
IQR
lower_limit = boston_data['rad'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['rad'].quantile(0.75) + (IQR * 1.5)


######################
sns.boxplot(boston_data.tax)
plt.title('Boxplot')
plt.show()

##### NO outliner in tax

IQR = boston_data['tax'].quantile(0.75) - boston_data['tax'].quantile(0.25)
IQR
lower_limit = boston_data['tax'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['tax'].quantile(0.75) + (IQR * 1.5)


###################
sns.boxplot(boston_data.ptratio)
plt.title('Boxplot')
plt.show()

IQR = boston_data['ptratio'].quantile(0.75) - boston_data['ptratio'].quantile(0.25)
IQR
lower_limit = boston_data['ptratio'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['ptratio'].quantile(0.75) + (IQR * 1.5)


boston_data['ptratio_replaced']= pd.DataFrame(np.where(boston_data['ptratio'] > upper_limit, upper_limit, np.where(boston_data['ptratio'] < lower_limit, lower_limit, boston_data['ptratio'])))
sns.boxplot(boston_data.ptratio_replaced);plt.title('Boxplot');plt.show()

###################
sns.boxplot(boston_data.black)
plt.title('Boxplot')
plt.show()

IQR = boston_data['black'].quantile(0.75) - boston_data['black'].quantile(0.25)
IQR
lower_limit = boston_data['black'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['black'].quantile(0.75) + (IQR * 1.5)


boston_data['black_replaced']= pd.DataFrame(np.where(boston_data['black'] > upper_limit, upper_limit, np.where(boston_data['black'] < lower_limit, lower_limit, boston_data['black'])))
sns.boxplot(boston_data.black_replaced);plt.title('Boxplot');plt.show()

##########################v
sns.boxplot(boston_data.lstat)
plt.title('Boxplot')
plt.show()

IQR = boston_data['lstat'].quantile(0.75) - boston_data['lstat'].quantile(0.25)
IQR
lower_limit = boston_data['lstat'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['lstat'].quantile(0.75) + (IQR * 1.5)


boston_data['lstat_replaced']= pd.DataFrame(np.where(boston_data['lstat'] > upper_limit, upper_limit, np.where(boston_data['lstat'] < lower_limit, lower_limit, boston_data['lstat'])))
sns.boxplot(boston_data.lstat_replaced);plt.title('Boxplot');plt.show()

######################
sns.boxplot(boston_data.medv)
plt.title('Boxplot')
plt.show()

IQR = boston_data['medv'].quantile(0.75) - boston_data['medv'].quantile(0.25)
IQR
lower_limit = boston_data['medv'].quantile(0.25) - (IQR * 1.5)
upper_limit = boston_data['medv'].quantile(0.75) + (IQR * 1.5)


boston_data['medv_replaced']= pd.DataFrame(np.where(boston_data['medv'] > upper_limit, upper_limit, np.where(boston_data['medv'] < lower_limit, lower_limit, boston_data['medv'])))
sns.boxplot(boston_data.medv_replaced);plt.title('Boxplot');plt.show()

