def calculate_kpi(df):

    total_omzet = df["Omzet"].sum()

    total_target = df["Target Sales"].sum()

    achievement = (
        total_omzet /
        total_target
    )*100

    return (
        total_omzet,
        total_target,
        achievement
    )