import pandas as pd
import os
import sys

data_frame = pd.read_csv('D:/fwdneedhelpwithcasestudy/mockup_data_articles.dsv',sep='|')
df = data_frame.sort_values(by = ['ARTICLE_CD'],ascending=[True])
df1 = data_frame.sort_values(by = ['PART_NO'],ascending=[True])
df2=df.pivot(index='ARTICLE_CD',columns='PART_NO')['COLOR']
df2.to_csv('denorm.csv',sep=',',encoding='utf-8')
print 'done'