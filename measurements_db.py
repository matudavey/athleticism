# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:18:29 2016

@author: Matthew
"""


from sqlalchemy import create_engine
import pandas as pd
from matplotlib import pyplot as plt
class User:
    def __init__(self,username,pswd):
        if username == 'Matt' and pswd == 'pass':
            self.uid = 22
        else: print 'Bad Login'
        
def add_meas(meas_date,user_cfg,meas,value,units):
    engine = create_engine('mssql+pyodbc://teamsolveig:q02XxfG2@athleticism.database.windows.net:1433/measurements', echo=True)
    cols = ['meas_date','user_id','measurement', 'meas_value', 'meas_units_id']
    x = [meas_date,user_cfg.uid,meas,value,units]
    
    df = pd.DataFrame([x],columns = cols)
    df = df.set_index('meas_date')
    print df
    df.to_sql('measurements',engine, if_exists = 'append')
    
def get_mass(uid):
    query = """ SELECT meas_date, meas_value FROM [measurements].[dbo].[measurements] WHERE user_id = %d""" % uid
    engine = create_engine('mssql+pyodbc://teamsolveig:q02XxfG2@athleticism.database.windows.net:1433/measurements', echo=True)
    df = pd.read_sql(query,engine)
    df = df.set_index('meas_date')
    return df
    
if __name__ == '__main__':
    meas_date = None
    units = 1
    meas = 1
    value = 77.8
    user = User('Matt','pass')
    
    if False: # add new mass value
        add_meas(meas_date,user,meas,value,units)
        
    if False: #plot mass vs time       
        mass_df = get_mass(user.uid)
        print mass_df
        mass_df.meas_value.plot()
        plt.show()
        plt.close()
    
    fname = 'C:\Users\Matthew\Documents\Dropbox\Documents\mat fan tracker.xlsx'
    
    df = pd.read_excel(fname, sheetname = '3')
    df= df.T
    engine = create_engine('mssql+pyodbc://teamsolveig:q02XxfG2@athleticism.database.windows.net:1433/measurements', echo=True)
    df.to_sql('tbl_meas_type',engine, if_exists = 'append', index = True, index_label = 'measurement_id')