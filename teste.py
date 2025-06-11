from sklearn.preprocessing import KBinsDiscretizer

def binarizar_numericos(df_tmp, cols_num):
    binarizer = KBinsDiscretizer(n_bins=4, encode='onehot-dense', strategy='quantile')
    binarizer.fit(df_tmp[cols_num])
    
    # Transforma
    X_bin = binarizer.transform(df_tmp[cols_num])
    
    # Converte para DataFrame e junta com o original
    X_bin_df = pd.DataFrame(X_bin, columns=binarizer.get_feature_names_out(cols_num))
    df_trans = pd.concat([df_tmp.reset_index(drop=True), X_bin_df.reset_index(drop=True)], axis=1)
    
    return df_trans, binarizer