num_aggregations = {
            'AMT_ANNUITY': [ 'max', 'mean'],
            'AMT_APPLICATION': ['min', 'mean'],
            'AMT_CREDIT': ['min', 'max', 'mean'],
            'APP_CREDIT_PERC': ['min', 'max', 'mean'],
            'AMT_DOWN_PAYMENT': ['min', 'max', 'mean'],
            'AMT_GOODS_PRICE': ['min', 'max', 'mean'],
            'HOUR_APPR_PROCESS_START': ['min', 'max', 'mean'],
            'RATE_DOWN_PAYMENT': ['min', 'max', 'mean'],
            'DAYS_DECISION': ['min', 'max', 'mean'],
            'CNT_PAYMENT': ['mean', 'sum'],
        }
        
cat_aggregations = {}
     for cat in cat_cols:
           cat_aggregations[cat] = ['mean']
        
prev_agg = prev.groupby('SK_ID_CURR').agg({**num_aggregations, **cat_aggregations})

prev_agg.columns = pd.Index(['PREV_' + e[0] + "_" + e[1].upper() for e in prev_agg.columns.tolist()])
