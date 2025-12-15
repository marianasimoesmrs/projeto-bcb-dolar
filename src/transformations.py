import pandas as pd


def to_silver(df_bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe o dataframe bruto (bronze) e devolve o dataframe da camada silver:
    - cria coluna 'data' (sem horário)
    - garante tipos numéricos
    - ordena por data/hora da cotação
    """
    df_silver = df_bronze.copy()

    # aqui assumimos que dataHoraCotacao já é datetime (do buscar_dolar_periodo)
    df_silver["data"] = df_silver["dataHoraCotacao"].dt.date

    df_silver["cotacaoCompra"] = pd.to_numeric(df_silver["cotacaoCompra"])
    df_silver["cotacaoVenda"] = pd.to_numeric(df_silver["cotacaoVenda"])

    df_silver = df_silver.sort_values("dataHoraCotacao")

    return df_silver


def to_gold(df_silver: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe o dataframe silver e devolve o dataframe gold:
    - agrega por dia
    - calcula médias, mínima, máxima e quantidade de cotações
    """
    df_gold = (
        df_silver
        .groupby("data", as_index=False)
        .agg(
            cotacao_compra_media=("cotacaoCompra", "mean"),
            cotacao_venda_media=("cotacaoVenda", "mean"),
            cotacao_compra_min=("cotacaoCompra", "min"),
            cotacao_venda_max=("cotacaoVenda", "max"),
            qtde_cotacoes=("cotacaoCompra", "count"),
        )
        .sort_values("data")
    )

    return df_gold