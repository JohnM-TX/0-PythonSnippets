

#%% get date features (fast)
def date_conv(df):
    # make a lookup table
    datevals = pd.date_range(start='2016-08-01', end='2018-04-30')
    datekeys = datevals.astype(str)
    datekeys = [d.replace('-', '') for d in datekeys]
    datedict = dict(zip(datekeys, datevals))
    # lookup
    df['date'] = df.date.map(datedict)
    return df

